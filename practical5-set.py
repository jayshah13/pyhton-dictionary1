list1=[1,2,"ABC","xyz"]
tuple1=(3,4,"ABC","xyz")
dictionary1={1:5,2:6,3:"ABC",4:"xyz"}
a1=set(list1)
a2=set(tuple1)
a3=set(dictionary1.values())
a=a1.intersection(a2)
result=a3.intersection(a)
counts=len(result)
print(result)
print("count of most comman elements is:-",str(counts))