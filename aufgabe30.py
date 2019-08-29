import numpy as np
import matplotlib.pyplot as plt
from mppstart import *


def main_30():
    '''
    fig = plt.figure('Name',figsize=(8,16))

    for r1 in ["1.5","40"]:
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
        manipulate_conf("hybridreaction.conf",
                        [("HybridProblem", "HybridReaction_logistic"), ("Discretization", "linear"), ("level", "2"),
                         ("T", "1.6"),
                         ("dt", "0.025"), ("Diffusion", "0.001"), ("delta", "0"), ("Reaction_0", "2.5"),
                         ("Reaction_1", r1),
                         ("Model", "HybridReaction"), ("Convection", "0.1")])
        output = run()
        name = "r0=2_r1=" + r1
        save("Aufgabe30",name)

    for r1 in ["0.5", "1.5","2.5", "5", "10", "20","40"]:
        name = "r0=2_r1=" + r1
        logfile = "Aufgabe30/"+name+"/log"
        out = parse_mpp_output_allg(["Step", "Mass", "OutFlowRate"], logfile=logfile)

        time = [0.025 * a for a in out[0]]
        label = "r_1 = " + r1
        plt.plot(time, out[1], label=label)

    plt.grid()
    plt.legend()
    plt.xlabel("Zeit")
    plt.ylabel("Masse")
    plt.grid(True)
    plt.savefig("Aufgabe30/vergleichsplot.png")
    '''
    delete_old()
    r0 = str(40)
    r1 = str(19.9)
    manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
    manipulate_conf("hybridreaction.conf",
                    [("HybridProblem", "HybridReaction_logistic"), ("Discretization", "linear"), ("level", "2"),
                     ("T", "1.6"),
                     ("dt", "0.05"), ("Diffusion", "0.001"), ("delta", "0"), ("Reaction_0", r0),
                     ("Reaction_1", r1),
                     ("Model", "HybridReaction"), ("Convection", "0.1"),("dt_min","0.0125")])
    output = run()
    name = "r0="+r0+"_r1=" + r1
    save("Aufgabe30", name)


def main_31():
    fig = plt.figure()
    for lvl in ["0"]:  # ,"1","2"]:
        for i in range(8):
            dt = str(0.1 * 0.5 ** i)
            delete_old()
            manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
            manipulate_conf("hybridreaction.conf",
                            [("HybridProblem", "HybridReaction"), ("Discretization", "linear"), ("level", lvl),
                             ("T", "1.6"),
                             ("dt", dt), ("Diffusion", "0.001"), ("delta", "0"), ("Reaction", "2.5"),
                             ("Model", "HybridReaction")])
            output = run()
            out = parse_mpp_output_allg(["Step", "Mass"], output)
            name = "lvl=" + lvl + "_dt=" + dt
            save("Aufgabe31", name)

            time = [0.1 * 0.5 ** i * a for a in out[0]]
            plt.plot(time, out[1], label=name)
    plt.grid()
    plt.legend()
    plt.xlabel("Zeit")
    plt.ylabel("Wert")
    plt.grid(True)
    plt.savefig("Aufgabe31/plot.png")


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
    for lvl in ["0"]:  # , "1", "2"]:
        oldmass = []
        print(lvl)
        for i in range(5):
            dt = str(0.1 * 0.5 ** i)
            name = "lvl=" + lvl + "_dt=" + dt
            path = "Aufgabe31/" + name + "/log"
            out = parse_mpp_output_allg(["Step", "Mass"], logfile=path)
            time = [0.1 * 0.5 ** i * a for a in out[0]]
            mass = out[1]
            if i > 0:
                maxi = max([a - b for a, b in zip(mass[::2], oldmass)])
                print(maxi)
            oldmass = mass


def main_32():
    diffls = [0.001, 0.0001, 0.00001, 0.000001]
    for diff in diffls:
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
        manipulate_conf("hybridreaction.conf",
                        [("HybridProblem", "HybridReaction"), ("Discretization", "linear"), ("level", "2"),
                         ("T", "1.6"),
                         ("dt", "0.025"), ("Diffusion", str(diff)), ("delta", "0.025"), ("Reaction", "5"),
                         ("Model", "HybridReaction"), ("Convection", "1")])
        output = run()
        name = "delta=0.025_diffusion=" + str(diff)
        print(name)
        print("done")
        save("Aufgabe32", name)
        out = parse_mpp_output_allg(["Step", "Mass", "OutFlowRate"], output)
        fig = plt.figure()
        time = [0.05 * a for a in out[0]]
        plt.subplot(211)
        plt.plot(time, out[1], label='Masse')
        plt.grid()
        plt.legend()
        plt.xlabel("Zeit")
        plt.ylabel("Wert")
        plt.grid(True)
        plt.subplot(212)
        plt.plot(time, out[2], label='OutFlowRate')
        plt.grid()
        plt.legend()
        plt.xlabel("Zeit")
        plt.ylabel("Wert")
        plt.grid(True)

        plt.subplots_adjust(hspace=0.35)
        plt.savefig("Aufgabe32/" + name + "/plot.png")
        '''
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])   
        manipulate_conf("hybridreaction.conf",
                        [("HybridProblem", "HybridReaction"), ("Discretization", "linear"), ("level", "2"),
                         ("T", "1.6"),
                         ("dt", "0.025"), ("Diffusion", str(diff)), ("delta", "0"), ("Reaction", "2"),
                         ("Model", "HybridReaction")])
        output = run()
        name = "reaction=0_diffusion=" + str(diff)
        print(name)
        print("done")
        save("Aufgabe32", name)
        '''


if __name__ == "__main__":
    # main_32()
    # main_31()
    main_30()
    # main_31b()
