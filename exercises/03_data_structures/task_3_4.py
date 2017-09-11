# -*- coding: utf-8 -*-
'''
Задание 3.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
list1 = command1.split()[-1].split(',')
list2 = command2.split()[-1].split(',')
result1 = [int(s) for s in list1 ]
result2 = [int(s) for s in list2 ]
result3 = list(set(result1).intersection(set(result2)))
print(result3)