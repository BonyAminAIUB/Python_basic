'''
x = 10
y = 3.14168769898709709
print(type(x))
print(type(y))
print(x)
x,y = y,x   # swap
print(x)
#print(y)

description = "Phitron is a platform to learn coding"
print(description.count("platform"))    # description word koybar ache seta count korbe

description1 = 142135623730951
print(len(str(description1))) # number count korbe

dd = "Phitron"
n_dd = dd[0:5:1] # [start:end:step] kind of loop (etake slicing bole)
print(n_dd)
n_dd = dd[::-1] # reverse hobe
print(n_dd)


various = [10, 20.5, "String", True]
print(various) 
print(type(various[2]))

number = [1,2,3,4,5]
print(number[::-1]) # slicing (list er value print korbe)



a = 15
if a>10:
    print("Yes")
else:
    print("No")

for i in range(0,10,1): # range(start,end,step)
    print(i)
    print()


    
number1 = [1,2,3,4,5]
for i in number1:
    print(i)

accuracy = 0
while accuracy<10:
    print("Train")
    accuracy += 2

'''