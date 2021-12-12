# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Tristian "Ty" Ssnders
# Section:        552
# Assignment:     Lab 1A
# Date:           9/2/2021
from math import *
print ("tristian 'ty' sanders, 331005076, 552")
print ("i've learned python twice and have managed to forget everything")


#Ohm's Law
Resistance = 20
Current = 5
OhmsLaw = (Resistance*Current)
print (OhmsLaw)
    
#Kinetic Energy
Mass = 100
Velocity = 21
KineticEnergy = ((Mass*Velocity**2)/2)
print (KineticEnergy)

#Reynolds number
RVelocity = 100
KViscosity = 1.2
LDim = 2.5
ReynoldsNumber = ((RVelocity*LDim)/KViscosity)
print (ReynoldsNumber)

#Stefan-Boltzmann Law
Temp = 2200
SBConstant = (5.67*10**-8)
StefanBoltzmannLaw = (SBConstant*(2200**4))
print (StefanBoltzmannLaw)

#Arps Equation
Time = 20
Qi = 100
Di = 2
HBconstant = 0.8
ArpsEquation = (Qi/((1+HBconstant*Di*Time)**(1/HBconstant)))
print (ArpsEquation)

#M/M/1 Queue
Ar = 20
Sr = 35
MM1Queue = (Ar/Sr)
print (MM1Queue)

#Mohr-Coulomb Failure Criterion
Ns = 20
Coh = 2
Fi = 35
MohrCoulomb = (Ns*tan(Fi)+Coh)
print (MohrCoulomb)

#Bragg's law
Wl = (7.5*10**-7)
d = (1*10**-6)
n = 1
BraggsLaw = (asin((n*Wl)/(2*d)))
print (BraggsLaw)
