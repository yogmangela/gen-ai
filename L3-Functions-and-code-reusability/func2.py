# Globle variable
def f():
    print(s)


s = 'This is a Global Variable'

f()

print(f'========Lets try Local and Global variable=========')

def f():
    s = "This is a LOCAL Variable"
    print(s)


s = "This is a GLOBAL Variable"

f()
print(s)

print(f'===================================')
def f():
    global s
    print(s)
    s="This is Global var"
    print (s)

s = "this is Global Variable"
f()
print(s)
