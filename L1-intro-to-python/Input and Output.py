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
# at the end you see ediable pizza. likewise... in programing a functions consists of 
# multiple stages producing output as a result of an input.

# mathamaticaly function takes one or more argument
# f(5x) + f(6y) = z two function adding to Z.
# 
# back to imput() function.
#  


#a,b = input("Ram please enter two numbers to add") # it seems it doesn't have method()
# menthod() as small action you can perform within a big function.
# so we need to change our functino a bit.
# going back to our example: "a = 9876" and "b = 937659".
# a = input("Ram add your first number:")
# b = input("Ram add your second number:")

# print("Ram yoour first number is", a)
# print("and your second number is:",b)
# c = a+b
# ok that worked. what's left now... to sum these two numbers.

# print(f'Ram your two numbers {a} and {b} add up to {a+b} is that correct')
# print(f'Ram your two numbers {a} and {b} add up to {c} is that correct')

# ok then i came across converting into integer using int() fucntion.

a = int(input("Ram add your first number:"))
b = int(input("Ram add your second number:"))

print("Ram yoour first number is", a)
print("and your second number is:",b)
c = int(a+b)

print(f'Ram your two numbers {a} and {b} add up to {c} is that correct')

