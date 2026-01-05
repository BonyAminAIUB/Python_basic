# sum of 2 list
a = [1,2,3]
b = [4,5,6]
c = a + b  # 2 ta list k eksathe marge korbe
d = b + a
print(c)
print(d)

print()

#string convert to list using list() function
s = "Hello Bony!"
print(list(s))
print(len(s))

print()

# append() Adds an element at the end of the list
val = [12,24,13,45]
val.append(48)
print(val)
# specific position a rakhte chaile insert(index,value) function
val.insert(2,100)
print(val)

print()

# copy()  Returns a copy of the list
value = [12,24,13,45,50]
cpy = value.copy() # or use ->   cpy = value
print(cpy)

print()

# count()  Returns the number of elements with the specified value
value2 = [1,2,2,2,3,4,2,3,4,5,2,6]
print(value2.count(2))  # 2 koyta ache ta print korbe

print()

# extend()  Add the elemets of a list to the end of the current list
apnd = [12,2,5,6]
apnd.extend([12,19])
print(apnd)   # or   apnd = apnd + [12,19]  -> same output ashbe


