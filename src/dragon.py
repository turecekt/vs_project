'''
DRAČÍKŘIVKA
Vytvořte program, který vykreslí Dračí křivku, někdy nazývanou „Heighway Dragon“.
VSTUP•
Počet iterací Dračí křivky •
Barva vykreslené čáry (z výčtu)•
Barva pozadí (z výčtu)•
Vpřípadě puštění bez parametrů vykreslení 9-té iterace Dračí křivky, červenoučárou na černém pozadí
VÝSTUP•
Vykreslení a zobrazení Dračí křivky
'''

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg



'''
	Input values
'''
iteration=int(input('Pocet interakci:'))
linecolor=input('Barva cary:')
backgroundcolor=input('Barva pozadi:')

'''
 move left
 in = pos , count , angle
 ret number of rotation, pos array
1 = up , 0 = no change , -1 = down 
 [90,180,270,360] degree
 [1,0,-1,0] = y
 [0,-1,0,1] = x
'''
def move_left(posx,posy,cnt,angle):
	static_y = [1,0,-1,0] # static mapping
	static_x = [0,-1,0,1] # static mapping
	x = posx[cnt]
	x = x + static_x[angle]
	posx[cnt] = x
	y = posy[cnt]
	y = y + static_y[angle]
	posy[cnt] = y
	

'''
 move right
 in = pos , count , angle
 ret number of rotation, pos array
1 = up , 0 = no change , -1 = down 
 [90,180,270,360] degree
 [-1,0,1,0] = y
 [0,-1,0,1] = x
'''

def move_right(posx,posy,cnt,angle):
	static_y = [-1,0,1,0]  # static mapping
	static_x = [0,-1,0,1] # static mapping
	x = posx[cnt]
	x = x + static_x[angle]
	posx[cnt] = x
	y = posy[cnt]
	y = y + static_y[angle]
	posy[cnt] = y

def generate_dragon():
	global r, l, old, new
	r = 'r'
	l = 'l'
	old = r
	new = old
	loop_cycle = 1
	while loop_cycle < iteration:
		new = (old) + (r)
		old = old[::-1]
		for char in range(0,len(old)):
			if old[char] == r:
				old = (old[:char])+ (l) + (old[char+1:])
			elif old[char] == l:
				old = (old[:char]) + (r) + (old[char+1:])
		new = (new) + (old)
		old = new
		loop_cycle=loop_cycle+1


generate_dragon()

position = 0
angle_right = 0
angle_left = 3-angle_right
size = len(new)
app = QtGui.QApplication([])
x = np.zeros(size)
y = np.zeros(size)
win = pg.GraphicsLayoutWidget(show=True, title="Dragon")
win.resize(1024,768)
plot = win.addPlot(title="Dragon plot")
dragon = plot.plot(x,y)

'''
Graph update function
'''

def update():
	global dragon, x, y, position, size, angle_left, angle_right
	if(position < size-1):
		if new[position] == (r):# right
			if(new[position-1] == (r)):
				angle_right +=1
				if(angle_left < 0):
					angle_left = 0
				if(angle_right > 3):
					angle_right = 0
			else:
				angle_right = 3 - angle_left
				if(angle_right < 0):
					angle_right = 0
				if(angle_right > 3):
					angle_right = 0

			move_right(x,y,position,angle_right)
		elif new[position] == (l):#left
			if(new[position-1] == (l)):
				angle_left +=1
				if(angle_left > 3):
					angle_left = 0
				
			else:
				angle_left = 3-(angle_right)
				if(angle_left < 0):
					angle_left = 0
			move_left(x,y,position,angle_left)
		else:	#done or empty
			pass
		dragon.setData(x,y)
		position +=1
		x[position]=x[position-1]#store old pos to new
		y[position]=y[position-1]#store old pos to new
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(1)
        
if __name__ == '__main__':
	import sys
	if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
		QtGui.QApplication.instance().exec_()

