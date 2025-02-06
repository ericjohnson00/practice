# Different ways to iterate (for loops)

# for loops
# Iterate over elements of an iterable (lists, tuples, strings, etc.).
for item in [1, 2, 3]:
    print(item)

# using the range() function
for i in range(5):
    print(i)
    
    
names = ["Alice", "Bob", "Charlie"]
for index in range(len(names)):
    print(index, names[index])
    
    
# with iter() functom
list = [1,2,3,4,5]

it = iter(list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Manual Iteration with iter() and next()
# Manually advance an iterator.
nums = iter([1, 2, 3])
print(next(nums))  # 1
print(next(nums))  # 2 (raises StopIteration when exhausted)


# while loops
# Repeat until a condition is False.
i = 0
while i < 4:
    print(i)
    i += 1


# comprehensions
# Concise syntax for creating lists, dictionaries, sets, or generators.
# List comprehension
squares = [x**2 for x in range(3)]  # [0, 1, 4]


# Generator expression
gen = (x**2 for x in range(3))  # Iterate via next(gen) or for loop


#  Iterating Over Files
# Read lines from a file directly.
with open('file.txt') as f:
    for line in f:
        print(line.strip())
        
        
# Generator Functions
# Use yield to create iterators.
def count_up_to(n):
    i = 0
    while i <= n:
        yield i
        i += 1

for num in count_up_to(3):
    print(num)  # 0, 1, 2, 3