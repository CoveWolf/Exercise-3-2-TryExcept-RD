import locale

# Exercise 2: Rewrite your pay program using try and except so that your program handles
# non-numeric input gracefully by printing a message and exiting the program. The 
# following shows two executions of the program:

#set locale to system locale
locale.setlocale(locale.LC_ALL, '')

#user input for hours worked
hours = input("Enter Hours Worked: ")
try:
  float(hours)
except:  
  print("Error, please enter a number by using a digit. (Program Stopped)")
  exit()

#user input for hourly rate
payperhour = input("Enter Pay per Hour: ")
try:
  float(payperhour)
except:  
  print("Error, please enter a number by using a digit. (Program Stopped)")
  exit()

#calculate payperhour * overtime
overtime = 1.5
payperhourovt = float(payperhour) * overtime

#logic to determine if overtime needs to be calculated or not
if float(hours) < 41:
  grosspay = float(hours) * float(payperhour)
else:
  grosspay = (float(hours) - (40.0)) * float(payperhour) * (overtime) + (40.0) * float(payperhour)
print("Gross Pay: " + locale.currency((grosspay)))


