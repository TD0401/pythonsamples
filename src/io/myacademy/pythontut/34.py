#The following script throws a NameError  in the last line saying that c  is not defined.
# Please fix the function so that there is no error and the last line is able to print out the value of c  (i.e. 1 ).

def foo():
    global c # this makes c as global
    c = 1
    return c
foo()
print(c)