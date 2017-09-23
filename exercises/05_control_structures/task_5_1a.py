# -*- coding: utf-8 -*-
'''
Задание 5.1a

Сделать копию скрипта задания 5.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip_addr = input('Введите IP-сети в формате 10.1.1.1: ')

ip_addr = ip_addr.split('.')

if (len(ip_addr) != 4):
    print('Incorrect IPv4 address')
elif (int(ip_addr[0]) < 0 or int(ip_addr[0]) >255):
    print('Incorrect IPv4 address')
elif (int(ip_addr[1]) < 0 or int(ip_addr[1]) >255):
    print('Incorrect IPv4 address')
elif (int(ip_addr[2]) < 0 or int(ip_addr[2]) >255):
    print('Incorrect IPv4 address')
elif (int(ip_addr[3]) < 0 or int(ip_addr[3]) >255):
    print('Incorrect IPv4 address')
elif (int(ip_addr[0]) >= 1 and int(ip_addr[0]) <= 223):
    print('unicast')
elif (int(ip_addr[0]) >= 224 and int(ip_addr[0]) <= 239):
    print('multicast')
elif (int(ip_addr[0]) == 255 and int(ip_addr[1]) == 255 and int(ip_addr[2]) == 255 and int(ip_addr[3]) == 255):
    print('local broadcast')
elif (int(ip_addr[0]) == 0 and int(ip_addr[1]) == 0 and int(ip_addr[2]) == 0 and int(ip_addr[3]) == 0):
    print('unassigned')
else:
    print('unused')
