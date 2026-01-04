rain = False
if rain == True:
    print("Versity jabo nah") # Gap ta k indentation bola hoy eita maintain korte hobe must
else:
    print("Versity jabo")
print() # only new ekta line print kore
age = 23
if age >= 18:
    print("Driving License pabo")
else:
    print("Driving Licencense pabo nah")


# Logical Operator
print(10-4 == 6 and 10+5 == 15)  # True return korbe(2 tai True hobe)
print(10-4 == 6 or 10+3 == 15)  # True return korbe (jekono 1 ta True hole)
print(not (10+3 != 13))  # Ture return korbe 

marks = 85
if marks>=90 and marks<=100:
    print("A+")
elif marks>=80 and marks<=90:
    print("A")
elif marks>=70 and marks<=80:
    print("A-")
elif marks>=60 and marks<=70:
    print("B")
else:
    print("Fail")   