a = int(input("Please enter number of seconds: "))

seconds = a % 60
minute = (a // 60) % 60
hours = (a / 60 ) // 60

print(hours, minute, seconds)