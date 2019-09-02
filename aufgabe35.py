import numpy as np
import matplotlib.pyplot as plt
from mppstart import *
import csv


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
                                 ("Preconditioner", "Multigrid"), ("LinearSteps", "2000")])
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
                         ("Preconditioner", "Multigrid"), ("LinearSteps", "2000")])
        output = run()
        # out = parse_mpp_output_allg(["Step","Flux Error","Flux Loss","Problem size"], output)
        # out2 = parse_mpp_output_single_inform(["Problem size"])+
        name = "DG2_lvl=" + lvl
        save("Aufgabe35", name)

    # 3b)
    for penalty in ["0", "1", "5", "10", "25", "50", "100"]:
        delete_old()
        manipulate_conf("m++conf", [("loadconf", "dglaplace.conf")])
        manipulate_conf("dglaplace.conf",
                        [("Model", "DGLaplace"), ("Problem", "Simple2D"), ("Mesh", "Square500"),
                         ("deg", "2"), ("level", "3"), ("sign", "1"), ("penalty", penalty),
                         ("Preconditioner", "Multigrid"),("LinearSteps", "2000")])
        output = run()
        # out = parse_mpp_output_allg(["Step","Flux Error","Flux Loss","Problem size"], output)
        # out2 = parse_mpp_output_single_inform(["Problem size"])+
        name = "DG3_penalty=" + penalty
        save("Aufgabe35", name)


def read_values():
    saveload = []
    for lvl in ["0", "1", "2", "3"]:
        for disc in ["linear", "serendipity"]:
            name = "FEM_lvl=" + lvl + "_disc=" + disc
            logfile = "Aufgabe35/" + name + "/log"
            out = parse_mpp_output_single_inform(["Problem size", "Inflow", "Outflow", "Flux Error", "Flux Loss"],
                                                 logfile=logfile)
            time, einheit = get_time(logfile=logfile)
            liste = [name, out[0][0], out[1][0], out[2][0], out[3][0], out[4][0], time, einheit]
            # print(liste)
            saveload.append(liste)
    for lvl in ["0", "1", "2", "3"]:
        for konf in ["sym", "nonsym"]:
            name = "DG_lvl=" + lvl + "_konf=" + konf
            logfile = "Aufgabe35/" + name + "/log"
            out = parse_mpp_output_single_inform(["Problem size", "Inflow", "Outflow", "Flux Error", "Flux Loss"],
                                                 logfile=logfile)
            time, einheit = get_time(logfile=logfile)
            liste = [name, out[0][0], out[1][0], out[2][0], out[3][0], out[4][0], time, einheit]
            # print(liste)
            saveload.append(liste)
    for lvl in ["0", "1", "2", "3"]:
        name = "DG2_lvl=" + lvl
        logfile = "Aufgabe35/" + name + "/log"
        out = parse_mpp_output_single_inform(["Problem size", "Inflow", "Outflow", "Flux Error", "Flux Loss"],
                                             logfile=logfile)
        time, einheit = get_time(logfile=logfile)
        liste = [name, out[0][0], out[1][0], out[2][0], out[3][0], out[4][0], time, einheit]
        # print(liste)
        saveload.append(liste)
    for penalty in ["0", "1", "5", "10", "25", "50", "100"]:
        name = "DG3_penalty=" + penalty
        logfile = "Aufgabe35/" + name + "/log"
        out = parse_mpp_output_single_inform(["Problem size", "Inflow", "Outflow", "Flux Error", "Flux Loss"],
                                             logfile=logfile)
        time, einheit = get_time(logfile=logfile)
        liste = [name, out[0][0], out[1][0], out[2][0], out[3][0], out[4][0], time, einheit]
        # print(liste)
        saveload.append(liste)

    return saveload


def write_to_csv(saveload):
    outputfile = "Aufgabe35/data.csv"
    with open(outputfile, 'w', newline='', encoding='utf-8')as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([a[0] for a in saveload])  # names
        writer.writerow([int(a[1]) for a in saveload])  # Problem Size
        writer.writerow([float(a[2]) for a in saveload])  # Inflow
        writer.writerow([float(a[3]) for a in saveload])  # Outflow
        writer.writerow([float(a[4]) for a in saveload])  # Flux Error
        writer.writerow([float(a[5]) for a in saveload])  # Flux Loss
        writer.writerow([a[6] for a in saveload])  # time
        writer.writerow([a[7] for a in saveload])  # einheit


def testit():
    delete_old()
    manipulate_conf("m++conf", [("loadconf", "laplace.conf")])
    manipulate_conf("laplace.conf",
                    [("Model", "Laplace"), ("Problem", "Simple2D"), ("Mesh", "UnitSquare2Triangles"),
                     ("Discretization", "linear"), ("level", "4")])
    output = run()
    # out = parse_mpp_output_allg(["Step","Flux Error","Flux Loss","Problem size"], output)
    # out2 = parse_mpp_output_single_inform(["Problem size"])+
    name = "test"
    save("Aufgabe35", name)


def aufgabe38():
    delete_old()
    manipulate_conf("m++conf", [("loadconf", "dgreaction.conf")])
    manipulate_conf("dgreaction.conf",
                    [("HybridProblem", "HybridReaction"), ("T", "1.6"), ("dt", "0.001"), ("Reaction", "0"),
                     ("Diffusion", "0.000001"),("Model","HybridDGReaction")])
    output = run()
    save("Aufgabe38")
    out = parse_mpp_output_allg(["Step", "Mass", "Outflow"],output=output)
    time = [0.001 * a for a in out[0]]
    fig = plt.figure(0)
    plt.plot(time, out[1], label="Masse")
    plt.grid()
    plt.legend()
    plt.xlabel("Zeit")
    plt.ylabel("Masse")
    plt.grid(True)
    plt.savefig("Aufgabe38/plotmass.png")

    fig = plt.figure(1)
    plt.plot(time, out[2], label="Outflow")
    plt.grid()
    plt.legend()
    plt.xlabel("Zeit")
    plt.ylabel("Outflow")
    plt.grid(True)
    plt.savefig("Aufgabe38/plotoutflow.png")

def a38_outflowrate():
    out = parse_mpp_output_allg(["Step", "Mass", "OutFlowRate"]) #logfile="Aufgabe38/Neu/log"
    time = [0.001 * a for a in out[0]]
    fig = plt.figure(1)
    plt.plot(time, out[2], label="OutFlowRate")
    plt.grid()
    plt.legend()
    plt.xlabel("Zeit")
    plt.ylabel("OutFlowRate")
    plt.grid(True)
    plt.savefig("Aufgabe38/plotoutflowrate.png")


if __name__ == "__main__":
    main()
    saveload = read_values()
    write_to_csv(saveload)
    #testit()
    #a38_outflowrate()
