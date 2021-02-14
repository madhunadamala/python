# SORT function sorts the data permanently
cars =['bmw','audi','toyota','subaru','Audi','BMW']
cars.sort()
print(cars)
cars.sort(reverse = True)
print(cars)

# Sorting a List Temporarily with sorted() Function
cars =['bmw','audi','toyota','subaru','Audi','BMW']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the sorted list in reverse:")
print(sorted(cars, reverse=True))

print("Here is the original list:")
print(cars)

# Original list
cars =['bmw','audi','toyota','subaru','Audi','BMW']
print("Here is the original list:")
print(cars)

# Reverse original cars list
print("Sorted on cars list")
cars.reverse()
print (cars)

print (f"Length of car is {len(cars)}")