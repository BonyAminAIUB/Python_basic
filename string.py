a = 'hello Bony'
b = "Hello Bony"
c = """This is
a 
multiple
line string
"""
print(a)
print(b)
print(c)

print(a[5])
print(a.lower())
print(a.upper())
print(a.capitalize())
print(a.title())
print(a.swapcase())
print(a.casefold()) # more powerful than lower()

d = "Helle"
e = d.replace('e','o',1)
print(e)
print(a.count('l'))
f = '23'
print(f.isdigit())
g = ["h","e","l","l","o"]
print("".join(g))
h = ["1","4","3"] # only for string er jonno
print("".join(h))
print(list(a))
print(a.split())