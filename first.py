
print("Bony Amin")
hello = "Hello "
my_name = "Bony"
bazar = ["piyaj","alu",'hello',2,1.34] #bazar ekta list type variable
print(bazar)
_ = 10 # variable name start with letter and underscore character
print(_)
print(hello + my_name) # string 2 tar sum
name = input("Enter your name: ") #space input ney nah
# input function always sting format a data nibe
print("My name's: ",name) # print function autometic new line print korse
# multi line comment er jonno ''' '''
# shortcut for single line comment ctrl + /
''' 
hello
'''
# Python Arithmetic Operator +,-,/,*,%
# ** Exponentiation
# // Floor division
a = 15
b = 2
print(a+b) # 17
print(a-b) # 13
print(a*b) # 30
print(a/b) # 7.5 float value dibe
print(a//b) # 7 integer value dibe
print(2**3) # 2 ^ 3 = 8  
print(a%b) # 1 modulus value dibe

print(3>5) # boolean value(True ou False) return korbe

# Type Casting
age1 = int(input("Enter your age: ")) 
# input() always string input ney but ekhane variable age ekta inter tai amra type casting korsi
if age1 >= 18:
    print("You are adult")
else:
    print("You are child")

weight = float(input("Enter weight: "))
print(type(weight)) # type print korbe eta --> <class 'float'>
print(int(weight)) # integer value output dekhabe

