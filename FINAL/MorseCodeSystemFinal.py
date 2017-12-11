import os

class Messenger:

    morseAlphabet ={#Alphabet
            "A" : ".-",
            "B" : "-...",
            "C" : "-.-.",
            "D" : "-..",
            "E" : ".",
            "F" : "..-.",
            "G" : "--.",
            "H" : "....",
            "I" : "..",
            "J" : ".---",
            "K" : "-.-",
            "L" : ".-..",
            "M" : "--",
            "N" : "-.",
            "O" : "---",
            "P" : ".--.",
            "Q" : "--.-",
            "R" : ".-.",
            "S" : "...",
            "T" : "-",
            "U" : "..-",
            "V" : "...-",
            "W" : ".--",
            "X" : "-..-",
            "Y" : "-.--",
            "Z" : "--..",
            " " : "/",
            "1" : ".----",
            "2" : "..---",
            "3" : "...--",
            "4" : "....-",
            "5" : ".....",
            "6" : "-....",
            "7" : "--...",
            "8" : "---..",
            "9" : "----.",
            "0" : "-----",
            "." : ".-.-.-",
            "," : "--..--",
            ":" : "---...",
            "?" : "..--..",
            "'" : ".----.",
            "-" : "-....-",
            "/" : "-..-.",
            "@" : ".--.-.",
            "=" : "-...-"
            }

    inverseMorseAlphabet = dict((v, k) for (k, v) in morseAlphabet.items())

    def encodeToMorse(textData):
        encodedMessage = ""
        for char in textData[:]:
            encodedMessage += Messenger.morseAlphabet[char.upper()] + " "          
        return encodedMessage
    
    def decodeFromMorse(textData):
        decodedMessage = ""
        textDataSeparated = textData.split(' ')
        for char in textDataSeparated:
            if char in Messenger.inverseMorseAlphabet:
                decodedMessage += Messenger.inverseMorseAlphabet[char]
            #else:
             #   # CNF = Character not found
              #  decodedMessage += '<CNF>'       
        return decodedMessage

class Transmitter:
    
    def decodeFromMorse(textData):#Decode, inverse alphabet
        output_filename = os.path.normpath("decode.txt")    
        decodeText = Messenger.decodeFromMorse(textData)
        file = open(output_filename,"a")
        file.write(decodeText + '\n')#Enter space every line
        file.close() 
        
    def encodeToMorse(textData):
        output_filename = os.path.normpath("code.txt")    
        encodeText = Messenger.encodeToMorse(textData)
        file = open(output_filename,"a")#Append text
        file.write(encodeText + '\n')
        file.close() 



