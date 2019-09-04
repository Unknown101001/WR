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
    for lvl in ["0","1","2","3"]:
        delete_old()
        manipulate_conf("m++conf", [("loadconf","laplace.conf")])
        manipulate_conf("laplace.conf",
                        [("level",lvl), ("Mesh","UnitSquare"),("Discretization","linear")])
        output = run()
        out = parse_mpp_output_single_inform("Problem size",output)
        outp.append(out)
        name = "Test2_"+lvl
        save(None, name)
    print(outp)


if __name__ == "__main__":
    main()

