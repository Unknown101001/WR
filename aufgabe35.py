import numpy as np
import matplotlib.pyplot as plt
from mppstart import *


def main():


    for lvl in ["0", "1", "2", "3"]:
        for disc in ["linear", "serendipity"]:
            delete_old()
            manipulate_conf("m++conf", [("loadconf", "laplace.conf")])
            manipulate_conf("laplace.conf",
                            [("Model", "Laplace"), ("Problem", "Simple2D"), ("Mesh", "Square500"),
                             ("Discretization", disc), ("level", lvl)])
            output = run()
            # out = parse_mpp_output_allg(["Step","Flux Error","Flux Loss","Problem size"], output)
            # out2 = parse_mpp_output_single_inform(["Problem size"])+
            name = "FEM_lvl=" + lvl + "_disc=" + disc
            save("Aufgabe35", name)

    # 2)

    for lvl in ["0", "1", "2", "3"]:
        for konf in ["sym", "nonsym"]:
            delete_old()
            manipulate_conf("m++conf", [("loadconf", "dglaplace.conf")])
            if konf == "sym":
                manipulate_conf("dglaplace.conf",
                                [("Model", "DGLaplace"), ("Problem", "Simple2D"), ("Mesh", "Square500"),
                                 ("deg", "1"), ("level", lvl), ("sign", "1"), ("penalty", "25"),
                                 ("Preconditioner", "Multigrid"),("LinearSteps","2000")])
            else:
                manipulate_conf("dglaplace.conf",
                                [("Model", "DGLaplace"), ("Problem", "Simple2D"), ("Mesh", "Square500"),
                                 ("deg", "1"), ("level", lvl), ("sign", "-1"), ("penalty", "0"),
                                 ("Preconditioner", "Jacobi"), ("LinearSteps", "10000")])
            output = run()
            # out = parse_mpp_output_allg(["Step","Flux Error","Flux Loss","Problem size"], output)
            # out2 = parse_mpp_output_single_inform(["Problem size"])+
            name = "DG_lvl=" + lvl + "_konf=" + konf
            save("Aufgabe35", name)

    # 3a)

    for lvl in ["0", "1", "2", "3"]:
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "dglaplace.conf")])
        manipulate_conf("dglaplace.conf",
                        [("Model", "DGLaplace"), ("Problem", "Simple2D"), ("Mesh", "Square500"),
                         ("deg", "2"), ("level", lvl), ("sign", "1"), ("penalty", "25"),
                         ("Preconditioner", "Multigrid"),("LinearSteps","2000")])
        output = run()
        # out = parse_mpp_output_allg(["Step","Flux Error","Flux Loss","Problem size"], output)
        # out2 = parse_mpp_output_single_inform(["Problem size"])+
        name = "DG2_lvl=" + lvl
        save("Aufgabe35", name)
    #3b)
    for penalty in ["0","1","5","10","25","50","100"]:
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "dglaplace.conf")])
        manipulate_conf("dglaplace.conf",
                        [("Model", "DGLaplace"), ("Problem", "Simple2D"), ("Mesh", "Square500"),
                         ("deg", "2"), ("level", "3"), ("sign", "1"), ("penalty", penalty),
                         ("Preconditioner", "Multigrid")])
        output = run()
        # out = parse_mpp_output_allg(["Step","Flux Error","Flux Loss","Problem size"], output)
        # out2 = parse_mpp_output_single_inform(["Problem size"])+
        name = "DG3_penalty=" + penalty
        save("Aufgabe35", name)

def read_error():
    for lvl in ["0", "1", "2", "3"]:
        for disc in ["linear", "serendipity"]:
            name = "FEM_lvl=" + lvl + "_disc=" + disc
            logfile = "Aufgabe35/"+name+"/log"
            out = parse_mpp_output_single_inform(["Flux Error","Flux Loss","Problem size"],logfile=logfile)
            print(out)
            print(get_time(out))


if __name__ == "__main__":
    #main()
    read_error()