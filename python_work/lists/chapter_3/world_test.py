locations = ['Italy','France','London','Switzerland']
print(f"Original locations order {locations}")
print(f"Sort list with out altering the original list {sorted(locations)}")
print(f"Original locations order {locations}")
print(f"Sort list in reverse with out altering the original list {sorted(locations, reverse=True)}")
locations.reverse()
print(f"Chaging to reverse order in original list{locations}")
locations.sort()
print(f"Sorted locations list{locations}")