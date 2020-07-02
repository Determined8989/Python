class Equipment():
	name = ''
	brand = ''
	state = False
	def Switch(self,state):
		self.state = state

class Monitor(Equipment):


	def __init__(self, resolution, size, mformat,name,brand):
		self.name = name
		self.brand = brand
		self.resolution = resolution
		self.size = size
		self.mformat = mformat
		self.state = False
	def PressPwrBtn(self):
		self.state = not self.state
	def show_info(self):
		print (
			'resolution:',self.resolution, 
			', size:', self.size, 
			', format:', self.mformat,
			',name:', self.name,
			',brand:',self.brand,
			',state:', self.state)

class Unit(Equipment):
	def __init__(self, processor, ram, hdd,  pwr,name,brand):
		self.processor = processor
		self.ram = ram
		self.hdd = hdd
		self.pwr = pwr
		self.state = False
		self.name = name
		self.brand = brand
	def PressPwrBtn(self):
		self.state = not self.state
	def show_info(self):
		print ('processor:',self.processor, 
			', ram:', self.ram, 
			', hdd:', self.hdd, 
			', pwr:', self.pwr, 
			', state:', self.state,
			', name:', self.name,
			',brand:', self.brand)

class Mouse(Equipment):
	def __init__(self,name, mformat,brand):
		self.lbtn = False
		self.rbtn = False
		self.scroll = 0  #0 = не двигается, -1 = низ, 1 = верх
		self.mformat = mformat
		self.name = name
		self.brand = brand
	def show_info(self):
		print('name:' ,self.name,
		 'mformat:', self.mformat,
		 ',scrollDirection:',self.scroll, 
		 ',lbtn:', self.lbtn, 
		 ',rbtn:', self.rbtn,
		 ',brand:', self.brand)
	def MakeScroll(self,direction):
		self.scroll = direction
	def PressButton(self,lmb,rmb):
		self.lbtn = lmb
		self.rbtn = rmb

class Keyboard(Equipment):
	def __init__(self,name,kformat,brand):
		self.name = name
		self.activebtn = ''
		self.kformat = kformat
		self.brand = brand
	def show_info(self):
		print('name:', self.name,
			',kformat:', self.kformat,
			',activebtn:',self.activebtn,
			',brand:', self.brand)
 
	def Buttons(self,activebtn):
		self.activebtn = activebtn

class PC():
	def __init__(self, monitor, unit, mouse, keyboard):
		self.monitor = monitor
		self.unit = unit
		self.mouse = mouse
		self.keyboard = keyboard
	def show_info(self):
		self.monitor.show_info()
		self.unit.show_info()
		self.mouse.show_info()
		self.keyboard.show_info()
	def PwrON(self):
		self.monitor.state = True
		self.unit.state	= True
	def PwrOFF(self):
		self.monitor.state = False
		self.unit.state = False
	def ReplaceMonitor(self,monitor):
		self.monitor = monitor
		
monitor1 = Monitor('1920/1080', 23 , 'HDMI', 'Panasonic2004Rus', 'Panasonic')
monitor2 = Monitor('1280/1024', 19 , 'VGA','LG-250 for gamers','LG')
unit1 = Unit(3580, 8, 256, 450, 'Radeon rx 2020 series', 'Radeon')
mouse1 = Mouse('Bloody V8',  'usb','Bloody')
keyboard1 = Keyboard('Renegade3000','USB','Renegade')
pc1 = PC(monitor1 , unit1, mouse1, keyboard1)
pc1.keyboard.Buttons('Alt + f4')
pc1.mouse.MakeScroll(1)
pc1.mouse.PressButton(True,False)
pc1.PwrON()
pc1.unit.PressPwrBtn()
pc1.PwrOFF()
pc1.ReplaceMonitor(monitor2)
pc1.show_info()