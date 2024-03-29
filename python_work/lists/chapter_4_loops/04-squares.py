# Adding items to Array
squares=[]
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

# Another way to write without having square variable
squares = []
for value in range(1,15):
	squares.append(value**2)
print(squares)

# Another way to write using "List Comprehension"
squares = [value**2 for value in range(1,16)]
print(squares)
