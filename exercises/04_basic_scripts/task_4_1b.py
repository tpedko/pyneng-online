# -*- coding: utf-8 -*-
'''
Задание 4.1b

Преобразовать скрипт из задания 4.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

ip_mask = argv[1:]

ip_mask = ''.join(ip_mask[0:])


#ip_mask = input('Введите IP-сети в формате 10.1.1.0/24: ')

ip_mask = str(ip_mask)

ip_mask = ip_mask.split('/')
ip = ip_mask[0]
mask = ip_mask[1]

ip_bit = ''.join('{:>08b}'.format(int(x)) for x in ip.split('.'))
ip_bit = ip_bit[0:int(mask)]+'0'*(32-int(mask))

print('Network:')
print('{:<10}{:<10}{:<10}{:<10}'.format(int(ip_bit[0:8],2),int(ip_bit[8:16],2),int(ip_bit[16:24],2),int(ip_bit[24:32],2)))
print('{:<10}{:<10}{:<10}{:<10}'.format(ip_bit[0:8],ip_bit[8:16],ip_bit[16:24],ip_bit[24:32]))

print('\nMask:')
print('/{}'.format(mask))
mask = '{:<b}{}'.format(2**int(mask)-1,'0'*(32-int(mask)))
print('{:<10}{:<10}{:<10}{:<10}'.format(int(mask[0:8],2),int(mask[8:16],2),int(mask[16:24],2),int(mask[24:32],2)))
print('{:<10}{:<10}{:<10}{:<10}'.format(mask[0:8],mask[8:16],mask[16:24],mask[24:32]))
