import numpy as np
import matplotlib.pyplot as plt
from mppstart import *
import csv

def parseplot():
    out = parse_mpp_output_allg(["Step", "Mass", "OutFlowRate"],logfile="Aufgabe24/Level2Deg2/log/log") #logfile="Aufgabe38/Neu/log"
    time = [0.005 * a for a in out[0]]
    fig = plt.figure(1)
    plt.plot(time, out[1], label="Masse")
    plt.grid()
    plt.legend()
    plt.xlabel("Zeit")
    plt.ylabel("Masse")
    plt.grid(True)
    plt.savefig("Aufgabe24/Level2Deg2/plotmasse.png")

import numpy as np
import matplotlib.pyplot as plt
from mppstart import *

def main():
    outp = []
    for prob in ["Discontinuous","Simple"]:
        for lvl in ["1","2","3","4","5","6","7","8"]:
            delete_old()
            manipulate_conf("m++conf", [("loadconf","laplace.conf")])
            manipulate_conf("laplace.conf",
                            [("level",lvl),("plevel","7"),("Preconditioner","Multigrid"),
                             ("Mesh","UnitSquare"),("Discretization","linear"),("Problem", prob),("LinearSteps","1000")])
            output = run()
            name = "test_"+lvl+"_"+prob
            save("Abb5", name)

def write_to_csv(saveload):
    outputfile = "Abb5/data.csv"
    with open(outputfile, 'w', newline='', encoding='utf-8')as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([a[0] for a in saveload])  # names
        writer.writerow([int(a[1]) for a in saveload])  # Problem Size
        writer.writerow([float(a[2]) for a in saveload])  # Inflow
        writer.writerow([float(a[3]) for a in saveload])  # Outflow
        writer.writerow([float(a[4]) for a in saveload])  # Flux Error
        writer.writerow([float(a[5]) for a in saveload])  # Flux Loss
        writer.writerow([a[6] for a in saveload])  # time
        writer.writerow([a[7] for a in saveload])  # einheit

def read_values():
    saveload = []
    for prob in ["Discontinuous", "Simple"]:
        for lvl in ["1","2","3","4","5","6","7","8"]:
            name = "test_"+lvl+"_"+prob
            logfile = "Abb5/" + name + "/log"
            out = parse_mpp_output_single_inform(["Problem size", "Inflow", "Outflow", "Flux Error", "Flux Loss"],
                                                 logfile=logfile)
            time, einheit = get_time(logfile=logfile)
            liste = [name, out[0][0], out[1][0], out[2][0], out[3][0], out[4][0], time, einheit]
            # print(liste)
            saveload.append(liste)
    return saveload


if __name__ == "__main__":
    main()
    saveload = read_values()
    write_to_csv(saveload)

