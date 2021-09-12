income = int(input("Please enter your income: "))

if income <= 38000 :
    tax1 = income * 0.3
    print("corresponding income tax: ", tax1)
elif income > 38000 and income <= 50000 :
    tax2 = income * 0.35
    print("corresponding income tax: ", tax2)
else :
    tax3 = income * 0.4
    print("corresponding income tax: ", tax3)
