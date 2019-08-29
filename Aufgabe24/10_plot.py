import numpy as np
import matplotlib.pyplot as plt




def read_log():
    log_file = "Level3Deg0/log"
    with open(log_file) as file:
        content = file.readlines();
    return content



T = []
Outflow = []
xString = "Step("
yString = "OutFlowRate(u) = " 
#line = "Step(92), t(0.46): Energy(u) = 0.00126323 Mass(u) = 0.0234278 InFlowRate(u) = -1.14819e-07 OutFlowRate(u) = 0.000410091\n"
for line in read_log():
    #print(line)
    if yString in line:
        line.strip("\n")
        t = line[line.index(xString) + len(xString):line.index(")")]
        outflow = line[line.index(yString) + len(yString):]
        T.append(int(t))
        Outflow.append(float(outflow))
    elif xString in line:
        line.strip("\n")
        t = line[line.index(xString) + len(xString):line.index(")")]
        T.append(int(t))
        Outflow.append(0)
        
#print(T)
#print(Outflow)
print(len(T))
print(len(Outflow))

plt.plot(T,Outflow)
plt.xlabel('Zeit')
plt.ylabel('OutFlowRate')
#plt.scatter(T,Outflow)
plt.grid()
plt.show()

