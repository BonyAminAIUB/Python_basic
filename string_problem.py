# Simple problem solving string sort
# Input  : x3b4U5i2
# Output : bbbbiiUUUUUxxx

a = input("Enter: ")
res = ""
for i in range(0, len(a), 2):
    print(f"{a[i]} {a[i+1]}")
    res = res + a[i]*int(a[i+1])
result = sorted(res, key=str.casefold)
res_string = "".join(result) # list to string conversion
print(res_string)