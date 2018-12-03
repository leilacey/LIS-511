# 3-4 Guest List
dinner_guests = ['Kurt Cobain', 'Bill Gates', 'Eddie Veddar']
for guest in dinner_guests
	print ("Would you like to have dinner with me " + guest + "?")
	
# 3-5 Changing Guest List
not_coming = "Bill Gates"
dinner_guests.insert(1, "Dave Grohl")
dinner_guests.remove(not_coming)
for guest in dinner_guests
	print ("Would you like to have dinner with me " + guest + "?")
print (not_coming)