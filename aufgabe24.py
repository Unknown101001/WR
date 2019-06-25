import subprocess
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import re
from distutils.dir_util import copy_tree

kernels = 4
working_dir = "mpp/build"


# stdout = subprocess.run(['mpirun','-np',str(kernels),'M++'],stdout = subprocess.PIPE,cwd=working_dir).stdout.decode('utf-8')

def run():
    '''
    runs M++ in working dir mpp/build with 4 kernels
    :return: output
    '''
    stdout = subprocess.run(['mpirun', '-np', str(kernels), 'M++'], stdout=subprocess.PIPE,
                            cwd=working_dir).stdout.decode('utf-8')
    return stdout.split('\n')


def manipulate_conf(confdatei, tupelliste):
    '''
    :param confdatei:
    :param tupelliste:
    :return:
    '''
    with open("mpp/Praktikum/conf/" + confdatei) as file:
        conf = file.readlines()
        # print(conf)
        for tupel in tupelliste:
            key = tupel[0]
            value = tupel[1]
            if any(key in s for s in conf):
                # print("YES")
                index = conf.index(next((s for s in conf if key in s), None))
                conf[index] = key + " = " + value + ";\n"
            else:
                # print("NO")
                new = key + " = " + value + ";\n"
                conf.append(new)
        # print(conf)
        with open("mpp/Praktikum/conf/" + confdatei, 'w') as file:
            file.writelines([item for item in conf])


def delete_old():
    '''
    deletes old vtk and log folders
    :return:
    '''
    folder = 'mpp/build/data/vtk'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path) #subdirs
        except Exception as e:
            print(e)
    folder = 'mpp/build/log'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path) #subdirs
        except Exception as e:
            print(e)


def check_dirs(name, aufgabe):
    '''
    checks target folder param is (/aufgabe/name)
    :param name:
    :param aufgabe:
    :return:
    '''
    if aufgabe is not None:
        try:
            os.mkdir(aufgabe)
            # raise FileNotFoundError
        except OSError as e:
            pass
        try:
            os.mkdir(aufgabe + "/" + name)
            # raise FileNotFoundError
        except OSError as e:
            pass
    else:
        try:
            os.mkdir(name)
            # raise FileNotFoundError
        except OSError as e:
            pass


def save(aufgabe=None, name="Neu"):
    '''
    saves content in (aufgabe)/name
    :param name: optional default is "Neu"
    :param aufgabe: optional
    :return:
    '''
    check_dirs(name, aufgabe)
    if aufgabe is None:
        toDirectory = name
    else:
        toDirectory = aufgabe + "/" + name
    fromDirectory1 = "mpp/build/data"
    fromDirectory2 = "mpp/build/log"
    copy_tree(fromDirectory1, toDirectory)
    copy_tree(fromDirectory2, toDirectory)


def parse_mpp_output_regex():
    pass


def parse_mpp_output_allg(paramlist, output=None):
    '''
    :param paramlist:
    :param output:
    :return:list of list of outputvalues
    '''
    out = []
    if output is None:
        logfile = "mpp/build/log/log"
        with open(logfile) as file:
            lines = file.readlines()
    else:
        lines = output
    for param in paramlist:
        out.append([])
        for line in lines:
            if "Step" in line and not "default" in line and not "reading" in line:
                regex = r"[+-]?[0-9]+[.]?[0-9]*[eE]?[+-]?[0-9]*"
                if param in line:
                    tmp = line.split(param)[1]
                    value = float(re.findall(regex, tmp)[0])
                    # print(value)
                else:
                    value = 0
                out[paramlist.index(param)].append(value)
    return out


def parse_mpp_output_OutFlowRate(output=None):
    T = []
    Outflow = []
    if output is None:
        logfile = "mpp/build/log/log"
        with open(logfile) as file:
            lines = file.readlines()
            for line in lines:
                if "Step" in line and not "default" in line and not "reading" in line:
                    line = line.split()
                    t = int(line[0][5:-2])
                    if any("OutFlowRate" in s for s in line):
                        outflow = float(line[-1])
                    else:
                        outflow = 0
                    T.append(t)
                    Outflow.append(outflow)
        return T, Outflow
    else:
        for line in output:
            if "Step" in line and not "default" in line and not "reading" in line:
                line = line.split()
                t = int(line[0][5:-2])
                if any("OutFlowRate" in s for s in line):
                    outflow = float(line[-1])
                else:
                    outflow = 0
                T.append(t)
                Outflow.append(outflow)
        return T, Outflow


def parse_mpp_output_EnergieMasse(logfile):
    '''
    :param logfile:
    :return:
    '''
    T = []
    Energie = []
    Mass = []
    logfile = "log"
    with open(logfile) as file:
        lines = file.readlines()
        for line in lines:
            if "Step" in line and not "default" in line and not "reading" in line:
                line = line.split()
                t = int(line[0][5:-2]) * 0.03125
                energie = float(line[4])
                mass = float(line[7])
                T.append(t)
                Energie.append(energie)
                Mass.append(mass)

    return T, Energie, Mass


def plot2():
    time, energie, mass = parse_mpp_output_EnergieMasse("log")
    plt.figure()
    plt.plot(time, energie, label="Energie")
    plt.plot(time, mass, label="Masse")
    plt.grid()
    plt.legend()
    plt.xlabel("Zeit")
    plt.ylabel("Wert")
    plt.grid(True)
    plt.savefig("plot2.png")

def main_masse():
    delete_old()
    dt = 0.5 * 0.03125
    manipulate_conf("m++conf", [("loadconf", "riemann.conf")])
    manipulate_conf("riemann.conf",
                    [("rkorder", "-2"), ("deg", "0"), ("Mesh", "Square4"), ("Problem", "Riemann"),
                     ("level", "6"), ("dt", str(dt))])
    output = run()

    out = parse_mpp_output_allg(["Step", "Mass", "OutFlowRate", "InFlowRate", "Energy", "Error"], output)
    outflow = [a * 4 * dt for a in out[2]]
    inflow = [a * 4 * dt for a in out[3]]
    print(out[0])
    print("Masse Ende: " + str(out[1][-1]))
    print("Masse Beginn: " + str(out[1][0]))
    print("Outflow: " + str(sum(outflow)))
    print("Inflow: " + str(sum(inflow)))
    save("Aufgabe21", "Test")
    dif = [out[1][i] + out[2][i] for i in range(len(out[2]))]
    plt.plot(out[0], out[1], label='mass')
    plt.plot(out[0], out[2], label='outflowrate')
    plt.plot(out[0], out[3], label='inflowrate')
    #plt.plot(out[0], out[5], label='error')
    plt.plot(out[0], outflow, label='outflow')
    plt.plot(out[0], inflow, label='inflow')

    # plt.plot(out[0], out[4], label='energy')
    plt.grid()
    plt.legend()
    plt.xlabel("Zeit")
    plt.ylabel("Wert")
    plt.grid(True)
    plt.savefig("Aufgabe21/Test/plot.png")
def main_transport():
    delete_old()
    dt = 0.5* 0.0015625
    manipulate_conf("m++conf", [("loadconf", "transport.conf")])
    manipulate_conf("transport.conf",
                    [("rkorder", "-2"), ("deg", "0"), ("Mesh", "Square-10x10quad"), ("Problem", "Circle_Wave"),
                     ("level", "6"), ("dt", str(dt))])
    output = run()

    out = parse_mpp_output_allg(["Step", "Mass", "OutFlowRate", "InFlowRate", "Energy", "Error"], output)
    outflow = [a * 10* dt for a in out[2]]
    inflow = [a * 10 * dt for a in out[3]]
    print("Masse Ende: " + str(out[1][-1]))
    print("Masse Beginn: " + str(out[1][0]))
    print("Outflow: " + str(sum(outflow)))
    print("Inflow: " + str(sum(inflow)))

    plt.plot(out[0], out[1], label='mass')
    plt.plot(out[0], out[2], label='outflow')
    plt.plot(out[0], out[3], label='inflow')
    plt.plot(out[0], out[5], label='error')
    # plt.plot(out[0], out[4], label='energy')
    plt.grid()
    plt.legend()
    plt.xlabel("Zeit")
    plt.ylabel("Wert")
    plt.grid(True)
    plt.savefig("plot.png")
    save("Aufgabe21", "Masseerhaltung_b_deg_2")


if __name__ == "__main__":
    reslist = []
    beglist = []
    dtlist = []
    reslist2 = []
    for i in range(6):
        delete_old()

        dt = 0.25 * 0.5**i
        manipulate_conf("m++conf", [("loadconf", "riemann.conf")])
        manipulate_conf("riemann.conf",
                        [("rkorder", "-2"), ("deg", "0"), ("Mesh", "Square4"), ("Problem", "Riemann"),
                         ("level", "6"), ("dt", str(dt))])
        output = run()

        out = parse_mpp_output_allg(["Step", "Mass", "OutFlowRate", "InFlowRate"], output)
        mass_beg = out[1][0]
        mass_end = out[1][-1]
        outflow = [a * 4 * dt for a in out[2]]
        inflow = [a * 4 * dt for a in out[3]]
        res = mass_end + sum(outflow) + sum(inflow)
        res2 = mass_end + sum(outflow)
        folder = "Masserverhalten"+str(dt)
        save("Aufgabe21",folder)
        dtlist.append(dt)
        reslist.append(res)
        reslist2.append(res2)
        beglist.append(mass_beg)

    print(dt)
    print(reslist)
    plt.plot(dtlist,reslist,'--bo',label = 'Masse_Ende + Outflow + Inflow')
    #plt.plot(dtlist,reslist2,label = 'Masse_Ende + Outflow')
    plt.plot(dtlist,beglist,'--go', label = 'Masse_Beginn')
    plt.xlim(0.25,0)
    plt.grid()
    plt.legend()
    plt.xlabel("Zeitschrittweite")
    plt.ylabel("Wert")
    plt.grid(True)
    plt.savefig("Aufgabe21/massoverdt2.png")

