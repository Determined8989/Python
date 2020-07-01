#Реализовать класс Monitor. Класс должен иметь такие поля как 
# "resolution (str), size (int), format (str), state (bool)"
class Monitor:

	def __init__(self, resolution, size, mformat):
		self.resolution = resolution
		self.size = size
		self.mformat = mformat
		self.state = False
	def PressPwrBtn(self):
		self.state = not self.state
	def show_info(self):
		print ('resolution:',self.resolution, ', size:', self.size, ', format:', self.mformat, ', state:', self.state)

"""
print('monitor1:')
monitor1 = Monitor('1920/1080', 23 , 'HDMI')
monitor1.PressPwrBtn()
monitor1.show_info()

print('monitor2:')
monitor2 = Monitor('1280/1024', 19 , 'VGA')
monitor2.show_info()
#Реализовать класс Unit. Класс должен иметь такие поля как 
#"processor (int), ram (int), hdd (int), case (str), pwr (int), state (bool)"
"""
class Unit:
	def __init__(self, processor, ram, hdd, case, pwr):
		self.processor = processor
		self.ram = ram
		self.hdd = hdd
		self.case = case
		self.pwr = pwr
		self.state = False
	def PressPwrBtn(self):
		self.state = not self.state
	def show_info(self):
		print ('processor:',self.processor, ', ram:', self.ram, ', hdd:', self.hdd, ', case:', self.case, ', pwr:', self.pwr, ', state:', self.state)
"""
print('unit1:')
unit1 = Unit(3580, 8, 256,'Radeon rx 2020 series', 450)
unit1.PressPwrBtn()
unit1.show_info()

print('unit2:')
unit2 = Unit(2660, 16, 1024, 'Doggi 5960 gaming edition', 750)
unit2.show_info()
"""

class PC():
	def __init__(self, monitor, unit):
		self.monitor = monitor
		self.unit = unit
	def show_info(self):
		self.monitor.show_info()
		self.unit.show_info()
	def PwrON(self):
		self.monitor.state = True
		self.unit.state	= True
	def PwrOFF(self):
		self.monitor.state = False
		self.unit.state = False
	def ReplaceMonitor(self,monitor):
		self.monitor = monitor
		
monitor1 = Monitor('1920/1080', 23 , 'HDMI')
monitor2 = Monitor('1280/1024', 19 , 'VGA')
unit1 = Unit(3580, 8, 256,'Radeon rx 2020 series', 450)
pc1 = PC(monitor1 , unit1)
pc1.PwrON()
pc1.unit.PressPwrBtn()
#pc1.show_info()
pc1.PwrOFF()
#pc1.show_info()
pc1.ReplaceMonitor(monitor2)
pc1.show_info()