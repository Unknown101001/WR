import numpy as np
import matplotlib.pyplot as plt
from mppstart import *


def main_Jac_GMRES():
    for lvl in ["3", "4", "5", "6", "7", "8", "9"]:
        prec = "Jacobi"
        ls = "GMRES"
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "laplace.conf")])
        manipulate_conf("laplace.conf",
                        [("Problem", "Simple2D"),
                         ("Mesh", "UnitSquare"),
                         ("level", lvl),
                         ("Preconditioner", prec),
                         ("LinearSteps", "800"),
                         ("LinearSolver", ls)])
        output = run()
        # out = parse_mpp_output_allg([], output)
        # print(out)
        name = prec + "_" + ls + "_" + lvl
        save("Aufgabe10", name)


def main_GS_GMRES():
    for lvl in ["3", "4", "5", "6", "7", "8", "9"]:
        prec = "GaussSeidel"
        ls = "GMRES"
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "laplace.conf")])
        manipulate_conf("laplace.conf",
                        [("Problem", "Simple2D"),
                         ("Mesh", "UnitSquare"),
                         ("level", lvl),
                         ("Preconditioner", prec),
                         ("LinearSteps", "800"),
                         ("LinearSolver", ls)])
        output = run()
        # out = parse_mpp_output_allg([], output)
        # print(out)
        name = prec + "_" + ls + "_" + lvl
        save("Aufgabe10", name)


def main_MG_GMRES():
    for lvl in ["3", "4", "5", "6", "7", "8", "9"]:
        prec = "Multigrid"
        ls = "GMRES"
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "laplace.conf")])
        manipulate_conf("laplace.conf",
                        [("Problem", "Simple2D"),
                         ("Mesh", "UnitSquare"),
                         ("level", lvl),
                         ("Preconditioner", prec),
                         ("LinearSteps", "800"),
                         ("LinearSolver", ls),
                         ("plevel", "2"),
                         ("BasePreconditioner", "LIB_PS")])
        output = run()
        # out = parse_mpp_output_allg([], output)
        # print(out)
        name = prec + "_" + ls + "_" + lvl
        save("Aufgabe10", name)

def main_Jac_CG():
    for lvl in ["3", "4", "5", "6", "7", "8", "9"]:
        prec = "Jacobi"
        ls = "CG"
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "laplace.conf")])
        manipulate_conf("laplace.conf",
                        [("Problem", "Simple2D"),
                         ("Mesh", "UnitSquare"),
                         ("level", lvl),
                         ("Preconditioner", prec),
                         ("LinearSteps", "800"),
                         ("LinearSolver", ls),
                         ("LinearVerbos","1")])
        output = run()
        # out = parse_mpp_output_allg([], output)
        # print(out)
        name = prec + "_" + ls + "_" + lvl
        save("Aufgabe10", name)

def main_SGS_CG():
    for lvl in ["3", "4", "5", "6", "7", "8", "9"]:
        prec = "SGS"
        ls = "CG"
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "laplace.conf")])
        manipulate_conf("laplace.conf",
                        [("Problem", "Simple2D"),
                         ("Mesh", "UnitSquare"),
                         ("level", lvl),
                         ("Preconditioner", prec),
                         ("LinearSteps", "800"),
                         ("LinearSolver", ls)])
        output = run()
        # out = parse_mpp_output_allg([], output)
        # print(out)
        name = prec + "_" + ls + "_" + lvl
        save("Aufgabe10", name)

def main_MG_CG():
    for lvl in ["3", "4", "5", "6", "7", "8", "9"]:
        prec = "Multigrid"
        ls = "CG"
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "laplace.conf")])
        manipulate_conf("laplace.conf",
                        [("Problem", "Simple2D"),
                         ("Mesh", "UnitSquare"),
                         ("level", lvl),
                         ("Preconditioner", prec),
                         ("LinearSteps", "800"),
                         ("LinearSolver", ls),
                         ("plevel", "2"),
                         ("BasePreconditioner", "LIB_PS")])
        output = run()
        # out = parse_mpp_output_allg([], output)
        # print(out)
        name = prec + "_" + ls + "_" + lvl
        save("Aufgabe10", name)




if __name__ == "__main__":
    main_GS_GMRES()
    main_Jac_GMRES()
    main_MG_GMRES()

    main_Jac_CG()
    main_MG_CG()
    main_SGS_CG()
