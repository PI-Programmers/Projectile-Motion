

import math  # for sin, cos, and other math functions


# collect information from user
angle = float(input('Angle: '))
print("     ")  # Blank Space
velocity = float(input('Velocity: '))
print("     ")  # Blank Space
gravity = input('Gravity (Enter To Take 9.8 By Default ) : ')
print("     ")  # Blank Space

# handle if user wants earths gravity by inputing nothing
if gravity.strip() == '':
    gravity = -9.8
else:
    gravity = float(gravity)

# calculate veloY(not an official term)
# velocity * sin(angle)

# calculate sin(angle)
# convert angle to radians because python uses radians instead of degrees
veloY = math.sin(math.radians(angle))
veloY = veloY * velocity

# calculate Vx(the object rising) and (Vy the object falling)
Vf = veloY * -1
Vx = veloY
Vy = Vf - Vx  # this number is important later for calculating deltaT
print('Velocity Of Object Rising : ', Vx)
print("     ")  # Blank Space
print('Velocity Of Object Falling : ', Vy)

# calculate deltaT or the time spent in the air
deltaT = Vy / gravity
print("     ")  # Blank Space
print('Time Spent In The Air : ', deltaT)  # bold output

# Calculate adj which is used for distance
# again convert to radians bc python uses them
adj = velocity * math.cos(math.radians(angle))

distance = adj * deltaT  # finally calculate distance
print("     ")  # Blank Space
print('Distance ( Range ) : ', distance)  # bold output
print("     ")  # Blank Space

message = input("Leave The Message : ")

