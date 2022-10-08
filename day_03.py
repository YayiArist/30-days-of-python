
# Day 3: 30 Days of python programming

# Declare your age as integer variable
age = 32

# Declare your height as a float variable
height = 1.62

# complex number
store = (3+5j)

# 5.The user to enter side a, side b, and side c of the triangle

""" a_side = float(input("Insert side a "))
b_side = float(input("Insert side b "))
c_side = float(input("Insert side c "))
perimeter_triangle = a_side + b_side + c_side
print(perimeter_triangle) """

# 6.Get length and width of a rectangle using prompt
""" length = int(input("Insert length "))
width = int(input("Insert width "))
area = length * width
perimeter = 2 * (length + width)
print(area,perimeter) """

# 7.Get radius of a circle using prompt.
""" pi = 3.14
r= int(input("Insert radius: "))
area = pi * r * r
circumference = 2 * pi * r
print(area,circumference) """

# 8.Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = int()
m = int(input("Insert m"))
y = (m*x-2)
print(m)

# 9.Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = int(input("x1 ")), int(input("y1 "))
x2, y2 = int(input("x2 ")), int(input("y2 "))
y = y2 -y1
x = x2-x1
slope = y/x

print(slope)
# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True