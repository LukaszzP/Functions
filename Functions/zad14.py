import zad13_keyboard

first_name = zad13_keyboard.input_string('Enter name: ')
last_name = zad13_keyboard.input_string('Enter last name: ')
age = zad13_keyboard.input_integer('Enter age: ')
salary = zad13_keyboard.input_real('Enter salary: ')
is_salary_hidden = zad13_keyboard.input_boolean('Hide salary? (y/n): ')

print('DATA RECORD')
print('===========')
print('Name:', first_name, last_name)
print('Age:', age)
if not is_salary_hidden:
    print('Salary:', salary)