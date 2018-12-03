# 4-3 Counting to Twenty
numbers = list(range(1,21))
for number in numbers:
	print(number)

#4-4 One Million
numbers = list(range(1, 1000001))
#for number in numbers:
	#print(number)

# 4-5 Summing a Million
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4-6 Odd Numbers
numbers = list(range(1, 20, 2))
for number in numbers:
	print(number)
	
# 4-7 Threes
numbers = list(range(3, 31, 3))
for number in numbers:
	print(number)
	
#4-8 Cubes
cubes = []
for value in range(1,11):
	cubes.append(value**3)
for number in cubes:
	print(number)

#4-9 Cube Comprehension
cubes = list(value **3 for value in range(1,11))
for number in cubes:
	print(number)