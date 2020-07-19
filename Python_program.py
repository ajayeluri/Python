
#DataTypes

#Every thing in python is a object,every varible holds an object instance.When an object is initiated it is assigned a unique object id.
#Mutable objects can change its state or content,immutable objects cannot.
#Mutable objects:list, dict, set, byte array& Immutable objects:int, float, complex, string, tuple, frozen set,bytes

#Built in data structures in python are List,Dictionary,Tuple and Set.

#List

num =[]
num.append(10)
num.append(20)

#inserts element at given position
num.insert(3,24)
print(num)

#using iterator to add elements to list
List =[]
for i in range(1,4):
    List.append(i)
print(List)


#List.clear()  # remove all elemets from list
#List.reverse() # reverse all the elements in list
#List.remove(2) # removes element at index 2
#num.sort(reverse=True) # Sorts in desc if reverse =True
#print(num.count(20)) # returns number of times 20 appeared in list
print(num.pop(2)) # removes element at given index