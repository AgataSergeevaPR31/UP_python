import math

#задание1
a = [1, 1, 2, 3, 5, 8, 10, 12, 34, 38, 40, 41, 46, 50, 55, 89]
for i in a:
    if i < 15:
        print(i)

#задание2
num = input("\nchislo: ")
number = int(num)
if number > 0: 
    print("+")
elif number < 0: 
    print("-")
else:
    print("0")
    
#задание3
z=0
x = int(input("\na = "))
y = int(input("b = "))
print("1. Plus;\n2. Minus;\n3. Delenie;\n4. Umnojenie")
g = input("Vash vibor: ")
if g == "1":
    z = x+y
elif g == "2":
    z = x-y
elif g =="3":
    z = x/y
else:
      z = x*y
print(round(z,2), "\n" )

#задание4
for i in range(10):
  print(i+1)

#задание5
x1 = 0
x2 = 0
a = int(input("\na = "))
b = int(input("b = "))
c = int(input("c = "))
print(a, "x^2 + ", b, "x + ", c, " = 0")
d = b * b - 4 * a * c 

if d < 0: 
    print("Корней нет")
elif d == 0:
    x1 = (-b) / (2 * a)
    print("x1 = x2 =", round(x1,2))
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 =", round(x1, 2), "\nx2 =", round(x2, 2))