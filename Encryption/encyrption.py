class encryption:
	def__init(self, message = 'hello', shift = 2)
		self.message = message
		self.shift = shift
	
	def message(self,message):
		message = self.message
		if self.message = '':
			self.message = 'hello'

	def shift(self, message):
		changed = ''  
		
		for i in range(len(message)):
			chr(ord(message[i])+self.shift)
			changed = changed + str(chr(ord(message[i])+2))
		
		print(changed)