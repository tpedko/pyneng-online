# -*- coding: utf-8 -*-
'''
Задание 3.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_value = ospf_route.replace(',','').replace('[','').replace(']','').split()
ospf_value[0] = 'OSPF'
ospf_value.remove('via')

print('{:24}{}'.format('Protocol:', ospf_value[0]))
print('{:24}{}'.format('Prefix:', ospf_value[1]))
print('{:24}{}'.format('AD/Metric:', ospf_value[2]))
print('{:24}{}'.format('Next-Hop:', ospf_value[3]))
print('{:24}{}'.format('Last update:', ospf_value[4]))
print('{:24}{}'.format('Outbound Interface', ospf_value[5]))


'''
for t, o in :
    print('{:25}{}'.format(t, o))

ospf_list = [x for x in ospf_route.replace(',', '').split(' ') if len(x) > 1]

ospf_list.insert(0, 'OSPF')
ospf_list.remove('via')

ospf_value = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Interface']

ospf_value = dict.fromkeys(ospf_value)



for key, value in r1.items():
    print('{:25}{}'.format(key, value))


for key, value in r1.items():
    print('{:20} => {}'.format(key, (s for s in ospf_router)))
'''