# password generator 

import random

alphabet = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYXZ'
numbers = '0123456789'
simbols = '#$%&?!+-_=/'

full_data = alphabet + numbers + simbols

length_password = int(input('Введите длину пароля: '))
psw = ''

for i in range(length_password):
    psw += random.choice(list(full_data))

print(psw)
