# let's try write a program which checks which school year a student is in.

name_input = input("What is your name: ")
year_input = input('How old are you: ')

year_input = int(year_input)

# checking condition based on user input

if year_input < 0:
    print("Please enter valid age above 3:")
elif year_input >= 3 and year_input <= 4:
    print(f'{name_input} are you in NURSERY')
elif year_input == 5:
    print(f'{name_input} you are in RECEPTION')
elif year_input >=6 and year_input <= 11:
    print(f'{name_input} you are in JUNIOR/PRIMARYschool')
elif year_input >=12 and year_input >= 15:
    print(f'{name_input} you are in SENIOR SCHOOL')
elif year_input >=16 and year_input <=18:
    print(f'{name_input} you are in SIxth Form Schoool')

else:
    print(f'{name_input} you are at UNIVERSITY??')