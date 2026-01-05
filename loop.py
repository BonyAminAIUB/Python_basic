# For loop
for i in range(5): # range() er kaj 0 theke sei number er ag porjonto chalona kora (0->4)
    print(i)

# range function(sequence onusare kaj kore)
a = range(10)
print(a)

# range(start,end,step)
b = list(range(10))
print(b)

c = list(range(5,15))
print(c)

d = list(range(5,15,2))
print(d)

e = list(range(15,1,-2))
print(e)

name = "Bony Amin"
for i in name:
    print(i)

bag = ["alu","piyaj",2,2.5]
for i in bag:
    print(i)

lst = [19,5,10,7,4,12,15]
for i in lst:
    if i >= 10:
        print(i)

print()
sum = 0
for i in range(1,11):
    sum += i
print(sum)

print()

for i in range(10):
    if i == 5:
        break
    print(i)

print()

# infinite loop

