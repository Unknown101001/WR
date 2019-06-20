import subprocess
import numpy as np
import matplotlib.pyplot as plt
kernels =  4
working_dir = ".."
#stdout = subprocess.run(['mpirun','-np',str(kernels),'M++'],stdout = subprocess.PIPE,cwd=working_dir).stdout.decode('utf-8')

def run():
    stdout = subprocess.run(['mpirun','-np',str(kernels),'M++'], stdout=subprocess.PIPE,cwd=working_dir).stdout.decode('utf-8')
def manipulate_conf(confdatei,tupelliste):
    with open("../../Praktikum/conf/"+confdatei) as file:
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
        with open("../../Praktikum/conf/"+confdatei,'w') as file:
            file.writelines([item for item in conf])


def parse_mpp_output_regex():
    pass


def parse_mpp_output_string(logfile):
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






#run()
#manipulate_conf("pollution.conf",[("deg","4")])
t,outflow = parse_mpp_output_string("log")
plt.figure()
plt.plot(t,outflow)
plt.grid()
plt.xlabel("Zeit")
plt.ylabel("OutFlowRate")
plt.grid(True)
plt.savefig("plot1.png")