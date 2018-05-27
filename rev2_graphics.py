from graphics import *
import random
from time import sleep


class Farm:
	def __init__(self):
		self.window = GraphWin('Farm', 1500, 844)
		self.first_round = True
		self.mono = False
		self.pesticide = False
		self.fertilizer = False
		self.money = 0
		self.pond_health = 100
		self.algae_coverage = 1
		self.field_health = 100
		self.buttons = dict()
		self.window.autoflush = False
		# TODO: fix the dimensions here
		self.buttons['mono_poly'] = [Point(1150, 90), Point(1350, 200)]
		self.buttons['pesticide'] = [Point(700, 90), Point(800, 200)]
		self.buttons['fertilizer'] = [Point(950, 90), Point(1050, 200)]
		self.buttons['GO'] = [Point(950, 740), Point(1050, 780)]


	def log_state(self):
		return 'FARM STATE \nPesticides applied: ' + str(self.pesticide) + '\nFertilizer applied: ' + str(self.fertilizer) + '\nMoney: $' + str(self.money) + '\nPond health: ' + str(self.pond_health) + '\nField health: ' + str(self.field_health) + '\nAlgae coverage: ' + str(self.algae_coverage)


	def run_round(self):
		self.display()
		self.make_choices()

		self.first_round = False

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


		if self.field_health == 0:
			self.money -= 300


	def in_button(self, loc, button):
		if loc.getX() <= button[1].getX() and loc.getX() >= button[0].getX():
			if loc.getY() <= button[1].getY() and loc.getY() >= button[0].getY():
				return True

		return False


	def handle_buttons(self, click):
		if self.in_button(click, self.buttons['pesticide']):
			if self.pesticide:
				img = Image(Point(750, 130), 'pesticide.png')
				self.pesticide = False
				img.draw(self.window)
			else:
				img = Image(Point(750, 130), 'pesticide-selected.png')
				self.pesticide = True
				img.draw(self.window)

		elif self.in_button(click, self.buttons['fertilizer']):
			if self.fertilizer:
				img = Image(Point(1000, 130), 'fertilize.png')
				self.fertilizer = False
				img.draw(self.window)

			else:
				img = Image(Point(1000, 130), 'fertilize-selected.png')
				self.fertilizer = True
				img.draw(self.window)

		elif self.in_button(click, self.buttons['mono_poly']):
			if self.mono:
				img = Image(Point(1250, 130), 'mono.png')
				self.mono = False
				img.draw(self.window)

			else:
				img = Image(Point(1250, 130), 'poly.png')
				self.mono = True
				img.draw(self.window)


	def make_choices(self):
		while(True):
			click = self.window.getMouse()
			if self.in_button(click, self.buttons['GO']):
				print('breaking')
				break
			self.handle_buttons(click)

		self.window.flush()
		sleep(0.5)


	def draw_buttons(self):
		img = Image(Point(750, 130), 'pesticide.png')
		img.draw(self.window)

		text = Text(Point(750, 240), 'Pesticides will help your crops \n grow stronger, but will damage your \n land and pond in the long run.')
		text.setSize(16)
		text.setFace('helvetica')
		text.draw(self.window)

		img = Image(Point(1000, 130), 'fertilize.png')
		img.draw(self.window)

		text = Text(Point(1000, 240), 'Fertilizer will help your crops \n grow stronger, but could lead \n to an algae bloom in your pond.')
		text.setSize(16)
		text.setFace('helvetica')
		text.draw(self.window)

		img = Image(Point(1250, 130), 'poly.png')
		img.draw(self.window)

		text = Text(Point(1250, 240), 'Monoculture farming will earn \n more money, but will \n damage the land over time.')
		text.setSize(16)
		text.setFace('helvetica')
		text.draw(self.window)

		text = Text(Point(1000, 760), 'RUN ONE YEAR')
		text.setSize(25)
		text.setFace('helvetica')
		text.draw(self.window)


	def display(self):
		if self.first_round:
			img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'farm-empty.png')

		elif self.mono: # monoculture
			if self.pond_health > 50: # pond is healthy
				if self.field_health > 50: # field is healthy
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'mono-good.png')
				elif self.field_health < 20: # field is dead
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'mono-dead.png')
				else: # field is sick
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'mono-bad.png')
			else: # pond is sick
				if self.field_health > 50: # field is healthy
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'mono-algae.png')
				else: # field is sick
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'mono-bad-algae.png')
				# TODO: need an image for dead pond and dead field

		else: # polyculture
			if self.pond_health > 50: # pond is healthy
				if self.field_health > 50: # field is healthy
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'poly-good.png')
				elif self.field_health < 20: # field is dead
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'poly-dead.png')
				else: # field is sick
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'poly-bad.png')
			else: # pond is sick
				if self.field_health > 50: # field is healthy
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'poly-algae.png')
				else: # field is sick
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'poly-bad-algae.png')
				# TODO: need an image for dead pond and dead field

		img.draw(self.window)
		self.draw_buttons()


def conclusion(farm, win):
	background = Rectangle(Point(0, 0), Point(1500, 844))
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

	state = farm.log_state()
	print(state)
	text = Text(Point(400, 400), state)
	text.setFace('helvetica')
	text.setSize(20)
	text.draw(farm.window)

	if farm.field_health <= 0 and farm.money <= 300:
		conclusion(farm, win=False)
		break

if farm.pond_health > 0 and farm.money > 0 and farm.field_health > 0:
	conclusion(farm, win=True)
else:
	conclusion(farm, win=False)
