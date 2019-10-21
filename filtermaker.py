import os
cwd = os.getcwd()
print(cwd)
import math
import random
name = "Downloads\AppChallenge2019-master\AppChallenge2019-master\\filters.txt"
f = open(name, "w")

#getting inputs
#lcount = input("How many layers? ")
"""
for layer in range(lcount-1):
    print("Layer " + str(layer))
    filters = input("How many filters? ")
    w, h = input("width, height? 'X Y' ").split(" ")
    for filter in range(filters):
        
        for y in range(h):
            filt = ""
            for x in range(w):
                filt.append(math.randint(0, 30) + " ")
            f.write(filt)
            """
layers = input("How many layers? ")
filters = input("How many filters per layer? ")
w = int(input("filter width? "))
h = int(input("filter height? "))
minimum = 20
maximum = 40
rounding=1000.00
f.write(str(layers) + "\n")
for layer in range(layers):
    f.write("Layer " + str(layer+1) + "\n")
    f.write(str(filters) + "\n")
    for filter in range(filters):
        f.write( str(w) + " " + str(h) + "\n")
        for y in range(h):
            filt = ""
            for x in range(w):
                val = ( (random.random()*(maximum-minimum))+abs(minimum) )
                valFixed = float(int(rounding * val)/rounding)
                filt += ((str(valFixed) + " "))
            filt +="\n"
            print(filt)
            f.write(filt)


f.close()


#range of inputs = ( math.random(max + math.abs(min)) - math.abs(min) )
#rounding limit of float = int(10eX * val)/10eX