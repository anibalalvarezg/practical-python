# Tuples
# Declare
my_tup = ()
tuple_a = ("hola",1)

student = ("Anibal", 8, "History", 3.4) 

name, num, subject, gpa = student
print(name, num, subject, gpa)

# Get values
print(student[1]) # second
print(student[-1]) # last
print(student[2:5]) # index 3 and 4

# Sets
# Declare
my_set = {1,2,3} # {} is a dict
my_set = set() 

my_set = {3,3,4} # {3,4}

names = ['Anibal', 'Anibal', 'Nicolas']
print(set(names))

my_set.add(5)

my_set.discard(5)

color = {'red', 'orange'}

color.update(my_set)


# Dictionaries
dict = {"one": 1, "two": 2}
print(type(dict))
print(dict['one'])
print(dict['two'])

dict2 = {'one': [1,1,1]}
print(dict2['one'])
print(dict.get("three", "default"))

dict2['two'] = 'twotwotowtwo'
print(dict2.get('two'))

# dict keys 
dict.keys() 

# dict values
dict.values()

# dict [(key, value)]
dict.items() 