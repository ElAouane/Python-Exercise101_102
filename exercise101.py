#Input user details

name = 'Lana'
last_name = 'Smith'
age = 26
eye_color = 'Green'
hair_color = 'Black'

name = input(f'Hello {name}, what new name would you like?: ')
last_name = input(f'what new surname would you like?: ')
age = input(f'How old would you like to be?: ')
eye_color = input(f'What eye color would you like?: ')
hair_color = input(f'What hair color would you like?: ')
print("Hello {} {}! Welcome, your age is {}, your eyes are {} and your hair are {}".format(name,last_name, age, eye_color, hair_color))
