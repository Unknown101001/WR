import subprocess
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import re
from distutils.dir_util import copy_tree
import sys

kernels = 4
working_dir = "mpp/build"


def run():
    '''
    runs M++ in working dir mpp/build with 4 kernels
    :return: output
    '''
    '''
    stdout = subprocess.run(['mpirun', '-np', str(kernels), 'M++'], stdout=subprocess.PIPE,
                            cwd=working_dir).stdout.decode('utf-8')
    return stdout.split('\n')
    '''
    output = []
    process = subprocess.Popen('mpirun -np '+ str(kernels)+' M++', stdout=subprocess.PIPE,
                               cwd=working_dir,shell = True)    #.stdout.decode('utf-8')
    for line in iter(process.stdout.readline,b''):
        l = line.decode('utf-8')
        sys.stdout.write(l)
        output.append(l.rstrip())

    return output



def manipulate_conf(confdatei, tupelliste):
    '''
    :param confdatei:
    :param tupelliste:
    :return:
    '''
    with open("mpp/Praktikum/conf/" + confdatei) as file:
        conf = file.readlines()
        # print(conf)
        for tupel in tupelliste:
            key = tupel[0]
            value = tupel[1]
            search = key + " ="  # looks behind
            if any((search in s and s.split(search)[0] == "") for s in conf):
                # print("YES")
                index = conf.index(next((s for s in conf if key in s), None))
                conf[index] = key + " = " + value + ";\n"
            else:
                # print("NO")
                new = key + " = " + value + ";\n"
                conf.append(new)
        # print(conf)
        with open("mpp/Praktikum/conf/" + confdatei, 'w') as file:
            file.writelines([item for item in conf])


def delete_old():
    '''
    deletes old vtk and log folders
    :return:
    '''
    folder = 'mpp/build/data/vtk'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path) #subdirs
        except Exception as e:
            print(e)
    folder = 'mpp/build/log'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path) #subdirs
        except Exception as e:
            print(e)


def check_dirs(name, aufgabe):
    '''
    checks target folder param is (/aufgabe/name)
    :param name:
    :param aufgabe:
    :return:
    '''
    if aufgabe is not None:
        try:
            os.mkdir(aufgabe)
            # raise FileNotFoundError
        except OSError as e:
            pass
        try:
            os.mkdir(aufgabe + "/" + name)
            # raise FileNotFoundError
        except OSError as e:
            pass
    else:
        try:
            os.mkdir(name)
            # raise FileNotFoundError
        except OSError as e:
            pass


def save(aufgabe=None, name="Neu"):
    '''
    saves content in (aufgabe)/name
    :param name: optional default is "Neu"
    :param aufgabe: optional
    :return:
    '''
    check_dirs(name, aufgabe)
    if aufgabe is None:
        toDirectory = name
    else:
        toDirectory = aufgabe + "/" + name
    fromDirectory1 = "mpp/build/data"
    fromDirectory2 = "mpp/build/log"
    copy_tree(fromDirectory1, toDirectory)
    copy_tree(fromDirectory2, toDirectory)


def parse_mpp_output_allg(paramlist, output=None , logfile = "mpp/build/log/log"):
    '''
    :param paramlist:
    :param output:
    :return:list of list of outputvalues
    '''
    out = []
    if output is None:
        #logfile = "mpp/build/log/log"
        with open(logfile) as file:
            lines = file.readlines()
    else:
        lines = output
    for param in paramlist:
        out.append([])
        for line in lines:
            if "Step" in line and not "default" in line and not "reading" in line:
                regex = r"[+-]?[0-9]+[.]?[0-9]*[eE]?[+-]?[0-9]*"
                if param in line:
                    tmp = line.split(param)[1]
                    value = float(re.findall(regex, tmp)[0])
                    # print(value)
                else:
                    value = 0
                out[paramlist.index(param)].append(value)
    return out

def parse_mpp_output_single_inform(paramlist, output= None, logfile = "mpp/build/log/log"):
    out = []
    if output is None:
        # logfile = "mpp/build/log/log"
        with open(logfile) as file:
            lines = file.readlines()
    else:
        lines = output
    for param in paramlist:
        out.append([])
        for line in lines:
            regex = r"[+-]?[0-9]+[.]?[0-9]*[eE]?[+-]?[0-9]*"
            if param in line:
                tmp = line.split(param)[1]
                try:
                    value = float(re.findall(regex, tmp)[0])
                except:
                    continue
            else:
                value = 0
            out[paramlist.index(param)].append(value)
    return out