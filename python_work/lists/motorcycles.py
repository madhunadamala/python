# Example for modifying the existing element
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Example for adding new element
motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

# Example for adding elements to an empty array
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Example for Inserting value at required position
motorcycles = ['honda','yamaha','suzuki']

motorcycles.insert(0,'ducati')
print(motorcycles)

# Removing an item using the DEL Statement
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print (motorcycles)

# Removing an item using the POP Statement
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#How pop is userful
motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

#Popping Items from nay position in a List
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#Remove an item by value
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print (motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")