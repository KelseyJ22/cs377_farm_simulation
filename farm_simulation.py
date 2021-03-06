from graphics import *
import random
from time import sleep


class Farm:
	def __init__(self):
		self.window = GraphWin('Farm', 500, 500)
		self.pesticide = False
		self.fertilizer = False
		self.money = 0
		self.pond_alive = True
		self.algae = 1
		self.field_alive = True
		self.buttons = dict()
		self.window.autoflush = False
		self.buttons['pesticide'] = [Point(325, 300), Point(500, 350)]
		self.buttons['fertilizer'] = [Point(325, 350), Point(500, 400)]
		self.buttons['GO'] = [Point(325, 400), Point(500, 450)]


	def log_state(self):
		return 'pesticides applied: ' + str(self.pesticide) + '\nfertilizer applied: ' + str(self.fertilizer) + '\nmoney: $' + str(self.money) + '\npond_alive: ' + str(self.pond_alive) + '\nfield_alive: ' + str(self.field_alive) + '\nalgae: ' + str(self.algae)


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
		pesticide_label = Text(Point(412, 325), 'pesticides on/off')
		pesticide_label.draw(self.window)

		fertilizer = Rectangle(self.buttons['fertilizer'][0], self.buttons['fertilizer'][1])
		fertilizer.setFill('white')
		if self.fertilizer:
			fertilizer.setOutline('red')
		else:
			fertilizer.setOutline('black')
		fertilizer.draw(self.window)
		fertilizer_label = Text(Point(412, 375), 'fertilizer on/off')
		fertilizer_label.draw(self.window)

		go = Rectangle(self.buttons['GO'][0], self.buttons['GO'][1])
		go.setFill('white')
		go.setOutline('black')
		go.draw(self.window)
		go = Text(Point(412, 425), 'run simulation')
		go.draw(self.window)


	def display(self):
		self.refresh_buttons()

		pond = Circle(Point(150, 125), 100)
		if self.pond_alive:
			pond.setFill('blue')
		else:
			pond.setFill('red')
		pond.draw(self.window)

		field = Rectangle(Point(25, 250), Point(275, 490))
		if self.field_alive:
			field.setFill('green')
		else:
			field.setFill('brown')
		field.draw(self.window)

		clear = Rectangle(Point(300, 5), Point(500, 100))
		clear.setFill('white')
		clear.draw(self.window)
		results = Text(Point(400, 50), farm.log_state())
		results.draw(self.window)


def conclusion(farm, win):
	window = GraphWin('Conclusion', 500, 500)
	if win:
		label = Text(Point(250, 50), 'YOU WIN!')
	else:
		label = Text(Point(250, 50), 'YOU LOSE!')

	label.draw(window)

	results = Text(Point(100, 100), farm.log_state())
	results.draw(window)

	message = Text(Point(400, 400), 'Click anywhere to quit.')
	message.draw(window)

	window.getMouse()
	window.close()


farm = Farm()
for i in range(0, 5):
	print('ROUND', i)
	farm.run_round()
	if not farm.field_alive:
		conclusion(farm, win=False)
		break

if farm.pond_alive and farm.money > 10 and farm.field_alive:
	conclusion(farm, win=True)
else:
	conclusion(farm, win=False)
