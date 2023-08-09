def sum ():
    num1 = int(input("the first number"))
    num2 = int(input(" the second number"))
    print("The sum is =", num1 + num2)
    print("*************************")
def substract():
    num1 = int(input("the first number"))
    num2 = int(input(" the second number"))
    print("The Substract =", num1 - num2)
    print("*************************")
def multiply():
    num1 = int(input("the first number"))
    num2 = int(input(" the second number"))
    print("The Multiply is =", num1 * num2)
    print("*************************")
def devision():
    num1 = int(input("the first number"))
    num2 = int(input(" the second number"))
    print("The Devision is =", num1 / num2)
    print("*************************")
def triangle_area():
    base = int(input("enter the base triangle area"))
    length = int(input("enter the length triangle area"))
    print("The triangle area is = ",.5*base*length)
    print("*************************")
def circle_area():
    radius = int(input("enter the radius area"))
    print("The circle area is =", 3.14 * (radius ** 2))
    print("*************************")
def rectangle_area():
    length = int(input("enter the length rectangle area"))
    width = int(input("enter the width rectangle area"))
    print("The rectangle area is =", length * width)
    print("*************************")

while True:
     menu = int(input("1. Sum\n" 
         "2.Substract\n" 
         "3.Multiply\n" 
         "4.Devision\n" 
         "5.Calculate triangle area\n" 
         "6.Calculate circle area\n" 
         "7.Calculate rectangle area\n"
                     "8.Exit\n"))
     while True:
       if menu <=8 and menu >=1:
        break
       else:
        menu = int(input("Invalid input,Enter valid Selction "))
     if menu == 1:
        sum()
     elif menu == 2:
        substract()
     elif menu == 3:
       multiply()
     elif menu == 4:
       devision()
     elif menu == 5:
       triangle_area()
     elif menu == 6:
       circle_area()
     elif menu == 7:
       rectangle_area()
     elif menu == 8:
        break