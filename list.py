a = [11,15,20,1.5,"Alu"]
print(a[3])
print(a[4])
#print(a[10])
a[4] = "Piyaj"
print(a[4])
print()
b = [1,2,3,4,5,"Phitron","Bony"]
#print(b)  sob gulo print korbe
print(b[0])
print(b[-1])  # -1 means last index print korbe ekoi vabe -2 means 2nd last ta print korbe
print(len(b)) # length print korbe
b[-7] = 10 # 1st index er value change hoye 10 print korbe
if 20 in b: # b list er vitor 20 ache kina check kortese
    print("Found")
else:
    print("Not Found")

print()

# Traversing 
for i in b:
    print(i)

print()

for i in range(len(b)):
    print(b[i])

print()

# Reverse printing
for i in range(-1,-len(b)-1,-1):
    print(b[i])

print()

# Another reverse method
for i in range(len(b)-1,-1,-1):
    print(b[i])

print()

# Nested list

c = [[12,13],[18,23,"Phitron"],[-1,-19]]
print(c[0]) # [12,13] print korbe
print(c[0][1]) # 13 print korbe 
c[1][2] = 10
print(c[1][2]) # 10 print korbe ie. string value change kore int replace kora possible
