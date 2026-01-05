# Palindrome string checking
# input  : "madam"
# output : "yes"

a = input("Enter string: ")
if a == a[::-1]:
    print("Yes")
else:
    print("No")



# string reversing
# input  : "I love coding using Python"
# output : "I evol fnidoc fnisu nohryP"

a = input("Enter: ")
a = a.split(" ")
result = ""
for i in a:
    result += i[::-1] + " "
print(result)
