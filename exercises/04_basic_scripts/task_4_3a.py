# -*- coding: utf-8 -*-

'''
Задание 4.3a

Дополнить скрипт из задания 4.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']

d_mode = dict(access='Enter VLAN number: ', trunk='Enter allowed VLANs: ')



mode = input('Enter interface mode (access/trunk): ')
inf = input('Enter interface type and number: ')

vlan = input(d_mode[mode])

d_access = dict.fromkeys(access_template)
d_trunk = dict.fromkeys(trunk_template)
d = dict(access=d_access, trunk=d_trunk)

print('interface {}'.format(inf))
print(' \n'.join(d[mode]).format(vlan))
