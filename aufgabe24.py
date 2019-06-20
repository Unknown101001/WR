import subprocess
import numpy as np
import matplotlib.pyplot as plt
kernels =  4
working_dir = "mpp/build"
#stdout = subprocess.run(['mpirun','-np',str(kernels),'M++'],stdout = subprocess.PIPE,cwd=working_dir).stdout.decode('utf-8')

def run():
    stdout = subprocess.run(['mpirun','-np',str(kernels),'M++'], stdout=subprocess.PIPE,cwd=working_dir).stdout.decode('utf-8')
def manipulate_conf(confdatei,tupelliste):
    with open("mpp/Praktikum/conf/"+confdatei) as file:
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
        with open("mpp/Praktikum/conf/"+confdatei,'w') as file:
            file.writelines([item for item in conf])


def parse_mpp_output_regex():
    pass


def parse_mpp_output_string(logfile = "mpp/build/log/log"):
    T =[]
    Outflow = []
    with open(logfile) as file:
        lines = file.readlines()
        for line in lines:
            if "Step" in line and not "default" in line and not "reading" in line:
                line = line.split()
                t = int(line[0][5:-2])
                if any("OutFlowRate" in s for s in line):
                    outflow = float(line[-1])
                else: outflow = 0
                T.append(t)
                Outflow.append(outflow)
    return T,Outflow
def parse_mpp_output_string2(logfile):
    T =[]
    Energie = []
    Mass = []
    with open(logfile) as file:
        lines = file.readlines()
        for line in lines:
            if "Step" in line and not "default" in line and not "reading" in line:
                line = line.split()
                t = int(line[0][5:-2])*0.03125
                energie = float(line[4])
                mass = float(line[7])
                T.append(t)
                Energie.append(energie)
                Mass.append(mass)

    return T,Energie,Mass






#run()
#manipulate_conf("pollution.conf",[("deg","4")])
t,energie,mass= parse_mpp_output_string2("log")
plt.figure()
plt.plot(t,energie,label = "Energie")
plt.plot(t,mass,label = "Masse")
plt.grid()
plt.legend()
plt.xlabel("Zeit")
plt.ylabel("Wert")
plt.grid(True)
plt.savefig("plot2.png")