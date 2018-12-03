#Assignment 2 Task 4 Part B

hours = float(input('Enter hours worked: '))
rate = float(input('Enter a pay rate without $: '))
print(" ")

gross_total = round (hours * rate,2)
print("You're total pay for " + str(hours) + " hours worked at a rate of " + str(rate) + " dollars per hour is $" + str(gross_total))