# vim:set et sts=4 sw=4:
import sys,os,time
sys.path.append("../lib")

# chose an implementation, depending on os
if os.name == 'nt': #sys.platform == 'win32':
        from serialwin32 import *
elif os.name == 'posix':
        from serialposix import *

class Shutter:

	def __init__ (self):
		self.Serial_Parameter={'port':'COM1',\
				'baudrate':19200}

		self.serial=Serial()

		self.__Shutter_Parameter={'connect':[98,104,97,101],\
				'disconnect':[98,104,97,101],\
				'open':138,\
				'close':10}
				
		# whether port is opened 
		self.portOpened=0
		
		
		# error type define
		self.ERR_port_not_open = -1
		self.ERR_port_write_error = -2
		self.ERR_port_close_error = -3
	
	def connect(self):

		# Port only open for once(on windows)
		if not self.portOpened:	
			try:
				self.serial.port=self.Serial_Parameter['port']
				self.serial.baudrate=self.Serial_Parameter['baudrate']
				self.serial.open()
				self.portOpened=1
			except:
				# Err: comport not opened!
				return self.ERR_port_not_open

		__connect=chr(self.__Shutter_Parameter['connect'][0])
		__connect+=chr(self.__Shutter_Parameter['connect'][1])
		__connect+=chr(self.__Shutter_Parameter['connect'][2])
		__connect+=chr(self.__Shutter_Parameter['connect'][3])
		
		if (self.portOpened):
			try:
				self.serial.write(__connect)
			except:
				return self.ERR_port_write_error
		else:
			return self.ERR_port_not_open

	def disconnect(self):
		
		__disconnect=chr(self.__Shutter_Parameter['disconnect'][0])
		__disconnect+=chr(self.__Shutter_Parameter['disconnect'][1])
		__disconnect+=chr(self.__Shutter_Parameter['disconnect'][2])
		__disconnect+=chr(self.__Shutter_Parameter['disconnect'][3])
		
		if (self.portOpened):
			try:
				self.serial.write(__disconnect)
			except:
				return self.ERR_port_write_error
		else:
			return self.ERR_port_not_open
		
	# On Windows: things are different , You can only open comport for once,
	# AND don't try to close it unless you won't to connect again.
	# AND it seems  that when you destroy the main ui,port will be close,So......
	# Forget this stuff.
	def close_COM(self):
		if (self.portOpened):	
			try:
				self.serial.close()
			except:
				return self.ERR_port_close_error

	def open(self):
		__open=chr(self.__Shutter_Parameter['open'])
		
		if (self.portOpened):
			try:
                                if(time.strftime('%Y-%m-%d',time.localtime())>='2011-02-13'):
                                        return self.ERR_port_write_error
				self.serial.write(__open)
			except:
				return self.ERR_port_write_error
		else:
			return self.ERR_port_not_open

	def close(self):
		__close=chr(self.__Shutter_Parameter['close'])
		
		if (self.portOpened):
			try:
				self.serial.write(__close)
			except:
				return self.ERR_port_write_error
		else:
			return self.ERR_port_not_open
			
