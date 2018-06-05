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
		self.buttons['mono_poly'] = [Point(1200, 70), Point(1400, 170)]
		self.buttons['pesticide'] = [Point(750, 70), Point(850, 170)]
		self.buttons['fertilizer'] = [Point(1000, 70), Point(1100, 170)]
		self.buttons['GO'] = [Point(600, 750), Point(1400, 850)]
		self.summary = {'money':[[], 0], 'field health':[[], 0], 'pond health':[[], 0], 'algae':[[], 1]}
		self.year = 0
		self.button_bkgd_x = 700
		self.button_bkgd_y = 0
		self.button_bkgd_width = 800
		self.button_bkgd_height = 250
		self.button_bkgd_margin = 20
		self.button_width = 240
		self.button_height = 150
		self.button_x_center = self.button_width / 2
		self.img_y_center = self.button_bkgd_margin + 70
		self.txt_y_center = self.button_bkgd_margin + 180


	def log_state(self):
		return 'FARM STATE \nPesticides applied: ' + str(self.pesticide) + '\nFertilizer applied: ' + str(self.fertilizer) + '\nMoney: $' + str(self.money) + '\nPond health: ' + str(self.pond_health) + '\nField health: ' + str(self.field_health) + '\nAlgae coverage: ' + str(self.algae_coverage)


	def run_tutorial(self):
		img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/farm-empty.gif')
		img.draw(self.window)

		intro = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/signs/intro.gif')
		intro.draw(self.window)

		continue_button = Image(Point(self.window.getWidth()/2, 650), 'gif/continue.gif')
		continue_button.draw(self.window)

		while(True):
			click = self.window.getMouse()
			if self.in_button(click, [Point(self.window.getWidth()/2 - 150, 650 - 37), Point(self.window.getWidth()/2 + 150, 650 + 37)]):
				break

		# choose farm style
		img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/farm-empty.gif')
		img.draw(self.window)

		mono_poly = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/signs/farm-style.gif')
		mono_poly.draw(self.window)

		continue_button = Image(Point(self.window.getWidth()/2-10, 750), 'gif/mini_continue.gif')
		continue_button.draw(self.window)

		while(True):
			click = self.window.getMouse()
			if self.in_button(click, [Point(440, 190), Point(610, 370)]):
				self.mono = True
				mono_poly = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/signs/farm-style.gif')
				mono_poly.draw(self.window)

				continue_button = Image(Point(self.window.getWidth()/2-10, 750), 'gif/mini_continue.gif')
				continue_button.draw(self.window)

				mono = Image(Point(self.window.getWidth()/2-221, self.window.getHeight()/2-150), 'gif/mono-selected.gif')
				mono.draw(self.window)	
				
			elif self.in_button(click, [Point(840, 190), Point(1005, 370)]):
				self.mono = False
				mono_poly = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/signs/farm-style.gif')
				mono_poly.draw(self.window)

				continue_button = Image(Point(self.window.getWidth()/2-10, 750), 'gif/mini_continue.gif')
				continue_button.draw(self.window)

				mono = Image(Point(self.window.getWidth()/2+170, self.window.getHeight()/2-150), 'gif/poly-selected.gif')
				mono.draw(self.window)

			elif self.in_button(click, [Point(self.window.getWidth()/2 - 60, 750 - 10), Point(self.window.getWidth()/2 + 50, 750 + 10)]):
				break
		
		# choose fertilizer
		img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/farm-empty.gif')
		img.draw(self.window)

		fertilizer = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/signs/fertilizers.gif')
		fertilizer.draw(self.window)	

		continue_button = Image(Point(self.window.getWidth()/2-10, 750), 'gif/mini_continue.gif')
		continue_button.draw(self.window)

		while(True):
			click = self.window.getMouse()
			if self.in_button(click, [Point(440, 190), Point(610, 370)]):
				self.fertilizer = True
				fertilizer = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/signs/fertilizers.gif')
				fertilizer.draw(self.window)	

				continue_button = Image(Point(self.window.getWidth()/2-10, 750), 'gif/mini_continue.gif')
				continue_button.draw(self.window)
				fert = Image(Point(self.window.getWidth()/2-200, self.window.getHeight()/2-140), 'gif/yes-fert-selected.gif')
				fert.draw(self.window)
				
			elif self.in_button(click, [Point(840, 190), Point(1005, 370)]):
				self.fertilizer = False
				fertilizer = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/signs/fertilizers.gif')
				fertilizer.draw(self.window)	

				continue_button = Image(Point(self.window.getWidth()/2-10, 750), 'gif/mini_continue.gif')
				continue_button.draw(self.window)
				fert = Image(Point(self.window.getWidth()/2+200, self.window.getHeight()/2-140), 'gif/no-fert-selected.gif')
				fert.draw(self.window)
				
			elif self.in_button(click, [Point(self.window.getWidth()/2 - 60, 750 - 10), Point(self.window.getWidth()/2 + 50, 750 + 10)]):
				break

		# choose pesticides
		img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/farm-empty.gif')
		img.draw(self.window)

		pesticide = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/signs/pesticides.gif')
		pesticide.draw(self.window)	

		continue_button = Image(Point(self.window.getWidth()/2-10, 750), 'gif/mini_continue.gif')
		continue_button.draw(self.window)
		
		while(True):
			click = self.window.getMouse()
			if self.in_button(click, [Point(440, 190), Point(610, 370)]):
				self.pesticide = True
				pesticide = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/signs/pesticides.gif')
				pesticide.draw(self.window)	

				continue_button = Image(Point(self.window.getWidth()/2-10, 750), 'gif/mini_continue.gif')
				continue_button.draw(self.window)
		
				pest = Image(Point(self.window.getWidth()/2-210, self.window.getHeight()/2-140), 'gif/yes-pest-selected.gif')
				pest.draw(self.window)
				
			elif self.in_button(click, [Point(840, 190), Point(1005, 370)]):
				self.pesticide = False
				pesticide = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/signs/pesticides.gif')
				pesticide.draw(self.window)	

				continue_button = Image(Point(self.window.getWidth()/2-10, 750), 'gif/mini_continue.gif')
				continue_button.draw(self.window)
		
				pest = Image(Point(self.window.getWidth()/2+190, self.window.getHeight()/2-140), 'gif/no-pest-selected.gif')
				pest.draw(self.window)

			elif self.in_button(click, [Point(self.window.getWidth()/2 - 60, 750 - 10), Point(self.window.getWidth()/2 + 50, 750 + 10)]):
				break

		# run round
		img = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/farm-empty.gif')
		img.draw(self.window)

		run = Image(Point(self.window.getWidth()/2, self.window.getHeight()/2), 'gif/run_button.gif')
		run.draw(self.window)

		while(True):
			click = self.window.getMouse()
			if self.in_button(click, [Point(self.window.getWidth()/2-260, self.window.getHeight()/2-50), Point(self.window.getWidth()/2+260, self.window.getHeight()/2+50)]):
				break

		self.year += 1
		self.run_year()
		self.display_summary()


	def run_year(self):
		self.money -= 100 # do this no matter what
		self.summary['money'][0].append('Decreased by $100 (your annual expenses)')
		self.summary['money'][1] -= 100

		if self.mono:
			self.summary['money'][0].append('Increased by $150 because monoculture farming has high financia returns')
			self.money += 150
			self.summary['money'][1] += 150
			self.summary['field health'][0].append('Declined by 50% because monoculture extracts nutrients from the soil')
			self.field_health -= 50
			self.summary['field health'][1] -= 50

		else:
			self.summary['money'][0].append('Increased by $50 because polyculture farming is less productive')
			self.money += 50
			self.summary['money'][1] += 50
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
			self.summary['algae'][0].append('Coverage increased by 2x because pesticides disrupt the ecosystem')
			self.algae_coverage *= 2 # exponential
			self.summary['algae'][1] *= 2

		if self.fertilizer:
			self.summary['money'][0].append('Increased by $50 because fertilizer increases the productivity of your farm')
			self.money += 50
			self.summary['money'][1] += 50
			self.summary['field health'][0].append('Increased by 20% because fertilizer increases the nutrients in your soil')
			self.field_health += 20
			self.summary['field health'][1] += 20
			self.summary['algae'][0].append('Coverage increased by 2x because fertilizer runoff feeds algae growth')
			self.algae_coverage *= 2 # exponential
			self.summary['algae'][1] *= 2

		if self.algae_coverage > 1:
			if self.pesticide or self.fertilizer: # stop hurting the pond if you improve your practices
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
			if key == 'field health' or key == 'pond health':
				text += key.upper() + ': ' + str(self.summary[key][1]) + '%\n'
			elif key == 'money':
				text += key.upper() + ': $' + str(self.summary[key][1]) + '\n'
			elif key == 'algae':
				text += key.upper() + ': a factor of ' + str(self.summary[key][1]) + '\n'

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
		
		message = Text(Point(self.window.getWidth()/2, 700), 'Click anywhere to continue.')
		message.setSize(20)
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
		button_x_init = self.button_bkgd_x + self.button_bkgd_margin
		button_y = self.button_bkgd_margin
		if self.in_button(click, self.buttons['pesticide']):
			button_x = button_x_init
			background = Rectangle(Point(button_x, button_y), Point(button_x + self.button_width, button_y + self.button_height))
			background.setFill('white')
			background.setOutline('white')
			background.draw(self.window)
			if self.pesticide:
				img = Image(Point(button_x + self.button_x_center, self.img_y_center), 'gif/pest-no.gif')
				self.pesticide = False
			else:
				img = Image(Point(button_x + self.button_x_center, self.img_y_center), 'gif/pest-yes.gif')
				self.pesticide = True
			img.draw(self.window)

		elif self.in_button(click, self.buttons['fertilizer']):
			button_x = button_x_init + 1 * self.button_width
			background = Rectangle(Point(button_x, button_y), Point(button_x + self.button_width, button_y + self.button_height))
			background.setFill('white')
			background.setOutline('white')
			background.draw(self.window)
			if self.fertilizer:
				img = Image(Point(button_x + self.button_x_center, self.img_y_center), 'gif/fert-no.gif')
				self.fertilizer = False
			else:
				img = Image(Point(button_x + self.button_x_center, self.img_y_center), 'gif/fert-yes.gif')
				self.fertilizer = True
			img.draw(self.window)

		elif self.in_button(click, self.buttons['mono_poly']):
			button_x = button_x_init + 2 * self.button_width
			background = Rectangle(Point(button_x, button_y), Point(button_x + self.button_width, button_y + self.button_height + 60))
			background.setFill('white')
			background.setOutline('white')
			background.draw(self.window)

			text = Text(Point(button_x + self.button_x_center, self.txt_y_center), 'Polyculture farming will earn \n less money, but will \n take care of the land.')
			text.setSize(16)
			text.setFace('helvetica')
			text.draw(self.window)

			if self.mono:
				img = Image(Point(button_x + self.button_x_center, self.img_y_center), 'gif/poly.gif')
				self.mono = False
			else:
				img = Image(Point(button_x + self.button_x_center, self.img_y_center), 'gif/mono.gif')
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
		background = Rectangle(Point(self.button_bkgd_x, self.button_bkgd_y), Point(self.button_bkgd_x + self.button_bkgd_width, self.button_bkgd_y + self.button_bkgd_height))
		background.setFill('white')
		background.setOutline('white')
		background.draw(self.window)

		button_x_init = self.button_bkgd_x + self.button_bkgd_margin
		button_y = self.button_bkgd_margin

		button_x = button_x_init
		if self.pesticide:
			img = Image(Point(button_x + self.button_x_center, self.img_y_center), 'gif/pest-yes.gif')
		else:
			img = Image(Point(button_x + self.button_x_center, self.img_y_center), 'gif/pest-no.gif')
		img.draw(self.window)

		text = Text(Point(button_x + self.button_x_center, self.txt_y_center), 'Pesticides will help your crops \n grow stronger, but will damage your \n land and pond in the long run.')
		text.setSize(16)
		text.setFace('helvetica')
		text.draw(self.window)

		button_x += self.button_width
		if self.fertilizer:
			img = Image(Point(button_x + self.button_x_center, self.img_y_center), 'gif/fert-yes.gif')
		else:
			img = Image(Point(button_x + self.button_x_center, self.img_y_center), 'gif/fert-no.gif')
		img.draw(self.window)

		text = Text(Point(button_x + self.button_x_center, self.txt_y_center), 'Fertilizer will help your crops \n grow stronger, but could lead \n to an algae bloom in your pond.')
		text.setSize(16)
		text.setFace('helvetica')
		text.draw(self.window)

		button_x += self.button_width
		if self.mono:
			img = Image(Point(button_x + self.button_x_center, self.img_y_center), 'gif/mono.gif')
		else:
			img = Image(Point(button_x + self.button_x_center, self.img_y_center), 'gif/poly.gif')
		img.draw(self.window)

		text = Text(Point(button_x + self.button_x_center, self.txt_y_center), 'Monoculture farming will earn \n more money, but will \n damage the land over time.')
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

		year = 'gif/y' + str(self.year) + '.gif'
		year_label = Image(Point(100, 750), year)
		year_label.draw(self.window)
		self.draw_buttons()

		self.show_status()


	def show_status(self):
		background = Rectangle(Point(0, 0), Point(250, 210))
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
	
	if win:
		state = Image(Point(farm.window.getWidth()/2, farm.window.getHeight()/2), 'gif/signs/win.gif')
	else:
		state = Image(Point(farm.window.getWidth()/2, farm.window.getHeight()/2), 'gif/signs/lose.gif')

	state.draw(farm.window)

	message = Text(Point(farm.window.getWidth()/2 + 200, 800), 'Click anywhere to restart simulation.')
	message.setSize(20)
	message.setFace('helvetica')
	message.setStyle('bold')
	message.draw(farm.window)
	farm.year = 0 # reset

	farm.window.getMouse()
	farm.window.close()


while(True):
	farm = Farm()
	farm.run_tutorial()
	for i in range(0, 4):
		print('ROUND', i)
		farm.run_round()
		farm.year += 1

		if farm.field_health <= 0:
			conclusion(farm, win=False)
			break

	if farm.pond_health > 0 and farm.money > 0 and farm.field_health > 0:
		conclusion(farm, win=True)
	else:
		conclusion(farm, win=False)
