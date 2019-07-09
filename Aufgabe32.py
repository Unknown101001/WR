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
                         ("dt", "0.025"), ("Diffusion", str(diff)), ("delta", "0.1"), ("Reaction", "0"),
                         ("Model", "HybridReaction"), ("Convection", "1")])
        output = run()
        name = "delta=0.0025_diffusion=" + str(diff) + "Reaktion=0"
        print(name)
        print("done")
        save("Aufgabe32", name)


if __name__ == "__main__":
    main_32()
    # main_31()
    #main_30()
    # main_31b()
