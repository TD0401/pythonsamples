#Why do you get an error and how would you fix it?


def foo(a=1, b=2):
    return a + b


#x = foo - 1  this generate error as it treats func and int can not be subtracted. ideally there should be paranthesis after foo to treat this as function
x=foo() -1
print(x)