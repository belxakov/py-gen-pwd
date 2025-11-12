import random
import string
import pyperclip

def pwd_generate(length, type):
    chars = ''
    if type == 1:
        chars = string.ascii_letters
    elif type == 2:
        chars = string.digits
    elif type == 3:
        chars = string.ascii_letters + string.digits
    else:
        print('Ошибка: вы не выбрали тип генерации или указали некорректное число! (Вы можете выбрать от 1 до 3)')
    pwd = ''.join(random.choice(chars) for pchar in range(length))
    return pwd

pwd_length = int(input('Введите длину пароля (необходимое количество символов): '))
pwd_type = int(input('Выберите тип генерации пароля:\n  1.  Только буквы\n  2.  Только цифры\n  3.  Буквы и цифры\n'))
password = pwd_generate(pwd_length, pwd_type)
print(password)

pwd_buf = input('Желаете сохранить этот пароль в буфер обмена? (y/n): ')
if pwd_buf == 'y':
    pyperclip.copy(password)
    print('Пароль успешно скопирован и сохранен в Ваш буфер обмена!')