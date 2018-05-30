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
		self.mono = False
		self.pesticide = False
		self.fertilizer = False
		self.money = 0
		self.pond_health = 100
		self.algae_coverage = 1
		self.field_health = 100
		self.buttons = dict()
		self.window.autoflush = False
		self.buttons['mono_poly'] = [Point(1150, 90), Point(1350, 200)]
		self.buttons['pesticide'] = [Point(700, 90), Point(800, 200)]
		self.buttons['fertilizer'] = [Point(950, 90), Point(1050, 200)]
		self.buttons['GO'] = [Point(950, 740), Point(1050, 780)]
		self.summary = {'money':[], 'farm health':[], 'pond health':[], 'algae':[]}


	def log_state(self):
		return 'FARM STATE \nPesticides applied: ' + str(self.pesticide) + '\nFertilizer applied: ' + str(self.fertilizer) + '\nMoney: $' + str(self.money) + '\nPond health: ' + str(self.pond_health) + '\nField health: ' + str(self.field_health) + '\nAlgae coverage: ' + str(self.algae_coverage)


	def run_tutorial(self):
		img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'farm-empty.gif')
		img.draw(self.window)

		# monoculture or polyculture selection
		rectangle_dimensions = TODO
		rectangle = Rectangle(rectangle_dimensions)
		rectangle.draw(self.window)
		button = Image(TODO)
		button.draw(self.window)
		if self.in_button(rectangle_dimensions):
			if self.mono:
				img = Image(TODO, 'mono.gif')
				self.mono = False
				img.draw(self.window)

			else:
				img = Image(TODO, 'poly.gif')
				self.mono = True
				img.draw(self.window)


		# pesticide selection
		rectangle.draw(self.window)
		button = Image(TODO)
		button.draw(self.window)
		if self.in_button(rectangle_dimensions):
			if self.pesticide:
				img = Image(TODO, 'pesticide.gif')
				self.pesticide = False
				img.draw(self.window)

			else:
				img = Image(TODO, 'pesticide-selected.gif')
				self.pesticide = True
				img.draw(self.window)


		# fertilizer selection
		rectangle.draw(self.window)
		button = Image(TODO)
		button.draw(self.window)
		if self.in_button(rectangle_dimensions):
			if self.fertilizer:
				img = Image(TODO, 'fertilizer.gif')
				self.fertilizer = False
				img.draw(self.window)

			else:
				img = Image(TODO, 'fertilize-selected.gif')
				self.fertilizer = True
				img.draw(self.window)


		# run round
		rectangle.draw(self.window)
		button = Image(TODO)
		button.draw(self.window)
		if self.in_button(rectangle_dimensions):
			year = Rectangle(Point(0, 0), Point(self.window.getWidth(), self.window.getHeight()))
			year.setFill('black')
			year.draw(self.window)

			text = Text(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'Running one year...')
			text.setStyle('bold')
			text.setFace('helvetica')
			text.setTextColor('white')
			text.setSize(20)
			text.draw(self.window)
			self.window.flush()

		self.run_year()
		self.display_summary()


	def run_year(self):
		self.money -= 100 # do this no matter what
		self.summary['money'].append('decreased by $100')

		if self.mono:
			self.summary['money'].append('increased by $300 because of monoculture')
			self.money += 300
			self.summary['field health'].append('declined by 50% because of monoculture')
			self.field_health -= 50
		else:
			self.summary['money'].append('increased by $100 because of polyculture')
			self.money += 100 # if you just do polyculture without fertilizer you will break even
			self.summary['field health'].append('increased by 10% because of polyculture')
			self.field_health += 10


		if self.pesticide:
			self.summary['money'].append('increased by $50 because of pesticide use')
			self.money += 50
			self.summary['field health'].append('declined by 20% because of pesticide use')
			self.field_health -= 20
			self.summary['algae'].append('coverage increased by 50% because of pesticide use')
			self.algae_coverage *= 2 # exponential


		if self.fertilizer:
			self.summary['money'].append('increased by $50 because of fertilizer use')
			self.money += 50
			self.summary['field health'].append('increased by 20% because of fertilizer use')
			self.field_health += 20
			self.summary['algae'].append('coverage increased by 50% because of fertilizer use')
			self.algae_coverage *= 2 # exponential


		if self.algae_coverage > 1:
			self.summary['pond health'].append('declined because of an algae bloom')
			self.pond_health -= self.algae_coverage


		if self.field_health == 0:
			self.money -= 300
			self.summary['money'].append('decreased by $300 because your land died and had to be replaced')


	def run_round(self):
		self.display()
		self.make_choices()
		self.run_year()
		self.display_summary()


	def display_summary(self):
		background = Rectangle(TODO)
		background.draw(self.window)
		text = ''
		for key in self.summary:
			text += key + ':'
			for info in self.summary[key]:
				text += info + '\n'
			text += '\n'

		message = Text(TODO, text)
		message.setSize(15)
		message.setStyle('helvetica')
		message.draw(self.window)

		self.summary = {'money':[], 'farm health':[], 'pond health':[], 'algae':[]} # reset for next round
		
		message = Text(TODO, 'Click anywhere to continue.')
		message.setSize(20)
		message.setFace('helvetica')
		message.setStyle('bold')
		message.draw(self.window)

		self.window.getMouse()
		self.window.close()


	def in_button(self, loc, button):
		if loc.getX() <= button[1].getX() and loc.getX() >= button[0].getX():
			if loc.getY() <= button[1].getY() and loc.getY() >= button[0].getY():
				return True

		return False


	def handle_buttons(self, click):
		if self.in_button(click, self.buttons['pesticide']):
			if self.pesticide:
				img = Image(Point(750, 130), 'pesticide.gif')
				self.pesticide = False
				img.draw(self.window)
			else:
				img = Image(Point(750, 130), 'pesticide-selected.gif')
				self.pesticide = True
				img.draw(self.window)

		elif self.in_button(click, self.buttons['fertilizer']):
			if self.fertilizer:
				img = Image(Point(1000, 130), 'fertilize.gif')
				self.fertilizer = False
				img.draw(self.window)

			else:
				img = Image(Point(1000, 130), 'fertilize-selected.gif')
				self.fertilizer = True
				img.draw(self.window)

		elif self.in_button(click, self.buttons['mono_poly']):
			if self.mono:
				img = Image(Point(1250, 130), 'mono.gif')
				self.mono = False
				img.draw(self.window)

			else:
				img = Image(Point(1250, 130), 'poly.gif')
				self.mono = True
				img.draw(self.window)


	def make_choices(self):
		while(True):
			click = self.window.getMouse()
			if self.in_button(click, self.buttons['GO']):
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
		img = Image(Point(750, 130), 'pesticide.gif')
		img.draw(self.window)

		text = Text(Point(750, 240), 'Pesticides will help your crops \n grow stronger, but will damage your \n land and pond in the long run.')
		text.setSize(16)
		text.setFace('helvetica')
		text.draw(self.window)

		img = Image(Point(1000, 130), 'fertilize.gif')
		img.draw(self.window)

		text = Text(Point(1000, 240), 'Fertilizer will help your crops \n grow stronger, but could lead \n to an algae bloom in your pond.')
		text.setSize(16)
		text.setFace('helvetica')
		text.draw(self.window)

		img = Image(Point(1250, 130), 'poly.gif')
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
		if self.mono: # monoculture
			if self.pond_health > 50: # pond is healthy
				if self.field_health > 50: # field is healthy
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'mono-good.gif')
				elif self.field_health < 20: # field is dead
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'mono-dead.gif')
				else: # field is sick
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'mono-bad.gif')
			else: # pond is sick
				if self.field_health > 50: # field is healthy
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'mono-algae.gif')
				else: # field is sick
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'mono-bad-algae.gif')

		else: # polyculture
			if self.pond_health > 50: # pond is healthy
				if self.field_health > 50: # field is healthy
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'poly-good.gif')
				elif self.field_health < 20: # field is dead
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'poly-dead.gif')
				else: # field is sick
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'poly-bad.gif')
			else: # pond is sick
				if self.field_health > 50: # field is healthy
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'poly-algae.gif')
				else: # field is sick
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'poly-bad-algae.gif')

		img.draw(self.window)
		self.draw_buttons()

		self.show_status()


	def show_status(self):
		background = Rectangle(Point(50, 50), Point(300, 300)) # TODO these locations aren't right
		background.draw(self.window)

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
			img = Image(Point(205, 65), 'checkmark_transparent.gif')
		else:
			img = Image(Point(205, 65), 'x_transparent.gif')
		img.draw(self.window)

		if self.fertilizer:
			img = Image(Point(200, 88), 'checkmark_transparent.gif')
		else:
			img = Image(Point(200, 88), 'x_transparent.gif')
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
	img = Image(Point(farm.window.getWidth()/2, farm.window.getHeight()/2), 'farm-empty.gif')
	img.draw(farm.window)
	if win:
		label = Text(Point(farm.window.getWidth()/2, farm.window.getHeight()/2), 'YOU WIN!')
	else:
		label = Text(Point(farm.window.getWidth()/2, farm.window.getHeight()/2), 'YOU LOSE!')

	label.setSize(20)
	label.setFace('helvetica')
	label.setStyle('bold')
	label.draw(farm.window)

	message = Text(Point(1000, 800), 'Click anywhere to restart simulation.')
	message.setSize(20)
	message.setFace('helvetica')
	message.setStyle('bold')
	message.draw(farm.window)

	farm.show_status()

	farm.window.getMouse()
	farm.window.close()


while(True):
	farm = Farm()
	farm.run_tutorial()
	for i in range(0, 4):
		print('ROUND', i)
		farm.run_round()

		if farm.field_health <= 0 and farm.money <= 300:
			conclusion(farm, win=False)
			break

	if farm.pond_health > 0 and farm.money > 0 and farm.field_health > 0:
		conclusion(farm, win=True)
	else:
		conclusion(farm, win=False)
