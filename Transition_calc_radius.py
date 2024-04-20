 # Python Transition Rechner 

import math


n1 = "Transitions that taper down to zero degrees towards the ground." 
n2 = "Instructions / Description: "
n3 = "Program calculates radius from given height and maximum slope angle. The physical unit in the output corresponds to the unit of the height input."
empty = "    "
print (n1)
print (empty)
print (n2)
print (empty)
print (n3)
print (empty)




H = float(input("Height input:  "))
p = float(input("Maximum slope angle input in degrees:  "))
phi = p*math.pi/180
R = H*(1+math.cos(phi)/math.sin(phi))/math.sin(phi)**2


print (empty)

nachricht2 = "Result:" 
print (nachricht2)
print (empty)

print("Radius", R)

