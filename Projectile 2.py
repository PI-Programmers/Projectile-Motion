import math
from math import sin, cos, tan, radians, pi
import numpy as np

#Initilization of Variables
#R=4*h_max

#Calculation

#Equation ofhorizontal Range is
#R=u**2*sin(2*alpha)*g**-1   .........1

#Equation of  MAx height 
#h_max=u**2*sin(alpha)**2*(2*g)**-1    .........2

#After simplifying both equations,we get
alpha=np.arctan(1)*(pi**-1*180)

#Result
print("Angle of projections is",round(alpha,2),"degrees")