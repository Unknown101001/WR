import numpy as np
import matplotlib.pyplot as plt
from mppstart import *


def main():
    delete_old()
    manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
    manipulate_conf("hybridreaction.conf",
                    [("HybridProblem", "HybridReaction"), ("Discretization", "linear"), ("level", "2"),
                     ("T", "1.6"),
                     ("dt", "0.05"), ("Diffusion", "0.001"), ("delta", "0"), ("Reaction_0","1"),("Reaction_1","1"),
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


if __name__ == "__main__":
    main()