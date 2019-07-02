import numpy as np
import matplotlib.pyplot as plt
from mppstart import *


def main_30a():
    delete_old()
    manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
    manipulate_conf("hybridreaction.conf",
                    [("HybridProblem", "HybridReaction_logistic"), ("Discretization", "linear"), ("level", "2"),
                     ("T", "1.6"),
                     ("dt", "0.05"), ("Diffusion", "0.001"), ("delta", "0"), ("Reaction_0","1"),("Reaction_1","5"),
                     ("Model", "HybridReaction"),("Convection","0.1")])
    output = run()
    out = parse_mpp_output_allg(["Step", "Mass", "OutFlowRate"], output)
    name = "Test"
    save("Aufgabe30", name)
    print("Plotting....")
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
    plt.savefig("Aufgabe30/" + name + "/plot.png")

    print("saved")

def main_31():
    delete_old()
    manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
    lvl = 0
    dt = 0.05
    manipulate_conf("hybridreaction.conf",
                    [("HybridProblem", "HybridReaction"), ("Discretization", "linear"), ("level", str(lvl)),
                     ("T", "1.6"),
                     ("dt", str(dt)), ("Diffusion", "0.001"), ("delta", "0"),("Reaction","2.5"),
                     ("Model", "HybridReaction")])
    output = run()
    out = parse_mpp_output_allg(["Step", "Mass", "OutFlowRate"], output)
    out = parse_mpp_output_allg(["Step", "Mass", "OutFlowRate"], output)
    name = "Blub"
    save("Aufgabe31", name)
    print("Plotting....")
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
    plt.savefig("Aufgabe31/" + name + "/plot.png")

    print("saved")
def main_32():
    diffls = [0.001, 0.0001, 0.00001, 0.000001]
    for diff in diffls:
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
        manipulate_conf("hybridreaction.conf",
                        [("HybridProblem", "HybridReaction"), ("Discretization", "linear"), ("level", "2"),
                         ("T", "1.6"),
                         ("dt", "0.025"), ("Diffusion", str(diff)), ("delta", "0.5"), ("Reaction", "5"),
                         ("Model", "HybridReaction"),("Convection","1")])
        output = run()
        name = "reaction=5_diffusion=" + str(diff)
        print(name)
        print("done")
        save("Aufgabe32",name )
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
    main_32()