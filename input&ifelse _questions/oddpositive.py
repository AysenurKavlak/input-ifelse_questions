import random
a = random.randint(-10, 10)

print("The generated number is: ", a)

if a < 0 : 
    print(a, " is odd and negative")

elif a == 0 :
    print(a, " is even and neither negative nor positive")

else :
    print(a, " is positive")