# what is input and output:
# suppose a user enters name = Ram,Location = Bharat and age = 23, 
# and expecting to print it back Ram is 23 years old and lives in Bharat.

# let's try and code this:

# firt you need three placeholders for Name,Location and Age to store it's value.
# <<name>> is <<age>> years old and lives in <<loaction>>.
name='Ram'
age=23
location='Bharat'

#print # <<name>> is <<age>> years old and lives in <<loaction>>.

print('$name') # that did not work , you try
print(name) # that worked

#print(name'is') # that did not work

# there's something called f-string
print(f"{name} is {age} years old and lives in {location}.") # this works.


# lets take another example
# say Ram wants to know sum of two numbers 23 + 65 = ?? I don't know 

# let's assign placeholder, input variables:

a = 23
b = 65

c = a+b

print(f'sum of {a} and {b} is {c}') # what does it print??

# now if you noticed last two examples we been providing input in the program.
# but say if Ram wants it to run program dynamically so that he does't have to edit code?
# what is imput variables changes everytime. Ram wants to change
# value of "a = 9876" and "b = 937659". he has to edit program everytime
# he wants to change variable.
# time to intorduce Input() function. probably thinking what is a function().
# imagine there's a there's a Pizza making factory. There will be different stages/areas
# e.g: Dough making, Tomatto catchup, Fruit and Vegitable, Oven and slishers.
# at the end you see ediable pizza.


