import os

class encryption:
    def __init__(self, textData = 'hello', shiftNumber = 2):#Default
        self.textData = textData
        self.shiftNumber = shiftNumber
    
    def message(self,textData):
        self.textData = textData
        if self.textData == '':
            self.textData = 'hello'

    def shift(self):
        changed = ''  
        for i in range(len(self.textData)):#Shifting
            changed = changed + str(chr(ord(self.textData[i])+self.shiftNumber))
        output_filename = os.path.normpath("code.txt")    
        file = open(output_filename,"a")
        file.write(changed + '\n')
        file.close() 
        return(changed)

    def decrypt(self):#Decrypting, minus two steps back
        changed = ''  
        for i in range(len(self.textData)):
            changed = changed + str(chr(ord(self.textData[i])-self.shiftNumber))
        output_filename = os.path.normpath("decode.txt")    
        file = open(output_filename,"a")
        file.write(changed + '\n')
        file.close() 
