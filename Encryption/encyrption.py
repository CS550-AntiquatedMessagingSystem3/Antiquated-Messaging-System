message = str(input('Type in your message. This program will encrypt your message safely.'))
changed = ''  
c = ''
for i in range(len(message)):
	chr(ord(message[i])+2)
	changed = changed + str(chr(ord(message[i])+2))
		
print(changed)