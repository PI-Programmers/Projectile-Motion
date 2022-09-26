import math
from math import sin, cos, tan, radians, pi

#Initilization of Variables
u=float(input('Enter The Initial Speed : ')) #m/s #Velocity
alpha=int(input('Enter The Angle Of Projectile : '))#Degrees #Angle made by projectile with horizontal
g=9.81 #m/s #Acceleration due to gravity

#Calculation

#Horizontal Range
R=u**2*sin(2*alpha*pi*180**-1)*g**-1 #m

#MAx height attained
h_max=u**2*sin(alpha*pi*180**-1)*g**-1 #m

#Time of flight
T=2*u*sin(alpha*pi*180**-1)*g**-1 #s

#Result
print("Horizontal Range is",round(R,2),"m")
print("MAX Height attained is",round(h_max,2),"m")
print("Time of Flight is",round(T,2),"s")   