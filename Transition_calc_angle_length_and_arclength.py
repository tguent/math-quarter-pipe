 # Python Transition Rechner 

import math

n1 = "Transitions that taper down to zero degrees towards the ground." 
n2 = "Instructions / Description: "
n3 = "Program calculates length, arclength and maximum slope angle from given height H and radius R. The physical unit in the output corresponds to the unit in the input. Height and radius must be entered in the same physical unit."
empty = "    "
print (n1)
print (empty)
print (n2)
print (empty)
print (n3)
print (empty)

H = float(input("Input height of quater pipe:   "))
print (empty)
R = float(input("Input radius of quater pipe:   "))
T = math.sqrt(2*R*H-H*H)
Larc = R*math.asin(T/R)
phi = 360*Larc/(2*math.pi*R)
n4 = "Results:" 
print (empty)
print (n4)
print (empty)

#Print results

print("Depth or length of the transition:", T)
print (empty)


print("arclength of the transition:", Larc)
print (empty)
print("maximum slope angle at highest point", phi)

