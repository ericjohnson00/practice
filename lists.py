"""
List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

"""


"""
    
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
    
"""


my_list = ["pie", "cat", "ace", "kim", "chong"]
my_list2 = [20, 6, 4]
mixed_list = [69, "hey", 44, "bong", "smoke"]

print(f"Original: { my_list }")
print(f"Original: { my_list2 }")
print()

# list methods

# APPEND .append()

my_list.append("cheech")
my_list2.append(420)
print(f"Append: { my_list }")
print(f"Append: { my_list2 }")
print()

# COPT .copy()

copied_list = my_list.copy()
print(f"Copy: { copied_list }")
print()

# COUNT .count()

count = my_list.count("cat")
print(f"Count: { count }")
print(f"Count: { my_list2.count(420) }")
print()

# SORT .sort()

# cant compare int and strings 
# mixed_list.sort()
my_list.sort()
my_list2.sort()

print(f"Sort: { my_list }")
print(f"Sort: { my_list2 }")
print()

# sorted()

sorted_list = sorted(my_list)
print(f"Sorted: { sorted_list }")
print()

# EXTEND .extend()
num_tup = (2, 6, 1, 8)
my_list.extend(num_tup)  # Modifies my_list in-place
print(f"Extended List: {my_list}") # extends tule and list

my_list.extend(my_list2)
print(f"Extended List: {my_list}") # extends 2 lists
print()

# INDEX .intex(x)
# my_list.index(2)
print(f"Index: {my_list.index(2)}") # shows index of the first value
print()

# INSERT .insert()
# list.insert(pos, elmnt)
my_list.insert(0, "booty")
print(f"Insert: {my_list}")
print()

# POP .pop()
my_list.pop(5)
print(f"Pop: {my_list}")
print()

# REMOVE .remove()
my_list.remove(2)
my_list.remove(6)
my_list.remove(4)
my_list.remove(8)
print(f"Remove: {my_list}")
print()

# REVERSE .reverse()
my_list.reverse()
print(f"Reverse: {my_list}")
print()


# LOOPING THROUGH LISTS #################################################
print("LOOPING: ")
print()

for x in my_list:
    print(x)
    
print()

# Using the enumerate()
# enumerate(my_list) returns pairs of (index, item) for each element in the list.

for index, item in enumerate(my_list2):
    print(f"{index}: {item}")
    
print()

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

for i in range(len(my_list)):
    print(my_list[i])
    
print()



# Using a While Loop
# You can loop through the list items by using a while loop.

# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

# Remember to increase the index by 1 after each iteration.
n = 0
while n < len(my_list2):
    print(my_list2[n])
    n = n + 1
    
print()



# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:

[print(x) for x in my_list]

print()


# ACCESSING AN INDEX ###########################################################

print(my_list[2])
print(my_list[-2])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.
print(my_list[2:7])

# By leaving out the start value, the range will start at the first item:
print(my_list[:2])
print(my_list[2:])


if "cat" in my_list:
    print("Yes!")