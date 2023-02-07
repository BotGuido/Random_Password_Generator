'''
The first thing we need to do is to import the required packages and modules.
In this project, we import random and math modules to make use of their functions.

Первое, что нам нужно сделать, это импортировать необходимые пакеты и модули.
В этом проекте мы импортируем случайные и математические модули, чтобы использовать их функции.
'''

import random
import math

'''
After the import section, we define three variables for storing alphabets, integers and special characters.

После раздела импорта мы определяем три переменные для хранения алфавита, целых чисел и специальных символов.
'''

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*!^&()"

'''
In this section of code implementation, we will define how much the length of the alphabets, 
integers and special characters must occupy in the resultant string.

В этом разделе реализации кода мы определим длину букв,
целых числа и специальных символов, которые займут результирующую строку.
'''

pass_len = int(input("Enter Password Length: "))

# length of password by 50-25-25 formula
alpha_len = pass_len // 2
num_len = math.ceil(pass_len * 25 / 100)
special_len = pass_len - (alpha_len + num_len)
password = []

'''
In this section, we define a function called generate_pass(), and we will append 
the respective alphabets, integers, or special characters based on the password length.

В этом разделе мы определяем функцию с именем generate_pass() и добавим
соответствующие буквы, целые числа или специальные символы в зависимости от длины пароля.
'''

def generate_pass(length, array, is_alpha=False):
    for i in range(length):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if is_alpha:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        password.append(character)

'''
In the last section, we will call the generate_pass() function 
with all the possible ways of passing arguments and finally loop 
through the list and create the final string gen_password and print it.

В последнем разделе мы вызовем функцию generate_pass().
со всеми возможными способами передачи аргументов и, наконец, циклом
через список и создадим окончательную строку gen_password и отобразим ее.
'''

# alpha password
generate_pass(alpha_len, alpha, True)
# numeric password
generate_pass(num_len, num)
# special Character password
generate_pass(special_len, special)
# suffle the generated password list
random.shuffle(password)
# convert List To string
gen_password = ""
for i in password:
    gen_password = gen_password + str(i)
print(gen_password)