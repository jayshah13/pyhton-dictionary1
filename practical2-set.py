#Create a new set
num_set = set([0, 1, 2, 3, 4, 5])
print("Original set elements:")
print(num_set)
print("\nRemove 0 from the said set:")
num_set.discard(4)  #discard method
print(num_set)
print("\nRemove 5 from the said set:")
num_set.remove(3)   #remove method
print(num_set)
print("\nRemove 2 from the said set:")
num_set.discard(5)
print(num_set)
print("\nRemove 7 from the said set:")
x=num_set.pop()    #pop method
print(x)
print(num_set)
