# Expression for item in list -> [expression for item in list]
a = [10,20,30,40,50]
b = [i+5 for i in a]
print(b)

print()

name = "Bony Amin"
b = [i for i in name]
print(b)  # ['B', 'o', 'n', 'y', ' ', 'A', 'm', 'i', 'n']  
c = list(b)   #  pray same as line 7
print(c)

print()

d = [i for i in range(1,20,2)]
print(d)






