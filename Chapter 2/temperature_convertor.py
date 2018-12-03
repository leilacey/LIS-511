#Assignment 2 Task 5
# This Program converts degrees Fahrenheit to degrees Celsius and prints the result

fahrenheit_temp = float(input("Enter the temperatures in degrees Fahrenheit? "))
celsius_temp = round(((fahrenheit_temp - 32) * (5/9)), 2)
print("")
print ("The temperature " + str(fahrenheit_temp) + " degrees Fahrenheit is " + str(celsius_temp) + " degrees Celsius.")