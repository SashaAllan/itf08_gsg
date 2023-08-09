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
        num1 = int(input("the first number"))
        num2 = int(input(" the second number"))
        print("The sum is =",x+y )
        print("*************************")
     elif menu == 2:
        num1 = int(input("the first number"))
        num2 = int(input(" the second number"))
        print("The Substract =", x-y)
        print("*************************")

     elif menu == 3:
        num1 = int(input("the first number"))
        num2 = int(input(" the second number"))
        print("The Multiply is =",x*y)
        print("*************************")

     elif menu == 4:
        num1 = int(input("the first number"))
        num2 = int(input(" the second number"))
        print("The Devision is =",x/y)
        print("*************************")

     elif menu == 5:
        base = int(input("enter the base triangle area"))
        length = int(input("enter the length triangle area"))
        print("The triangle area is = ",.5*base*length)
        print("*************************")

     elif menu == 6:
        radius = int(input("enter the radius area"))
        print("The circle area is =",3.14*(radius**2))
        print("*************************")

     elif menu == 7:
        length = int(input("enter the length rectangle area"))
        width = int(input("enter the width rectangle area"))
        print("The rectangle area is =",length*width)
        print("*************************")

     elif menu == 8:
        break