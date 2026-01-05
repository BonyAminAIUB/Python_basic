'''
val = int(input("Enter a number: "))
for i in range(1,11):
    print(val,"*",i,"=",val*i)

print()
# Factorial Problem
val2 = int(input("Enter a number: "))
fact = 1
for i in range(1,val2+1):
    fact = fact * i
print(fact)

print()
# Fibonacci Series
val3 = int(input("Enter a number: "))
first = 0
second = 1
# Shortcut -> first,second = 0,1
for i in range(val3):
    print(first,end=" ")  
    result = first + second
    first = second
    second = result


print()
print()
# Counting Number Digit in a Number
a = int(input("Enter a number: "))
count = 0
while a>0:
    count = count + 1
    a = a // 10
print(count)

#shortcut
a1 = input("Enter a number: ")
print(len(a1))

print()
'''
# Reverse A number
b = int(input("Enter a number: "))
rev_a = 0
while b>0:
    last_digit = b % 10
    rev_a = rev_a*10 + last_digit
    b = b // 10
print(rev_a)   

    