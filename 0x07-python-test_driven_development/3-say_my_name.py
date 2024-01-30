'''
3-say_my_name module
The module has say_my_name function to print 
both first_name and last_name
'''
def say_my_name(first_name, last_name=""):
    """
    say_my_name accept 2 parameters
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
