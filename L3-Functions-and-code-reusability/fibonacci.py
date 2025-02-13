print(f'-=====================')
def fib(n):    # write Fibonacci series less than n

    """Print a Fibonacci series less than n."""

    a, b = 0, 1

    while a < n:

        print(a, end=' ')

        a, b = b, a+b
        print(a+b)
    print()

# Now call the function we just defined:

fib(50)

print(f'list of Fibinacci series')

def fibList(n):
    result = []

    a, b = 0, 1 
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f30 = fibList(30)
f30

def fib2(n):  # return Fibonacci series up to n

    """Return a list containing the Fibonacci series up to n."""

    result = []

    a, b = 0, 1

    while a < n:

        result.append(a)    # see below

        a, b = b, a+b

    return result


f100 = fib2(100)    # call it

f100                # write the result