# -*- coding: utf-8 -*-
'''
Задание 4.1

Обработать строку nat таким образом,
чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

nat = 'ip nat inside source list ACL interface FastEthernet1/1 overload'

nat.replace('Fast', 'Gigabit')
