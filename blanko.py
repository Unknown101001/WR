import numpy as np
import matplotlib.pyplot as plt
from mppstart import *

def main():
    delete_old()
    manipulate_conf("m++conf", [()])
    manipulate_conf(None,
                    [(), ()])
    output = run()
    out = parse_mpp_output_allg([], output)
    print(out)
    name = ""
    save(None, name)