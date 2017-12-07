class encryption:
	def__init(self, textData = 'hello', shift = 2)
		self.textData = textData
		self.shift = shift
	
	def message(self,textData):
		textData = self.textData
		if self.textData = '':
			self.textData = 'hello'

	def shift(self, textData):
		changed = ''  
		
		for i in range(len(textData)):
			chr(ord(message[i])+self.shift)
			changed = changed + str(chr(ord(textData[i])+self.shift))
		
		return(changed)