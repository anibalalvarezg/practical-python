#

bool(1) # True
bool(0) # False

bool([]) # False
bool([[1,2,3]]) # True

1 == 1 # equal
1 != 1 # not equal

list1 = [1,2,3]
list2 = [1,2,3]

print(list1 == list2) # True

x = None 

print(x is None) # True
print([] is None) # False

a = True 

print(a == True)
print(a is True)


print(a and True) 
print(a or True)

print(a is not False)


if (bool([1,2,3])): 
    print('True')


my_dict = {'key': 'a new value'}
print('key' in my_dict) # True
print('no a key' in my_dict) # False