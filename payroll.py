'''
Program: payroll.py
Chapter 2 practice project (page 63 question 10) 12/22/23

Application that asks for inputs on hourly wage, regular hours worked and overtime hours worked. It will output the total weekly pay.
'''

#Input phase
wage = float(input("Please enter your hourly wage: "))
regHours = float(input("How many regular hours have you worked this week?: "))

otHours = float(input("Enter any overtime hours worked, enter 0 for none: "))

# Processing phase
totalPay = (regHours * wage) + (otHours * wage * 1.5)

# Output phase
#print("\nThe total weekly pay is $", totalPay)

print("\nThe total weekly pay is $", str(round(totalPay, 2)))