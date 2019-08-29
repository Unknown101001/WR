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
        output = run(1)
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
        output = run(1)
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
        output = run(1)
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
                         ("LinearVerbose", "1")])
        output = run(1)
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
        output = run(1)
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
        output = run(1)
        # out = parse_mpp_output_allg([], output)
        # print(out)
        name = prec + "_" + ls + "_" + lvl
        save("Aufgabe10", name)


def main_Jac_CG_2():
    lvl = "6"
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
                     ("LinearVerbose", "1")])
    output = run(2)
    # out = parse_mpp_output_allg([], output)
    # print(out)
    name = prec + "_" + ls + "_" + lvl + "_2proc"
    save("Aufgabe10", name)


def main_Jac_CG_4():
    lvl = "4"
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
                     ("LinearVerbose", "1")])
    output = run(4)
    # out = parse_mpp_output_allg([], output)
    # print(out)
    name = prec + "_" + ls + "_" + lvl + "_4proc"
    save("Aufgabe10", name)


def main_Jac_CG_probs():
    for prob in ["Discontinuous", "Divergent", "Simple2D"]:
        lvl = "4"
        prec = "Jacobi"
        ls = "CG"
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "laplace.conf")])
        manipulate_conf("laplace.conf",
                        [("Problem", prob),
                         ("Mesh", "UnitSquare"),
                         ("level", lvl),
                         ("Preconditioner", prec),
                         ("LinearSteps", "800"),
                         ("LinearSolver", ls),
                         ("LinearVerbose", "1")])
        output = run(1)
        # out = parse_mpp_output_allg([], output)
        # print(out)
        name = prec + "_" + ls + "_" + lvl + "_Problem-" + prob
        save("Aufgabe10", name)


def main_Jac_CMRES_probs():
    for prob in ["Discontinuous", "Divergent", "Simple2D"]:
        lvl = "6"
        prec = "Jacobi"
        ls = "GMRES"
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "laplace.conf")])
        manipulate_conf("laplace.conf",
                        [("Problem", prob),
                         ("Mesh", "UnitSquare"),
                         ("level", lvl),
                         ("Preconditioner", prec),
                         ("LinearSteps", "800"),
                         ("LinearSolver", ls),
                         ("LinearVerbose", "1")])
        output = run(1)
        # out = parse_mpp_output_allg([], output)
        # print(out)
        name = prec + "_" + ls + "_" + lvl + "_Problem-" + prob
        save("Aufgabe10", name)


def main_Jac_LS():
    lvl = "3"
    prec = "Jacobi"
    ls = "LS"
    delete_old()
    manipulate_conf("m++conf", [("loadconf", "laplace.conf")])
    manipulate_conf("laplace.conf",
                    [("Problem", "Simple2D"),
                     ("Mesh", "UnitSquare"),
                     ("level", lvl),
                     ("Preconditioner", prec),
                     ("LinearSteps", "800"),
                     ("LinearSolver", ls),
                     ("LinearVerbose", "1")])
    output = run(1)
    # out = parse_mpp_output_allg([], output)
    # print(out)
    name = prec + "_" + ls + "_" + lvl
    save("Aufgabe10", name)


if __name__ == "__main__":
    '''
    main_GS_GMRES()
    main_Jac_GMRES()
    main_MG_GMRES()
    '''
    '''
    main_Jac_CG()
    main_MG_CG()
    main_SGS_CG()
    '''

    '''
    main_Jac_CG_2()
    main_Jac_CG_4()

    main_Jac_CG_probs()

    main_Jac_LS()
    '''
    main_Jac_CG_2()
    main_Jac_CG_4()
