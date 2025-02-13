def f():

    # local variable
    s = "I like painting"
    print(s)

# Driver code
f()

def test(x, y=10):
    return x * y

print(test(2,3))
print(test(4))

def example(a, b=[]):
    b.append(a)
    return b

print(example(1))
print(example(2))


def func(a, b=5, c=10):
    return a+b*c

print(func(2, c=4))