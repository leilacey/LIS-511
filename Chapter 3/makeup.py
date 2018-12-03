# Assignment 3 Part B
makeup_list = []
prompt = "\nPlease enter the makeup you want:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	makeup = input(prompt)
	
	if makeup == 'quit' :
		break
	else:
		makeup_list.append(makeup)

print("This is the makeup you purchased:")
for makeup in makeup_list:
	print (makeup)

continue_purchase = input("Would you like to buy anything else? ")
if  continue_purchase == 'yes':
	while True:
		makeup = input(prompt)
		
		if makeup == 'quit' :
			break
		else:
			makeup_list.append(makeup)
			
print("This is the makeup you purchased: ")
for makeup in makeup_list:
	print (makeup)