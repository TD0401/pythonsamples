#Why do you get an error and how would you fix it?

#def foo(a=2, b):   this generates error, as all the params after default param should also be default
def foo(b, a=2):
    return a + b