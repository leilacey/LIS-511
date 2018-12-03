# 3-4 Guest List
dinner_guests = ['Kurt Cobain', 'Bill Gates', 'Eddie Veddar']
for guest in dinner_guests:
	print ("Would you like to have dinner with me " + guest + "?")
print('\n')

# 3-5 Changing Guest List
not_coming = "Bill Gates"
dinner_guests.insert(1, "Dave Grohl")
dinner_guests.remove(not_coming)
for guest in dinner_guests:
	print ("Would you like to have dinner with me " + guest + "?")
print (not_coming + '\n')

#3-6 More Guests
dinner_guests.insert(0, 'Brendan Urie')
dinner_guests.insert(2, 'Patrick Stump')
dinner_guests.append('Tim McIlrath')
for guest in dinner_guests:
	print ("Would you like to have dinner with me " + guest + "?")
print("I found a bigger table \n")

#3-7 Shrinking Guest List
print("Sorry, I can only invite two people now.")
while (len(dinner_guests) > 2):
	uninvited_guest = dinner_guests.pop()
	print("Sorry, you have been uninvited " + uninvited_guest + ".")
index = 0
print ("You are still invited " + dinner_guests[0] + ".")
print ("You are still invited " + dinner_guests[1] + ".")
del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)

#3-9 Dinner Guests
dinner_guests = ['Kurt Cobain', 'Bill Gates', 'Eddie Veddar']
len(dinner_guests)