"First the name of the square block is asked. Then it is checked whether the user has written the block name in the cprrect order."
"If the order is correct, it is checked whether the number is even or odd. In case of double, the letters are printed in white if b  f h if not black."
a = input("Enter a chess square identifier (e.g. e5) between a-g and 1-8: ")

letter = a[0]
number = int(a[1])

if type(letter) == int :
    print("please replace number with letter")
else :   
    if number % 2 == 0 and number < 9:
        if letter == "b" or letter == "d" or letter == "f" or letter == "h" :
            print(a , "is BLACK")
        elif letter == "a" or letter == "c" or letter == "e" or letter == "g" :
            print(a , "is WHITE")
        else :
            print(a , " is not proper")
    elif number < 8 :
        if letter == "a" or letter == "c" or letter == "e" or letter == "g" :
            print(a , "is WHITE")
        elif letter == "b" or letter == "d" or letter == "f" or letter == "h" :
            print(a , "is BLACK")
        else :
            print(a, "is not proper")
    else :
        print(a, "is not proper")

    
