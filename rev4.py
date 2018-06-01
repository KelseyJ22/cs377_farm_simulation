from graphics import *
import random
import time

#==================#
# HELPER FUNCTIONS #
#==================#

# Pauses the program for specified number of seconds without making the
# process sleep (which can interfere with graphics). Finest granularity
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
		self.buttons['GO'] = [Point(600, 750), Point(1400, 850)]
		self.summary = {'money':[[], 0], 'field health':[[], 0], 'pond health':[[], 0], 'algae':[[], 1]}


	def log_state(self):
		return 'FARM STATE \nPesticides applied: ' + str(self.pesticide) + '\nFertilizer applied: ' + str(self.fertilizer) + '\nMoney: $' + str(self.money) + '\nPond health: ' + str(self.pond_health) + '\nField health: ' + str(self.field_health) + '\nAlgae coverage: ' + str(self.algae_coverage)


	def run_tutorial(self):
		img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/farm-empty.gif')
		img.draw(self.window)

		# monoculture or polyculture selection
		rectangle_dimensions = [Point(self.window.getWidth()/2-260, self.window.getHeight()/2-150), Point(self.window.getWidth()/2+260, self.window.getHeight()/2+150)]
		rectangle = Rectangle(rectangle_dimensions[0], rectangle_dimensions[1])
		rectangle.setFill('white')
		rectangle.setOutline('white')
		rectangle.draw(self.window)
		mono = Image(Point(self.window.getWidth()/2-120, self.window.getHeight()/2-50), 'gif/mono.gif')
		mono.draw(self.window)

		text = Text(Point(self.window.getWidth()/2-120, self.window.getHeight()/2+50), 'Monoculture')
		text.setSize(16)
		text.setFace('helvetica')
		text.draw(self.window)

		poly = Image(Point(self.window.getWidth()/2+120, self.window.getHeight()/2-50), 'gif/poly.gif')
		poly.draw(self.window)
		text = Text(Point(self.window.getWidth()/2+120, self.window.getHeight()/2+50), 'Polyculture')
		text.setSize(14)
		text.setFace('helvetica')
		text.draw(self.window)
		
		text = Text(Point(self.window.getWidth()/2, self.window.getHeight()/2+100), 'Monoculture farming will earn \n more money, but will \n damage the land over time.')
		text.setSize(14)
		text.setFace('helvetica')
		text.draw(self.window)
		while(True):
			click = self.window.getMouse()
			if self.in_button(click, [Point(self.window.getWidth()/2-150, self.window.getHeight()/2-100), Point(self.window.getWidth()/2-50, self.window.getHeight()/2+50)]):
				self.mono = True
				break
			elif self.in_button(click, [Point(self.window.getWidth()/2+50, self.window.getHeight()/2-100), Point(self.window.getWidth()/2+150, self.window.getHeight()/2+50)]):
				self.mono = False
				break

		# pesticide selection
		rectangle = Rectangle(rectangle_dimensions[0], rectangle_dimensions[1])
		rectangle.setFill('white')
		rectangle.setOutline('white')
		rectangle.draw(self.window)
		pest_yes = Image(Point(self.window.getWidth()/2-110, self.window.getHeight()/2-50), 'gif/pest-yes.gif')
		pest_yes.draw(self.window)
		text = Text(Point(self.window.getWidth()/2-110, self.window.getHeight()/2+50), 'Apply Pesticides')
		text.setSize(14)
		text.setFace('helvetica')
		text.draw(self.window)

		pest_no = Image(Point(self.window.getWidth()/2+110, self.window.getHeight()/2-50), 'gif/pest-no.gif')
		pest_no.draw(self.window)
		text = Text(Point(self.window.getWidth()/2+110, self.window.getHeight()/2+50), "Don't Apply Pesticides")
		text.setSize(14)
		text.setFace('helvetica')
		text.draw(self.window)

		text = Text(Point(self.window.getWidth()/2, self.window.getHeight()/2+100), 'Pesticides will help your crops \n grow stronger, but will damage your \n land and pond in the long run.')
		text.setSize(16)
		text.setFace('helvetica')
		text.draw(self.window)
		while(True):
			click = self.window.getMouse()
			if self.in_button(click, [Point(self.window.getWidth()/2-150, self.window.getHeight()/2-100), Point(self.window.getWidth()/2-50, self.window.getHeight()/2+50)]):
				self.pesticide = True
				break
			elif self.in_button(click, [Point(self.window.getWidth()/2+50, self.window.getHeight()/2-100), Point(self.window.getWidth()/2+150, self.window.getHeight()/2+50)]):
				self.pesticide = False
				break


		# fertilizer selection
		rectangle = Rectangle(rectangle_dimensions[0], rectangle_dimensions[1])
		rectangle.setFill('white')
		rectangle.setOutline('white')
		rectangle.draw(self.window)
		fert_yes = Image(Point(self.window.getWidth()/2-110, self.window.getHeight()/2-50), 'gif/fert-yes.gif')
		fert_yes.draw(self.window)
		text = Text(Point(self.window.getWidth()/2-110, self.window.getHeight()/2+50), 'Fertilize')
		text.setSize(14)
		text.setFace('helvetica')
		text.draw(self.window)

		fert_no = Image(Point(self.window.getWidth()/2+110, self.window.getHeight()/2-50), 'gif/fert-no.gif')
		fert_no.draw(self.window)
		text = Text(Point(self.window.getWidth()/2+110, self.window.getHeight()/2+50), "Don't Fertilize")
		text.setSize(14)
		text.setFace('helvetica')
		text.draw(self.window)
		
		text = Text(Point(self.window.getWidth()/2, self.window.getHeight()/2+100), 'Fertilizer will help your crops \n grow stronger, but could lead \n to an algae bloom in your pond.')
		text.setSize(16)
		text.setFace('helvetica')
		text.draw(self.window)
		while(True):
			click = self.window.getMouse()
			if self.in_button(click, [Point(self.window.getWidth()/2-150, self.window.getHeight()/2-100), Point(self.window.getWidth()/2-50, self.window.getHeight()/2+50)]):
				self.pesticide = True
				break
			elif self.in_button(click, [Point(self.window.getWidth()/2+50, self.window.getHeight()/2-100), Point(self.window.getWidth()/2+150, self.window.getHeight()/2+50)]):
				self.pesticide = False
				break


		# run round
		img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/farm-empty.gif')
		img.draw(self.window)
		button = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/run_button.gif')
		button.draw(self.window)
		while(True):
			click = self.window.getMouse()
			if self.in_button(click, [Point(self.window.getWidth()/2-260, self.window.getHeight()/2-50), Point(self.window.getWidth()/2+260, self.window.getHeight()/2+50)]):
				break

		self.run_year()
		self.display_summary()


	def run_year(self):
		self.money -= 100 # do this no matter what
		self.summary['money'][0].append('Decreased by $100 (your annual expenses)')
		self.summary['money'][1] -= 100

		if self.mono:
			self.summary['money'][0].append('Increased by $300 because monoculture farming has high financia returns')
			self.money += 300
			self.summary['money'][1] += 300
			self.summary['field health'][0].append('Declined by 50% because monoculture extracts nutrients from the soil')
			self.field_health -= 50
			self.summary['field health'][1] -= 50

		else:
			self.summary['money'][0].append('Increased by $100 because polyculture farming is less productive')
			self.money += 100 # if you just do polyculture without fertilizer you will break even
			self.summary['field health'][0].append('Increased by 10% because polyculture helps cultivate healthy soil')
			self.field_health += 10
			self.summary['field health'][1] += 10

		if self.pesticide:
			self.summary['money'][0].append('Increased by $50 because pesticides kill bugs and increase productivity')
			self.money += 50
			self.summary['money'][1] += 50
			self.summary['field health'][0].append('Declined by 20% because pesticides poison valuable insects as well as pests')
			self.field_health -= 20
			self.summary['field health'][1] -= 20
			self.summary['algae'][0].append('Coverage increased by 50% because pesticides disrupt the balance of the ecosystem')
			self.algae_coverage *= 2 # exponential
			self.summary['algae'][1] *= 2

		if self.fertilizer:
			self.summary['money'][0].append('Increased by $50 because fertilizer increases the productivity of your farm')
			self.money += 50
			self.summary['money'][1] += 50
			self.summary['field health'][0].append('Increased by 20% because fertilizer increases the nutrients in your soil')
			self.field_health += 20
			self.summary['field health'][1] += 20
			self.summary['algae'][0].append('Coverage increased by 50% because fertilizer runoff feeds algae growth')
			self.algae_coverage *= 2 # exponential
			self.summary['algae'][1] *= 2

		if self.algae_coverage > 1:
			self.summary['pond health'][0].append('Declined because of an algae bloom')
			self.pond_health -= self.algae_coverage
			self.summary['pond health'][1] -= self.algae_coverage

		if self.field_health <= 0:
			self.money -= 300
			self.summary['money'][1] -= 300
			self.summary['money'][0].append('Decreased by $300 because your soil failed and had to be replaced')

		if self.field_health > 100:
			self.field_health = 100
		if self.pond_health <= 0:
			self.pond_health = 0 # prevent from going negative
			self.summary['pond health'][0].append('Your pond died due to algae overgrowth, suffocating other plants and starving the animals that depended on them')


	def run_round(self):
		self.display()
		self.make_choices()
		self.run_year()
		self.display_summary()


	def display_summary(self):
		background = Rectangle(Point(self.window.getWidth()/2-400, self.window.getHeight()/2-400), Point(self.window.getWidth()/2+400, self.window.getHeight()/2+400))
		background.setFill('white')
		background.setOutline('white')
		background.draw(self.window)
		text = ''
		for key in self.summary:
			if key == 'field health' or key == 'pond health' or key == 'algae':
				text += key.upper() + ': ' + str(self.summary[key][1]) + '%\n'
			elif key == 'money':
				text += key.upper() + ': $' + str(self.summary[key][1]) + '\n'

			if len(self.summary[key][0]) == 0:
				text += 'No change this iteration\n'
			else:
				for info in self.summary[key][0]:
					text += info + '\n'
			text += '\n'

		message = Text(Point(self.window.getWidth()/2, self.window.getHeight()/2), text)
		message.setSize(20)
		message.setFace('helvetica')
		message.draw(self.window)

		self.summary = {'money':[[], 0], 'field health':[[], 0], 'pond health':[[], 0], 'algae':[[], 1]} # reset for next round
		
		message = Text(Point(self.window.getWidth()/2, 800), 'Click anywhere to continue.')
		message.setSize(30)
		message.setFace('helvetica')
		message.setStyle('bold')
		message.draw(self.window)

		self.window.getMouse()


	def in_button(self, loc, button):
		if loc.getX() <= button[1].getX() and loc.getX() >= button[0].getX():
			if loc.getY() <= button[1].getY() and loc.getY() >= button[0].getY():
				return True

		return False


	def handle_buttons(self, click):
		if self.in_button(click, self.buttons['pesticide']):
			if self.pesticide:
				background = Rectangle(Point(650, 30), Point(900, 210))
				background.setFill('white')
				background.setOutline('white')
				background.draw(self.window)

				img = Image(Point(750, 130), 'gif/pest-no.gif')
				self.pesticide = False
				img.draw(self.window)
			else:
				background = Rectangle(Point(650, 30), Point(900, 210))
				background.setFill('white')
				background.setOutline('white')
				background.draw(self.window)

				img = Image(Point(750, 130), 'gif/pest-yes.gif')
				self.pesticide = True
				img.draw(self.window)

		elif self.in_button(click, self.buttons['fertilizer']):
			if self.fertilizer:
				background = Rectangle(Point(900, 30), Point(1100, 210))
				background.setFill('white')
				background.setOutline('white')
				background.draw(self.window)
				img = Image(Point(1000, 130), 'gif/fert-no.gif')
				self.fertilizer = False
				img.draw(self.window)
			else:
				background = Rectangle(Point(900, 30), Point(1100, 210))
				background.setFill('white')
				background.setOutline('white')
				background.draw(self.window)
				img = Image(Point(1000, 130), 'gif/fert-yes.gif')
				self.fertilizer = True
				img.draw(self.window)

		elif self.in_button(click, self.buttons['mono_poly']):
			if self.mono:
				background = Rectangle(Point(1100, 30), Point(1400, 210))
				background.setFill('white')
				background.setOutline('white')
				background.draw(self.window)
				img = Image(Point(1250, 130), 'gif/poly.gif')
				self.mono = False
				img.draw(self.window)
			else:
				background = Rectangle(Point(1100, 30), Point(1400, 210))
				background.setFill('white')
				background.setOutline('white')
				background.draw(self.window)
				img = Image(Point(1250, 130), 'gif/mono.gif')
				self.mono = True
				img.draw(self.window)


	def make_choices(self):
		while(True):
			click = self.window.getMouse()
			if self.in_button(click, self.buttons['GO']):
				break

			self.handle_buttons(click)

		self.window.flush()


	def draw_buttons(self):
		background = Rectangle(Point(600, 30), Point(1400, 300))
		background.setFill('white')
		background.setOutline('white')
		background.draw(self.window)

		if self.pesticide:
			img = Image(Point(750, 130), 'gif/pest-yes.gif')
		else:
			img = Image(Point(750, 130), 'gif/pest-no.gif')
		img.draw(self.window)

		text = Text(Point(750, 240), 'Pesticides will help your crops \n grow stronger, but will damage your \n land and pond in the long run.')
		text.setSize(16)
		text.setFace('helvetica')
		text.draw(self.window)

		if self.fertilizer:
			img = Image(Point(1000, 130), 'gif/fert-yes.gif')
		else:
			img = Image(Point(1000, 130), 'gif/fert-no.gif')
		img.draw(self.window)

		text = Text(Point(1000, 240), 'Fertilizer will help your crops \n grow stronger, but could lead \n to an algae bloom in your pond.')
		text.setSize(16)
		text.setFace('helvetica')
		text.draw(self.window)

		if self.mono:
			img = Image(Point(1250, 130), 'gif/mono.gif')
		else:
			img = Image(Point(1250, 130), 'gif/poly.gif')
		img.draw(self.window)

		text = Text(Point(1250, 240), 'Monoculture farming will earn \n more money, but will \n damage the land over time.')
		text.setSize(16)
		text.setFace('helvetica')
		text.draw(self.window)

		img = Image(Point(1000, 790), 'gif/run_button.gif')
		img.draw(self.window)


	def display(self):
		if self.mono: # monoculture
			if self.pond_health > 50: # pond is healthy
				if self.field_health > 50: # field is healthy
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/mono-good.gif')
				elif self.field_health < 20: # field is dead
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/mono-dead.gif')
				else: # field is sick
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/mono-bad.gif')
			elif self.pond_health > 20 and self.pond_health < 50:
				if self.field_health > 50: # field is healthy
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/2.gif')
				elif self.field_health < 20: # field is dead
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/5.gif')
				else: # field is sick
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/5.gif')
			else: # pond is very sick
				if self.field_health > 50: # field is healthy
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/mono-algae.gif')
				else: # field is sick
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/mono-bad-algae.gif')

		else: # polyculture
			if self.pond_health > 50: # pond is healthy
				if self.field_health > 50: # field is healthy
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/poly-good.gif')
				elif self.field_health < 20: # field is dead
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/poly-dead.gif')
				else: # field is sick
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/poly-bad.gif')
			elif self.pond_health > 20 and self.pond_health < 50: # pond is sick
				if self.field_health > 50: # field is healthy
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/8.gif')
				elif self.field_health < 20: # field is dead
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/6.gif')
				else: # field is sick
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/7.gif')
			else: # pond is very sick
				if self.field_health > 50: # field is healthy
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/poly-algae.gif')
				else: # field is sick
					img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/poly-bad-algae.gif')

		img.draw(self.window)
		self.draw_buttons()

		self.show_status()


	def show_status(self):
		background = Rectangle(Point(0, 0), Point(250, 250))
		background.setFill('white')
		background.setOutline('white')
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
			img = Image(Point(205, 65), 'gif/checkmark_transparent.gif')
		else:
			img = Image(Point(205, 65), 'gif/x_transparent.gif')
		img.draw(self.window)

		if self.fertilizer:
			img = Image(Point(200, 88), 'gif/checkmark_transparent.gif')
		else:
			img = Image(Point(200, 88), 'gif/x_transparent.gif')
		img.draw(self.window)

		health_background = Rectangle(Point(170, 125), Point(240, 140))
		health_background.draw(self.window)

		pond = Rectangle(Point(170, 125), Point(240, 140))
		
		limit = self.pond_health/100.0 * 70
		pond = Rectangle(Point(170, 125), Point(170 + int(limit), 140))
		pond.setFill('green')
		pond.setOutline('green')
		
		if self.pond_health < 25:
			pond.setFill('red')
			pond.setOutline('red')
		elif self.pond_health < 50:
			pond.setFill('yellow')
			pond.setOutline('yellow')
			

		pond.draw(self.window)

		health_background = Rectangle(Point(170, 148), Point(240, 163))
		health_background.draw(self.window)

		field = Rectangle(Point(170, 148), Point(240, 163))
		limit = self.field_health/100.0 * 70
		field = Rectangle(Point(170, 148), Point(170 + int(limit), 163))
		field.setFill('green')
		field.setOutline('green')
		if self.field_health < 25:
			field.setFill('red')
			field.setOutline('red')
		elif self.field_health < 50:
			field.setFill('yellow')
			field.setOutline('yellow')

		field.draw(self.window)


def conclusion(farm, win):
	img = Image(Point(farm.window.getWidth()/2, farm.window.getHeight()/2), 'gif/farm-empty.gif')
	img.draw(farm.window)
	rectangle = Rectangle(Point(farm.window.getWidth()/2-100, farm.window.getHeight()/2-100), Point(farm.window.getWidth()/2+100, farm.window.getHeight()/2+100))
	rectangle.setFill('white')
	rectangle.draw(farm.window)
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
