from graphics import *
import random
import time

#==================#
# HELPER FUNCTIONS #
#==================#

# Pauses the program for specified number of seconds without making the
# process sleep (which can interfere with garphics). Finest granularity
# is .2 seconds
def pause(seconds):
	start = time.perf_counter()
	while time.perf_counter() - start < seconds:
		res = 1000003007 * 1007000401

#==================#

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
				print('running round')
				year = Rectangle(Point(0, 0), Point(self.window.getWidth(), self.window.getHeight()))
				year.setFill('black')
				year.draw(self.window)

				text = Text(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'Running one year...')
				text.setStyle('bold')
				text.setFace('helvetica')
				text.setTextColor('white')
				text.setSize(20)
				text.draw(self.window)
				break

			self.handle_buttons(click)

		self.window.flush()


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
		text.setStyle('bold')
		text.setTextColor('white')
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

		self.show_status()


	def show_status(self):
		algae_percent = 0
		if self.algae_coverage >= 4:
			algae_percent = 25
		elif self.algae_coverage >= 8:
			algae_percent = 50
		elif self.algae_coverage >= 16:
			algae_percent = 100 
		state = 'FARM STATE \nPesticides applied: \nFertilizer applied: \nMoney: $' + str(self.money) + '\nPond health: \nField health: \nAlgae coverage: ' + str(algae_percent) + '%'

		text = Text(Point(110, 110), state)
		text.setFace('helvetica')
		text.setSize(20)
		text.draw(self.window)

		if self.pesticide:
			img = Image(Point(205, 65), 'checkmark_transparent.png')
		else:
			img = Image(Point(205, 65), 'x_transparent.png')
		img.draw(self.window)

		if self.fertilizer:
			img = Image(Point(200, 88), 'checkmark_transparent.png')
		else:
			img = Image(Point(200, 88), 'x_transparent.png')
		img.draw(self.window)

		health_background = Rectangle(Point(170, 125), Point(240, 140))
		health_background.draw(self.window)

		pond = Rectangle(Point(170, 125), Point(240, 140))
		print('pond health:', self.pond_health)
		if self.pond_health < 20:
			pond = Rectangle(Point(170, 125), Point(180, 140))
		elif self.pond_health < 50:
			pond = Rectangle(Point(170, 125), Point(200, 140))
		elif self.pond_health < 80:
			pond = Rectangle(Point(170, 125), Point(220, 140))

		pond.setFill('black')
		pond.draw(self.window)

		health_background = Rectangle(Point(170, 148), Point(240, 163))
		health_background.draw(self.window)

		field = Rectangle(Point(170, 148), Point(240, 163))
		print('field health:', self.field_health)
		if self.field_health < 20:
			field = Rectangle(Point(170, 148), Point(180, 163))
		elif self.field_health < 50:
			field = Rectangle(Point(170, 148), Point(200, 163))
		elif self.field_health < 80:
			field = Rectangle(Point(170, 148), Point(220, 163))

		field.setFill('black')
		field.draw(self.window)


def conclusion(farm, win):
	img = Image(Point(farm.window.getWidth()/2, farm.window.getHeight()/2), 'farm-empty.png')
	img.draw(farm.window)
	if win:
		label = Text(Point(farm.window.getWidth()/2, farm.window.getHeight()/2), 'YOU WIN!')
	else:
		label = Text(Point(farm.window.getWidth()/2, farm.window.getHeight()/2), 'YOU LOSE!')

	label.setSize(20)
	label.setFace('helvetica')
	label.setStyle('bold')
	label.draw(farm.window)

	message = Text(Point(1000, 800), 'Click anywhere to quit.')
	message.setSize(20)
	message.setFace('helvetica')
	message.setStyle('bold')
	message.draw(farm.window)

	farm.show_status()

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
