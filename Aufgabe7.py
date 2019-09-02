import numpy as np
import matplotlib.pyplot as plt
from mppstart import *
import csv

def write_to_csv(saveload,outputfile):

    with open(outputfile, 'w', newline='', encoding='utf-8')as csvfile:
        writer = csv.writer(csvfile, delimiter=';')

        writer.writerow([float(a[1]) for a in saveload])  # Flux Error
        writer.writerow([float(a[2]) for a in saveload])  # Flux Loss


def main_aufgabe7():

    for prob in ["Kellogg"]:
        outputfile = "Aufgabe7/data_"+prob+".csv"
        saveload = []
        for lvl in ["3","4","5","6","7"]:
            delete_old()
            manipulate_conf("m++conf", [("loadconf","laplace.conf")])
            if prob == "Divergent":
                manipulate_conf("laplace.conf",
                                [("Problem",prob), ("Mesh","UnitSquare"),("level",lvl)])
            else:
                manipulate_conf("laplace.conf",
                                [("Problem", prob), ("Mesh", "Square-1x1"), ("level", lvl)])
            output = run()
            out = parse_mpp_output_single_inform(["Flux Error", "Flux Loss"],
                                                 output)
            name = prob + "_lvl" + lvl
            liste = [name, out[0][0], out[1][0]]
            # print(liste)
            saveload.append(liste)


            save("Aufgabe7", name)
        write_to_csv(saveload,outputfile)




if __name__ == "__main__":
    main_aufgabe7()