import numpy as np
import matplotlib.pyplot as plt
from mppstart import *
import seaborn as sns
import pandas as pd
from scipy.interpolate import UnivariateSpline
from scipy.integrate import quad


def main_31():
    for lvl in ["3"]:
        for i in range(9):
            dt = str(0.8 * 0.5 ** i)
            delete_old()
            manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
            manipulate_conf("hybridreaction.conf",
                            [("HybridProblem", "HybridReaction"), ("Discretization", "linear"), ("level", lvl),
                             ("T", "1.6"),
                             ("dt", dt), ("Diffusion", "0.001"), ("delta", "0"), ("Reaction", "2.5"),
                             ("Model", "HybridReaction"), ("Convection", "1.0")])
            output = run()
            name = "lvl=" + lvl + "_dt=" + dt
            save("Aufgabe31", name)


def main_31b():
    '''
    for i in range(5):
        fig = plt.figure()
        for lvl in ["0","1","2"]:
            dt = str(0.1 * 0.5 ** i)
            name = "lvl=" + lvl + "_dt=" + dt
            path = "Aufgabe31/"+name+"/log"
            out = parse_mpp_output_allg(["Step", "Mass"], logfile = path)
            time = [0.1 * 0.5 ** i * a for a in out[0]]
            plt.plot(time, out[1], label=name)
        plt.grid()
        plt.legend()
        plt.xlabel("Zeit")
        plt.ylabel("Wert")
        plt.grid(True)
        newname = lvl +"vergleich_dt="+dt
        plt.savefig("Aufgabe31/"+newname+"_plot.png")
    '''
    ddt = []
    dlvl = []

    for lvl in ["0", "1", "2", "3"]:
        fig = plt.figure()
        oldmass = []
        print(lvl)
        for i in range(9):
            if i == 8 and lvl == "3":
                ddt.append(0)
                continue
            dt = str(0.8 * 0.5 ** i)
            name = "lvl=" + lvl + "_dt=" + dt
            path = "Aufgabe31/" + name + "/log"
            out = parse_mpp_output_allg(["Step", "Mass"], logfile=path)
            time = [0.8 * 0.5 ** i * a for a in out[0]]
            mass = out[1]
            #s1 = UnivariateSpline(time, [abs(m) for m in mass], k=3)
            #newi = s1.integral(0, 1.6)
            if i > 0:
                maxi = max([abs(a - b) for a, b in zip(mass[::2], oldmass)])
                #maxi = abs(newi - oldi)
                print(maxi)
                ddt.append(maxi)
            oldmass = mass
            #oldi = newi
            plt.plot(time, mass, label=name)
        plt.grid(True)
        plt.legend()
        plt.ylim(-0.025, 0.32)
        plt.xlabel("Zeit")
        plt.ylabel("Wert")
        newname = "zeitvergleich_lvl=" + lvl
        plt.savefig("Aufgabe31/" + newname + "_plot.png")

    for i in range(8):
        oldmass = []
        fig = plt.figure()
        dt = str(0.8 * 0.5 ** i)
        for lvl in ["0", "1", "2", "3"]:
            name = "lvl=" + lvl + "_dt=" + dt
            path = "Aufgabe31/" + name + "/log"
            out = parse_mpp_output_allg(["Step", "Mass"], logfile=path)
            time = [0.8 * 0.5 ** i * a for a in out[0]]
            mass = out[1]
            #s1 = UnivariateSpline(time,[abs(m) for m in mass],k=3)
            #newi = s1.integral(0,1.6)
            if lvl != "0":
                print(lvl + ";" + dt)
                maxi = max([abs(a - b) for a, b in zip(mass[::2], oldmass)])
                #maxi = abs(newi-oldi)
                print(maxi)
                dlvl.append(maxi)
            oldmass = mass
            #oldi = newi
            plt.plot(time, mass, label=name)
        plt.ylim(-0.025, 0.32)
        plt.grid(True)
        plt.legend()
        plt.xlabel("Zeit")
        plt.ylabel("Wert")
        newname = lvl + "vergleich_dt=" + dt
        plt.savefig("Aufgabe31/" + newname + "_plot.png")

    return ddt, dlvl


def generate_new(lvl, dt):
    delete_old()
    manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
    manipulate_conf("hybridreaction.conf",
                    [("HybridProblem", "HybridReaction"), ("Discretization", "linear"), ("level", lvl),
                     ("T", "1.6"),
                     ("dt", dt), ("Diffusion", "0.001"), ("delta", "0"), ("Reaction", "2.5"),
                     ("Model", "HybridReaction")])
    output = run()
    name = "lvl=" + lvl + "_dt=" + dt
    save("Aufgabe31", name)


def plot_heat(d, d2):
    plt.subplot(211)
    plt.title("Unterschied zwischen den Zeitschritten dt")
    '''
           '0.8': [d[0], d[8], d[16]],
           '0.4': [d[1], d[9], d[17]],
           '0.2': [d[2], d[10], d[18]],
           '0.1': [d[3], d[11], d[19]],
           '0.05': [d[4], d[12], d[20]],
           '0.025': [d[5], d[13], d[21]],
           '0.0125': [d[6], d[14], d[22]],
           '0.00625': [d[7], d[15], d[23]]
           '''
    dat = {
            '0.8': [d[0], d[8], d[16]],
           '0.4': [d[1], d[9], d[17]],
           '0.2': [d[2], d[10], d[18]],
           '0.1': [d[3], d[11], d[19]],
           '0.05': [d[4], d[12], d[20]],
           '0.025': [d[5], d[13], d[21]],
           '0.0125': [d[6], d[14], d[22]],
           '0.00625': [d[7], d[15], d[23]]
    }
    data = pd.DataFrame(data=dat)
    ax = sns.heatmap(data, annot=True, cbar_kws={"orientation": "horizontal"}, cmap="YlGnBu")
    plt.yticks(rotation=0)
    plt.xticks(rotation=0)

    plt.subplot(212)
    plt.title("Unterschied zwischen den Leveln")
    '''
           '0.8': [d2[0], d2[1], d2[2]],
           '0.4': [d2[3], d2[4], d2[5]],
           '0.2': [d2[6], d2[7], d2[8]],
           '0.1': [d2[9], d2[10], d2[11]],
           '0.05': [d2[12], d2[13], d2[14]],
           '0.025': [d2[15], d2[16], d2[17]],
           '0.0125': [d2[18], d2[19], d2[20]],
           '0.00625': [d2[21], d2[22], d2[23]]
           '''
    dat = {
            '0.8': [d2[0], d2[1], d2[2]],
           '0.4': [d2[3], d2[4], d2[5]],
           '0.2': [d2[6], d2[7], d2[8]],
           '0.1': [d2[9], d2[10], d2[11]],
           '0.05': [d2[12], d2[13], d2[14]],
           '0.025': [d2[15], d2[16], d2[17]],
           '0.0125': [d2[18], d2[19], d2[20]],
           '0.00625': [d2[21], d2[22], d2[23]]
    }
    data = pd.DataFrame(data=dat)
    ax = sns.heatmap(data, annot=True, cbar_kws={"orientation": "horizontal"}, cmap="YlGnBu")
    plt.yticks(rotation=0)
    plt.xticks(rotation=0)
    plt.subplots_adjust(hspace=0.4)
    plt.savefig("Aufgabe31/Heatmapblub.png")


if __name__ == "__main__":
    # main_31()
    dat1, dat2 = main_31b()
    plot_heat(dat1, dat2)
