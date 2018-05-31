from graphics import *

window = GraphWin('test', 500, 500)
img = Image(Point(100, 100), 'test.png')
img.draw(window)
message = Text(Point(400, 400), 'Click anywhere to quit.')
message.draw(window)

window.getMouse()
window.close()	