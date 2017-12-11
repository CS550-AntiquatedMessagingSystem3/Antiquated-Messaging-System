import sys
import re
import os.path
import codesystem
import encryption
import pigeon

encodeChoice = 0
codeMode = 0

while (codeMode < 1 or codeMode > 2):
    try:
        # Get Mode
        codeMode = int(input('Select the Mode:\n1: Encoding to send secret messages\n2: Decoding the secret message you recieved\nEnter the number corresponding to your Mode of operation:'))
    except ValueError:
        # Make sure it is a valid number
        print("That wasn't a proper choice.")
        
        
textBlock = []
if (codeMode ==1):

    while (encodeChoice < 1 or encodeChoice > 3):
        try:
            # Get encoded choice
            encodeChoice = int(input('Messaging Code System:\n1: Encryption\n2: Morse Code\n3: Pigeon Carrier\nEnter the number corresponding to your encoding choice:'))
        except ValueError:
            # Make sure it is a valid number
             print("That wasn't a proper choice.")
    while True:
        sourceText = input('\nType text to encode one line at a time. Press enter to start a new line. Type Q in a separate line to end the message.')
        if sourceText.lower() == 'q':
            break
        textBlock.append(sourceText)

    

if (codeMode ==2):
    # For decoding we dont provide an option for pegion carrier as there is no secret
    while (encodeChoice < 1 or encodeChoice > 2):
        try:
            # Get encoded choice
            encodeChoice = int(input('Messaging Code System:\n1: Encryption\n2: Morse Code\nEnter the number corresponding to your encoding choice:'))
        except ValueError:
            # Make sure it is a valid number
             print("That wasn't a proper choice.")
                       
    while True:
        inputFileName = input('\nType name of the file where the secret message is located:')
        if (os.path.isfile(inputFileName)):
            break
        else:
            print("That wasn't a valid input file with secret code.")
    with open(inputFileName) as f:
        content = f.readlines()
        textBlock =  [x.strip('\n') for x in content]


if (codeMode ==2):
    try:
        os.remove("decode.txt")
    except OSError:
        pass
    for textData in textBlock:
        if encodeChoice == 2:
            codesystem.Transmitter.decodeFromMorse(textData)
        if encodeChoice == 1:
            e = encryption.encryption()
            e.message(textData)
            e.decrypt()
        if encodeChoice == 3:
            p = pigeon.bird(3,textData)
            p.fly()

if (codeMode ==1):
    try:
        os.remove("code.txt")
    except OSError:
        pass
    for textData in textBlock:
        if encodeChoice == 2:
            codesystem.Transmitter.encodeToMorse(textData)
        if encodeChoice == 1:
            e = encryption.encryption()
            e.message(textData)
            e.shift()
        if encodeChoice == 3:
            p = pigeon.bird(3,textData)
            p.fly()
