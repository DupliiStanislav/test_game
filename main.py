import random
import time


class Character:
	def __init__(self, name):
		self.name = name
		self.health = 100

	def __str__(self):
		return f'{self.name} имеет {self.health} здоровья'


class Game:
	def __init__(self):
		self.player = Character('player')
		self.computer = Character('computer')
		self.end = True

#   создаем метод для снятия очков здоровья
	def hit(self, char):
		damage = random.randint(18, 25)
		# проверка, что количество здоровья не заходит в минус
		if (char.health - damage) < 0:
			char.health = char.health - char.health
			self.end = False
			print(f'{char} получил урон в размере {damage}\n{char.name} Проиграл')
		else:
			char.health -= damage
			print(f'{char} получил урон в размере {damage}')

	# метод для снятия очков здоровья
	def hit_more(self, char):
		damage = random.randint(10, 35)
		# проверка, что количество здоровья не заходит в минус
		if (char.health - damage) < 0:
			char.health = char.health - char.health
			self.end = False
			print(f'{char} получил урон в размере {damage}\n{char.name} Проиграл')
		else:
			char.health -= damage
			print(f'{char} получил урон в размере {damage}')

	# метод для добавления очков здоровья
	def heal(self, char):
		healing = random.randint(18, 25)
		# проверка, что здоровье не может быть больше чем 100
		if (char.health + healing) > 100:
			char.health = 100

		else:
			char.health += healing
			print(f'{char} получил лечение в размере {healing}')


	# метод для рандомного приминения одного из методов для снятия
	# или пополнения очков здоровья
	def get_random_action(self, char):
		a = random.randint(1, 3)
		b = random.randint(1, 100)

		# в случае если у компьютера меньше 35% здоровья, он чаще получает лечение
		if self.computer.health <= 35:
			if b <= 33:
				self.hit(char)
			elif b > 35 and b <= 66:
				self.hit_more(char)
			elif b > 60:
				self.heal(self.computer)
			elif b > 66:
				self.heal(self.player)
		else:
			if a == 1:
				self.hit(char)
			elif a == 2:
				self.hit_more(char)
			else:
				self.heal(char)

	def logic(self):
		# рандомно выбираем за кем первый ход
		players = [self.computer, self.player]
		random.shuffle(players)
		first = players[0]
		second = players[-1]
		print(f'Первым ходит {first.name}')

		while self.end:
			time.sleep(1.0)
			self.get_random_action(first)
			self.get_random_action(second)



if __name__ == '__main__':
	start = Game()
	start.logic()
