from random import randint

max_limit = 100

def new_game():
    secret_number = str(randint(1, max_limit))
    #print(secret_number)
    counter = 0
    print('Добро пожаловать в числовую угадайку')
    user_number = input(f'Введите число от 1 до {max_limit}: ')
    return (is_valid(user_number, counter, secret_number)) 
                             
def is_valid(user_number, counter, secret_number): 
    if user_number.isdigit() and 1 <= int(user_number) <= max_limit:
        counter += 1
        return compare_num(user_number, secret_number, counter)
    else:
        user_number = input(f'А может быть все-таки введем целое число от 1 до {max_limit}?: ')
        return is_valid(user_number, counter, secret_number)

def compare_num(user_number, secret_number, counter):
    if user_number > secret_number:
        user_number = input('Ваше число больше загаданного, попробуйте еще разок: ')
        return is_valid(user_number, counter, secret_number)
    elif user_number < secret_number:
        user_number = input('Ваше число меньше загаданного, попробуйте еще разок: ')
        return is_valid(user_number, counter, secret_number)
    else:
        print(f'Вы угадали, поздравляем! Число попыток {counter}')
        game = input('Вы хотите сыграть еще раз? Y - да, N - нет: ')
        while True:
            if game == 'Y' or game == 'y':
                return new_game()
            elif game == 'N' or game == 'n':
                return 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
            else:
                game = input('Введите корректный ответ. Y - да, N - нет: ')
               
new_game()

