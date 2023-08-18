def is_palindrome(numb):
    numb=int(input("enter number"))

    num_str = str(numb)
    return num_str == num_str[::-1]


def is_even_odd(numb):
    numb=int(input("enter number"))
    if numb % 2 == 0:
        return "Even"
    else:
        return "Odd"

while True:
   selection=int(input("1. Check if a number is palindrome \n"
                        " 2. Check if a number is even or odd\n"
                       "3.exit"))


    if selection== 1:
     is_palindrome(numb)

    elif selection == 2:
      is_even_odd(numb)


    elif selection == 3:
        exit

