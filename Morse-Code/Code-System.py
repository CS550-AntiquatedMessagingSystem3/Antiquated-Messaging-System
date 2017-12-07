import os

class Messenger:

    morseAlphabet ={
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

    def encodeToMorse(textData):
        encodedMessage = ""
        for char in textData[:]:
            encodedMessage += Messenger.morseAlphabet[char.upper()] + " "          
        return encodedMessage
    
    def decodeToMorse():
        return 'hello world'

class Transmitter:
    
    def decodeFromMorse():
        return 'hello world'
    def encodeToMorse(textData):
        output_filename = os.path.normpath("code.txt")    
        encodeText = Messenger.encodeToMorse(textData)
        file = open(output_filename,"a")
        file.write(encodeText + '\n')
        file.close() 


