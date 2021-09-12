"First, the user was prompted to enter the payment and price to determine the change "
"It is checked step by step whether there are bills and coins. If there is an bills or coins after control, this amount is deducted from change."
payment = int(input("please enter your payment: "))
price = float(input("Please enter price: "))
change = round(payment - price)
print(change)
a = change // 1000
remainder_1 = change - (1000 * a)

b  = remainder_1 // 500
remainder_2 = remainder_1 - (500 * b)

c = remainder_2 // 200
remainder_3 = remainder_2 - (200 * c)

d = remainder_3 // 100
remainder_4 = remainder_3 - (100 * d)

e = remainder_4 // 50
remainder_5 = remainder_4 - (50 * e)

f = remainder_5 // 20
remainder_6 = remainder_5 - (20 * f)

g = remainder_6 // 10
remainder_7 = remainder_6 - (10 * g)

h = remainder_7 // 5
remainder_8 = remainder_7 - (5 * h)

i = remainder_8 // 2
remainder_9 = remainder_8 - (2 * i)

j = remainder_9 // 1

print(
    "1000kr bills: " , a ,  "\n" ,
    " 500kr bills: " , b ,  "\n" , 
    " 200kr bills: " , c ,  "\n" ,
    " 100kr bills: " , d ,  "\n" , 
    "  50kr bills: " , e ,  "\n" , 
    "  20kr bills: " , f ,  "\n" , 
    "  10kr bills: " , g ,  "\n" , 
    "   5kr bills: " , h ,  "\n" ,
    "   2kr bills: " , i ,  "\n" ,
    "   1kr bills: " , j )
