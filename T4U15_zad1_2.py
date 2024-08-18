# -*- coding: cp1251 -*-
print('Задание 1')
class Transport(object):
	capacity = 50

	def __init__(self, name, max_speed, mileage):
		self.name=name
		self.max_speed=max_speed
		self.mileage=mileage
	
	def seating_capacity (self, capacity):
		self.capacity = capacity
		return(f'Вместимость одногоавтобуса {self.name}: {self.capacity} пассажиров')

autobus = Transport('Renailt Logan', '180', '12')
print(f'Название автомобиля: {autobus.name} Скорость:{autobus.max_speed} Пробег:{autobus.mileage}')


print('Задание 2')
print(autobus.seating_capacity(150))
