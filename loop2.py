# while loop
i = 0
while i<=10:
    i+=1
    if i == 5:
        break
    print(i)

print()

# infinite loop

# while True:
#     print("I love Python")

while True:
    a = input("Enter your name: ")
    if a == "quit" or a == "q":
        break
    print("Hello",a)