friends=['Pratap','Malli','Hari']
print (f"Hi {friends[0]} How are you doing?")
print (f"Hi {friends[-1]} How are you doing?")
print (f"Hi {friends[1]} How are you doing?")
friends.remove("Pratap")
print(friends)
friends.insert(1,'Reddy')
print(friends)
print(f"Hi {friends[1]} where are you?")
friends.append("Aswarth")
print(friends)

# Removing 2 friednds
friend_removed = friends.pop()
print(f"{friend_removed} Removing due to no seats")
print(friends)
del friends[0]
print(friends)