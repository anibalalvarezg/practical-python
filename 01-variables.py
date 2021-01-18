# Assign a variable 
name = 'Anibal'
num = 42

# Check type of variable (type())
print(f'name type is: {type(name)}')
print(f'num type is: {type(num)}')


# Check available methods of a class (dir())
print(dir(str))
print(dir(bool))

# Documentation of a method (help())
help(str.isalpha)

# Parse int 
int("5")

# Parse float
float(3)

# Parse str
str(2345)

#Integer division //
print(25/5)
print(25//5)

# Exp
print((3) ** 2)

# min, max, round
print(min(1, 5, -6))
print(max(10, 20, 100, 2))
print(round(3.9))

# bool type
t = True
f = False

# None 
n = None

# STR

# str quotes
single = 'don\'t'
doble = "don't"

# long strings
a_long_string = """
    very 
    long
    string
"""
print(a_long_string)

# prints
print("hi")
a = 5 
print(a)
print("hi", a)
print(f"hi {a}")

# Concat strings
con = "hi " + "bye"

# Replace
name = 'Anival'
print(name.replace('v', 'b'))

# Upper str 
print('anibal'.upper())