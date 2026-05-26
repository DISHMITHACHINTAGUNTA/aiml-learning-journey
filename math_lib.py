import math

# area od circle (pi*r**2)
rad = float(input("Please enter the radius of the circle: "))
area=math.pi*pow(rad,2)
print("area of the circle:",area,"cm^2")

# circumference od circle :(2*pi*r)
circumference=2*math.pi*rad
print("area of the circumference:",circumference,"cm")

# hypotenuse of right angle triangle

hig=float(input("enter height of the triangle: "))
wid=float(input("enter width of the triangle: "))
hyp=math.sqrt(pow(hig,2)+pow(wid,2))
print(" hypotenuse of the triangle:",hyp,"cm")


