# -*- coding: utf-8 -*-
'''
Задание 4.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip_mask = input('Введите IP-сети в формате 10.1.1.0/24: ')

ip_mask = ip_mask.split('/')
ip = ip_mask[0]
mask = ip_mask[1]

print('Network:')
print(''.join('{:<10}'.format(x) for x in ip.split('.')))
print('  '.join('{:>08b}'.format(int(x)) for x in ip.split('.')))
print('\nMask:')
print('/{}'.format(mask))
mask = '{:<b}{}'.format(2**int(mask)-1,'0'*(32-int(mask)))
print('{:<10}{:<10}{:<10}{:<10}'.format(int(mask[0:8],2),int(mask[8:16],2),int(mask[16:24],2),int(mask[24:32],2)))
print('{:<10}{:<10}{:<10}{:<10}'.format(mask[0:8],mask[8:16],mask[16:24],mask[24:32]))

'''
print('/', mask, sep='')

mask = ('1' * int(mask)+('0' * 32))[:32]
'''