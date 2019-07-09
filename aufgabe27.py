import subprocess
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import re
from distutils.dir_util import copy_tree
import sys
from mppstart import *


def main_27a():
    rels = [-2.5, -1, 0, 1, 2.5, 5]
    rels = [2.5]
    for react in rels:
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
        manipulate_conf("hybridreaction.conf",
                        [("HybridProblem", "HybridReaction"), ("Discretization", "linear"), ("level", "2"),
                         ("T", "1.6"),
                         ("dt", "0.025"), ("Diffusion", "0.001"), ("delta", "0"), ("Reaction", str(react)),
                         ("Model", "HybridReaction"), ("Convection", "0.1")])
        output = run()

        name = "lowconvecreaction=" + str(react)
        save("Aufgabe27", name)
        out = parse_mpp_output_allg(["Step", "Mass", "OutFlowRate"], output)
        fig = plt.figure()
        time = [0.025 * a for a in out[0]]
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
        plt.savefig("Aufgabe27/" + name + "/plot.png")
        # plt.show()
        print(react)
        print("done")


def main_27_b():
    diffls = [0.0001, 0.00001, 0.000001]
    for diff in diffls:
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
        manipulate_conf("hybridreaction.conf",
                        [("HybridProblem", "HybridReaction"), ("Discretization", "linear"), ("level", "2"),
                         ("T", "1.6"),
                         ("dt", "0.025"), ("Diffusion", str(diff)), ("delta", "0"), ("Reaction", "5"),
                         ("Model", "HybridReaction")])
        output = run()
        name = "reaction=5_diffusion=" + str(diff)
        print(name)
        print("done")
        # save("Aufgabe27", name)

        delete_old()
        manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
        manipulate_conf("hybridreaction.conf",
                        [("HybridProblem", "HybridReaction"), ("Discretization", "linear"), ("level", "2"),
                         ("T", "1.6"),
                         ("dt", "0.025"), ("Diffusion", str(diff)), ("delta", "0"), ("Reaction", "0"),
                         ("Model", "HybridReaction")])
        output = run()
        name = "reaction=0_diffusion=" + str(diff)
        print(name)
        print("done")
        # save("Aufgabe27", name)
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
        plt.savefig("Aufgabe27/" + name + "/plot.png")
        print("done")


def main_27_c():
    diffls = [0.000001]  # , 0.00001, 0.000001]
    for diff in diffls:
        '''
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
        manipulate_conf("hybridreaction.conf",
                        [("HybridProblem", "HybridReaction"), ("Discretization", "serendipity"), ("level", "2"),
                         ("T", "1.6"),
                         ("dt", "0.025"), ("Diffusion", str(diff)), ("delta", "0"), ("Reaction", "5"),("Model","HybridReaction")])
        7
        output = run()
        name = "serendipity_lvl=2_reaction=5_diffusion=" + str(diff)
        print(name)
        print("done")
        save("Aufgabe27", name)
        '''
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
        manipulate_conf("hybridreaction.conf",
                        [("HybridProblem", "HybridReaction"), ("Discretization", "serendipity"), ("level", "3"),
                         ("T", "1.6"),
                         ("dt", "0.025"), ("Diffusion", str(diff)), ("delta", "0"), ("Reaction", "5"),
                         ("Model", "HybridReaction")])

        output = run()
        name = "serendipity_lvl=3_reaction=5_diffusion=" + str(diff)
        print(name)
        print("done")
        # save("Aufgabe27", name)
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
        plt.savefig("Aufgabe27/" + name + "/plot.png")
        print("done")


def gen_plots():
    for dt in ["0.0001", "1e-05", "1e-06"]:
        path = "Aufgabe27/b/reaction=0_diffusion=" + dt
        out = parse_mpp_output_allg(["Step", "Mass", "OutFlowRate"], logfile=path + "/log")
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
        plt.savefig(path + "/plot.png")
        print("done")


def gen_plots():
    # for dt in ["0.0001","1e-05","1e-06"]:  #c/serendipity_lvl=3_ #
    for r in ["-2.5", "-1", "0", "1", "2.5", "5"]:
        # path = "Aufgabe27/b/reaction=0_diffusion="+dt
        path = "Aufgabe27/a/reaction=" + r
        out = parse_mpp_output_allg(["Step", "Mass", "OutFlowRate"], logfile=path + "/log")
        fig = plt.figure()
        time = [0.025 * a for a in out[0]]
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
        plt.savefig(path + "/plot.png")
        print("done")


def vgl_30():
    for lvl in ["2", "3"]:
        diff = 0.000001
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "hybridreaction.conf")])
        manipulate_conf("hybridreaction.conf",
                        [("HybridProblem", "HybridReaction"), ("Discretization", "serendipity"), ("level", lvl),
                         ("T", "1.6"),
                         ("dt", "0.025"), ("Diffusion", str(diff)), ("delta", "0"), ("Reaction", "0"),
                         ("Model", "HybridReaction")])

        output = run()
        name = "serendipity_lvl="+lvl+"_reaction=0_diffusion=" + str(diff)
        print(name)
        print("done")
        save("Aufgabe27", name)

if __name__ == "__main__":
            #main_27a()
        # main_27_b()
        # main_27_c()
        # gen_plots()
    vgl_30()
