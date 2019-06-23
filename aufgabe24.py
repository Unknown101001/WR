import subprocess
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
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
        print(conf)
        for tupel in tupelliste:
            key = tupel[0]
            value = tupel[1]
            if any(key in s for s in conf):
                print("YES")
                index = conf.index(next((s for s in conf if key in s), None))
                conf[index] = key + " = " + value + ";\n"
            else:
                print("NO")
                new = key + " = " + value + ";\n"
                conf.append(new)
        print(conf)
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
            raise FileNotFoundError
        except OSError as e:
            pass
        try:
            os.mkdir(aufgabe + "/" + name)
            raise FileNotFoundError
        except OSError as e:
            pass
    else:
        try:
            os.mkdir(name)
            raise FileNotFoundError
        except OSError as e:
            pass


def save(name="Neu", aufgabe=None):
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


def parse_mpp_output_string(output=None):
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


def parse_mpp_output_string2(logfile):
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
    t, energie, mass = parse_mpp_output_string2("log")
    plt.figure()
    plt.plot(t, energie, label="Energie")
    plt.plot(t, mass, label="Masse")
    plt.grid()
    plt.legend()
    plt.xlabel("Zeit")
    plt.ylabel("Wert")
    plt.grid(True)
    plt.savefig("plot2.png")


if __name__ == "__main__":
    delete_old()
    # manipulate_conf("pollution.conf",[("deg","4")])
    output = run()
    t, out = parse_mpp_output_string(output)
    print(t)
    print(out)
    save()
