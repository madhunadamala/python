# Page No 61: Slicing List
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])

# If you omit the first index in a slice, Python automatically starts from "0"
print(players[:4])

# Print items from the 3rd(Index 2) item to last item
print(players[2:])

# Negative index to retun last 3 elelments
print(players[-3:])

# Third item to skip the items in the range (1 Default)
print(players[:4:2])