# pop()  Removes and returns the last value from the list or the given index value
a = [1,2,4,5,6,7,8]
a.pop()        # print(a.pop())
print(a)

print()

# remove()  Removes(1 element only) a given object from the list
a1 = [1,2,4,5,6,7,8]
a1.remove(4)
print(a1)

print()

# clear()  Removes all items from the list
a2 = [1,2,4,5,6,7,8]
a2.clear()
print(a2)

print()

# reverse() Reserses objects of the list in place
a3 = [1,2,4,5,6,7,8]
    # print(a3[::-1])  reverse korbe or
a3.reverse()
print(a3)

print()

# sort()  Sort a list in ascending or descending
a4 = [10,1,5,4,9,6,5,7,8]
a4.sort()
print(a4)
    # For descending
a4.sort(reverse=True)
print(a4)

print()

# max() or min() Calculates maximum of all the elements of list
a5 = [10,100,5,4,9,6,0,5,7,8]
print(max(a5))
print(min(a5))