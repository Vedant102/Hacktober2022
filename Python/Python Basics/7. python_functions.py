def hello_fun():
    pass # we are not using it right now
print(hello_fun) # just tells us that there is some function that occupies some space in the memory at some address
print(hello_fun()) # prints None, because no return value is present

def ffun():
    print('Hello bemta')
ffun()

def fun():
    return 'Hello fren'
print(fun()) # we can treat this return function as a string, and also store it in a variable

print(len('hemloo')) # this function returns an integer

# Passing values to function
def hello(greeting,name='Beluga'): # arguments can be set to a default value also
    return '{}, {} '.format(greeting,name)
print(hello('Hola','Kratos'))

def star(*args,**kwargs): # allowing us to accept an arbitrary number of positional or keyword arguments
    print(args) # args takes positional arguments, and prints a tuple
    print(kwargs) # kwargs takes keyword arguments, stores the keyword values in a dictionary

star("maths","arts","physics",name='Beluga',age=19)



def star(*args,**kwargs): # allowing us to accept an arbitrary number of positional or keyword arguments
    print(args) # args takes positional arguments, and prints a tuple
    print(kwargs) # kwargs takes keyword arguments, stores the keyword values in a dictionary
courses=['maths','arts','physics']
info={'age':22,'name':'Beluga','roll number':21045133}
# star(courses,info) this will put both the list and the dictionary in the tuple (args argument)
star(*courses,**info)























































