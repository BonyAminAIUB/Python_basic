value = int(input("Enter value: "))
for i in range(value):
    for j in range(i+1):
        print("#",end=" ")
    print()

value1 = int(input("Enter value: "))
for i in range(0,value1):
    for j in range(i+1):
        print(chr(97+i),end=" ")
    print()