# -*- coding: utf-8 -*-
'''
Задание 5.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip_addr = input('Введите IP-сети в формате 10.1.1.1: ')

ip_addr = ip_addr.split('.')

if (int(ip_addr[0]) >= 1 and int(ip_addr[0]) <= 223):
    print('unicast')
elif (int(ip_addr[0]) >= 224 and int(ip_addr[0]) <= 239):
    print('multicast')
elif (int(ip_addr[0]) == 255 and int(ip_addr[1]) == 255 and int(ip_addr[2]) == 255 and int(ip_addr[3]) == 255):
    print('local broadcast')
elif (int(ip_addr[0]) == 0 and int(ip_addr[1]) == 0 and int(ip_addr[2]) == 0 and int(ip_addr[3]) == 0):
    print('unassigned')
else:
    print('unused')
