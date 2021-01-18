# Declare a list 
arr = list() 
arr_ = []

arr_with_values = [1,2,3,4,5]
arr_str = ["Anibal", "Alvarez", "Gonzalez"]

print(type(arr))


# Get value 

arr_with_values = [1,2,3,4,5]
print(arr_with_values[4]) # 5

arr_with_values[4] = 6
print(arr_with_values[4]) # 6

# Sort list
numbers = [1,2,4,62,-5,-2]
numbers.sort()
print(numbers)
print(sorted(numbers))
print(sorted(numbers, reverse=True))

# Check method of a list 
dir(list)
help(list.count)

# Add new value
numbers.append(999)
numbers.insert(0, 9999)

print(numbers)

# Concat 
numbers += [1,1,1,1]
print(numbers)

# Get length of list
print(len(numbers))

# Delete element in a list 
delete = numbers.pop() 
