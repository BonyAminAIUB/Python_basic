# Taking multiple inputs from user and store it in a list

# Problem - 1 : Taking multiple string input

a = input("Enter some string value: ").split()  # Bony Amin
print(a)  #  ['Bony', 'Amin']


# Problem - 2 : Taking multiple int input
    #map(data_type, value_input) jehetu input() function always string input ney tai eta ke int a convert korte hobe
a1 = list(map(int, input("Enter some integer value: ").split()))
print(a1)


# Problem - 2 : Taking multiple int input
a2 = list(map(float, input("Enter some integer value: ").split()))
print(a2)
