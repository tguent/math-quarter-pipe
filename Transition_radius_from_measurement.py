 # Python Transition Radius Rechner 

import math


n1 = "Transitions that taper down to zero degrees towards the ground." 
n2 = "Instructions / Description: "
n3 = "The program calculates the radius of a quarter pipe from the length of a secant and distance of the secant's center to the transition."
empty = "    "
print (n1)
print (empty)
print (n2)
print (empty)
print (n3)
print (empty)




L = float(input("Input length c of secant at any location within the transition     "))
print (empty)
a = float(input("Input distance a of the secant's center to the transition (same physical unit)  "))

R = a/2+L**2/(8*a)

print (empty)
#Radius ausgeben
print("The radius, measured in the same physical unit as the input values, is:    ", R)
print (empty)
#Programmpause
input("Press enter to calculate measurement errors.")
print (empty)
#Fehlerberechnung für den Radius

print("Input of measurement errors in the same physical unit as above")
print (empty)
DeltaL = float(input("Input error of length c of secant  "))
print (empty)
Deltaa = float(input("Input error of distance a of the secant's center to the transition "))
print (empty)
dRdL = L/(4*a)
dRda = 1/2-L**2/(8*a**2)
DeltaR = math.sqrt((dRda*Deltaa)**2+(dRdL*DeltaL)**2)

#Messfehler Radius ausgeben
print("Propagation of error for the radius is:    ", DeltaR)
