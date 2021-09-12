a = int(input("Please enter first integer: "))
b = int(input("Please enter second integer: "))
c = int(input("Please enter third integer: "))

if a > b and a > c :
    if b > a :
        print(a, b, c)
    else :
        print(a, c, b)

elif b > a and b > c :
    if a > c :
        print(b, a, c)
    else :
        print (b, c, a)

else :
    if a > b :
        print(c, a, b)
    else : 
        print(c, b, a)
