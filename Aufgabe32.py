import numpy as np
import matplotlib.pyplot as plt
from mppstart import *




def main_32():
    diffls = [0.000001]
    for diff in diffls:
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
        manipulate_conf("hybridreaction.conf",
                        [("HybridProblem", "HybridReaction"), ("Discretization", "linear"), ("level", "2"),
                         ("T", "1.6"),
                         ("dt", "0.025"), ("Diffusion", str(diff)), ("delta", "0.1"), ("Reaction", "5"),
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
    main_32()
    # main_31()
    #main_30()
    # main_31b()
