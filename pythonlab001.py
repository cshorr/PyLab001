#Chris Shortt Cis-12
import math

#The area of a circle with radius 5
radius = 5
area_circle = (math.pi * radius **2)
print(f"Area of a Circle, Ta-dah",  area_circle)

# Volume of a sphere with radius 3
radius_sphere =3
volume_sphere = 4/3 * math.pi * radius_sphere ** 3
print(f"Volume of a Sphere, WHA-LAH", volume_sphere)

#The hypotenuse of a right-angled triangle with sides 3 and 4.
side_a =3
side_b = 4
hypotenuse = math.sqrt(side_a ** 2) + (side_b ** 2)
print(f"Hypotenuse of a TRIANGLE, HUZZAH! ", hypotenuse)
#print name and len(gth)
full_name =  "Chris Shortt"
len(full_name)
print(len(full_name))
# name upper and lower
first_name = "Chris"
last_name = 'Shortt'
full_name =  first_name + ' ' + last_name
print(full_name,full_name.upper(),full_name.lower())
#3 variable of data types
#Create variables to store your age, height (in feet), and weight (in pounds).
#Print the data type of each variable using the type() function.
#Calculate your Body Mass Index (BMI) using the formula
age = 49
weight = 300
height = 6.0
inches = height * 12
bmi = (weight / inches**2) * 703
print(f"Your BMI is {bmi}")