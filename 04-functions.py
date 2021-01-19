# Declare function
def my_func(): 
    print('hi')

greeting = my_func() 

print(f"greeting {greeting}")


def add_numbers(x, y, z=1): 
    return x + y + z

# Call a fn
print(add_numbers(3, 7))
print(add_numbers(3, 7, 2))
print(add_numbers(z=1, y=2, x=3))

def create_query(language="Javascript", num_stars=10, sort="desc"): 
    return f"language: {language}, num_stars: {num_stars}, sort is {sort}"

print(create_query())

#Keyword Arguments
def add_numbers_(*args): 
    print(args)

add_numbers_(1,2,3,4,5,6,7)

# Keyword Arguments
def my_function(**kwargs): 
    print("His last name is " + kwargs["lname"])

my_function(fname = "Aníbal", lname = "Álvarez")
