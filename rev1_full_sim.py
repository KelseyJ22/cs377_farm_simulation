from graphics import *
import random
from time import sleep


class Farm:
	def __init__(self):
		self.window = GraphWin('Farm', 500, 500)
		self.mono = False
		self.pesticide = False
		self.fertilizer = False
		self.money = 0
		self.pond_health = 100
		self.algae_coverage = 1
		self.field_health = 100
		self.buttons = dict()
		self.window.autoflush = False
		self.buttons['mono_poly'] = [Point(325, 250), Point(500, 300)]
		self.buttons['pesticide'] = [Point(325, 300), Point(500, 350)]
		self.buttons['fertilizer'] = [Point(325, 350), Point(500, 400)]
		self.buttons['GO'] = [Point(325, 400), Point(500, 450)]


	def log_state(self):
		return 'FARM STATE \nPesticides applied: ' + str(self.pesticide) + '\nFertilizer applied: ' + str(self.fertilizer) + '\nMoney: $' + str(self.money) + '\nPond health: ' + str(self.pond_health) + '\nField health: ' + str(self.field_health) + '\nAlgae coverage: ' + str(self.algae_coverage)


	def run_round(self):
		self.display()
		self.make_choices()

		if self.mono:
			self.money += 200
			self.field_health -= 50
		else:
			self.money += 50
			self.field_health += 10


		if self.pesticide:
			self.money += 50
			self.field_health -= 20
			self.algae_coverage *= 2 # exponential


		if self.fertilizer:
			self.money += 50
			self.field_health += 20
			self.algae_coverage *= 2 # exponential


		if self.algae_coverage > 1:
			self.pond_health -= self.algae_coverage

		# field surviving is more likely if you use chemicals
		"""if self.fertilizer:
			if self.pesticide:
				self.field_health -= 50
				rand = 20
			else:
				rand = 15
		else:
			rand = 10

		if random.randint(0, rand) == 0:
			self.field_health = 0
			print('your field was wiped out by a weather event!')"""

		if self.field_health == 0:
			self.money -= 300

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
		elif self.in_button(click, self.buttons['mono_poly']):
			if self.mono:
				self.mono = False
			else:
				self.mono = True

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
		mono_poly = Rectangle(self.buttons['mono_poly'][0], self.buttons['mono_poly'][1])
		mono_poly.setFill('white')
		if self.mono:
			mono_poly_label = Text(Point(412, 275), 'Switch to Polyculture')
		else:
			mono_poly_label = Text(Point(412, 275), 'Switch to Monoculture')
		mono_poly.draw(self.window)
		mono_poly_label.draw(self.window)


		pesticide = Rectangle(self.buttons['pesticide'][0], self.buttons['pesticide'][1])
		pesticide.setFill('white')
		if self.pesticide:
			pesticide_label = Text(Point(412, 325), 'Do Not Apply Pesticides')
		else:
			pesticide_label = Text(Point(412, 325), 'Apply Pesticides')
		pesticide.draw(self.window)
		pesticide_label.draw(self.window)

		fertilizer = Rectangle(self.buttons['fertilizer'][0], self.buttons['fertilizer'][1])
		fertilizer.setFill('white')
		if self.fertilizer:
			fertilizer_label = Text(Point(412, 375), 'Do Not Apply Fertilizer')
		else:
			fertilizer_label = Text(Point(412, 375), 'Apply Fertilizer')
		fertilizer.draw(self.window)
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
		if self.pond_health > 0:
			pond.setFill('blue')
		else:
			pond.setFill('red')
		pond.draw(self.window)

		field = Rectangle(Point(25, 250), Point(275, 490))
		if self.field_health > 20:
			field.setFill('green')
		else:
			field.setFill('brown')
		field.draw(self.window)

		clear = Rectangle(Point(300, 5), Point(500, 150))
		clear.setFill('white')
		clear.draw(self.window)
		results = Text(Point(400, 75), farm.log_state())
		results.draw(self.window)


def conclusion(farm, win):
	background = Rectangle(Point(0, 0), Point(500, 500))
	background.setFill('white')
	background.draw(farm.window)
	if win:
		label = Text(Point(250, 50), 'YOU WIN!')
	else:
		label = Text(Point(250, 50), 'YOU LOSE!')

	label.draw(farm.window)

	results = Text(Point(100, 100), farm.log_state())
	results.draw(farm.window)

	message = Text(Point(400, 400), 'Click anywhere to quit.')
	message.draw(farm.window)

	farm.window.getMouse()
	farm.window.close()


farm = Farm()
for i in range(0, 5):
	print('ROUND', i)
	farm.run_round()
	if farm.field_health <= 0 and farm.money <= 300:
		conclusion(farm, win=False)
		break

if farm.pond_health > 0 and farm.money > 0 and farm.field_health > 0:
	conclusion(farm, win=True)
else:
	conclusion(farm, win=False)
