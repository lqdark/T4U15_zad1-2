# -*- coding: cp1251 -*-
print('������� 1')
class Transport(object):
	capacity = 50

	def __init__(self, name, max_speed, mileage):
		self.name=name
		self.max_speed=max_speed
		self.mileage=mileage
	
	def seating_capacity (self, capacity):
		self.capacity = capacity
		return(f'����������� �������������� {self.name}: {self.capacity} ����������')

autobus = Transport('Renailt Logan', '180', '12')
print(f'�������� ����������: {autobus.name} ��������:{autobus.max_speed} ������:{autobus.mileage}')


print('������� 2')
print(autobus.seating_capacity(150))
