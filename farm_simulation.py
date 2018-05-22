from graphics import *
import random
from time import sleep


class Farm:
	def __init__(self):
		self.window = GraphWin()
		self.pesticide = False
		self.fertilizer = False
		self.money = 0
		self.pond_alive = True
		self.algae = 0
		self.field_alive = True
		self.buttons = dict()
		self.window.autoflush = False
		self.buttons['pesticide'] = [Point(100, 100), Point(200, 150)]
		self.buttons['fertilizer'] = [Point(100, 125), Point(200, 145)]
		self.buttons['GO'] = [Point(100, 50), Point(200, 80)]


	def log_state(self):
		return 'pesticide:' + str(self.pesticide) + '\nfertilizer:' + str(self.fertilizer) + '\nmoney:' + str(self.money) + '\npond_alive:' + str(self.pond_alive) + '\nfield_alive:' + str(self.field_alive) + '\nalgae:' + str(self.algae)


	def run_round(self):
		self.display()
		self.make_choices()

		if self.pesticide:
			self.money += 5
			self.algae *= 2 # exponential
		else:
			self.money += 1

		if self.fertilizer:
			self.money += 10
			self.algae *= 2 # exponential
		else:
			self.money += 5
		if self.algae > 5:
			self.pond = False

		# field surviving is more likely if you use chemicals
		if self.fertilizer:
			if self.pesticide:
				rand = 10
			else:
				rand = 6
		else:
			rand = 4

		if random.randint(0, rand) == 0:
			self.field_alive = False


		print(self.log_state())



	def in_button(self, loc, button):
		if loc.getX() <= button[1].getX() and loc.getX() >= button[0].getX():
			if loc.getY() <= button[1].getY() and loc.getY() >= button[0].getY():
				return True

		return False


	def handle_buttons(self, click):
		if self.in_button(click, self.buttons['pesticide']):
			if self.pesticide:
				self.pesticide = False
			else:
				self.pesticide = True
		elif self.in_button(click, self.buttons['fertilizer']):
			if self.fertilizer:
				self.fertilizer = False
			else:
				self.fertilizer = True
		self.refresh_buttons()


	def make_choices(self):
		while(True):
			click = self.window.getMouse()
			if self.in_button(click, self.buttons['GO']):
				print('breaking')
				break
			self.handle_buttons(click)

		self.window.flush()
		sleep(0.5)



	def refresh_buttons(self):
		pesticide = Rectangle(self.buttons['pesticide'][0], self.buttons['pesticide'][1])
		pesticide.setFill('white')
		if self.pesticide:
			pesticide.setOutline('red')
		else:
			pesticide.setOutline('black')
		pesticide.draw(self.window)
		pesticide_label = Text(Point(100, 110), 'toggle pesticide')
		pesticide_label.draw(self.window)

		fertilizer = Rectangle(self.buttons['fertilizer'][0], self.buttons['fertilizer'][1])
		fertilizer.setFill('white')
		if self.fertilizer:
			fertilizer.setOutline('red')
		else:
			fertilizer.setOutline('black')
		fertilizer.draw(self.window)
		fertilizer_label = Text(Point(100, 135), 'toggle fertilizer')
		fertilizer_label.draw(self.window)

		go = Rectangle(self.buttons['GO'][0], self.buttons['GO'][1])
		go.setFill('white')
		go.setOutline('black')
		go.draw(self.window)
		go = Text(Point(100, 65), 'run simulation')
		go.draw(self.window)


	def display(self):
		self.refresh_buttons()

		pond = Circle(Point(50, 50), 25)
		if self.pond_alive:
			pond.setFill('blue')
		else:
			pond.setFill('red')
		pond.draw(self.window)

		field = Rectangle(Point(100, 25), Point(80, 25))
		if self.field_alive:
			field.setFill('green')
		else:
			field.setFill('brown')
		field.draw(self.window)


def conclusion(farm, win):
	window = GraphWin()
	if win:
		label = Text(Point(100, 100), 'YOU WIN!')
	else:
		label = Text(Point(100, 100), 'YOU LOSE!')

	label.draw(window)

	results = Text(Point(0,0), farm.log_state())
	results.draw(window)

	message = Text(Point(window.getWidth()/2, 20), 'Click anywhere to quit.')
	message.draw(window)
	window.getMouse()
	window.close()



farm = Farm()
for i in range(0, 3):
	print('ROUND', i)
	farm.run_round()

if farm.pond_alive and farm.money > 10 and farm.field_alive:
	conclusion(farm, win=True)
else:
	conclusion(farm, win=False)