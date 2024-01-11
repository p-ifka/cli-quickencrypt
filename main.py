#!/usr/bin/env python3
import sys
import os
from cryptography.fernet import Fernet

## SETTTINGS ##
keyPath = os.path.dirname(os.path.abspath(sys.argv[0]))+"/key.key" #String: path of text file containing the encryption key, leave as "" to generate a new one
debugInfo = False # boolean: whether or not to display debug info, when false, only the output will be printed

## functions
def showHelp():
    print("Usage: quickencrypt [mode] [input type] [file/text]")
    print("1. mode: 'encrypt' (en) or 'decrypt' (de)")
    print("2. input type: 'file' ('-f') or 'text' ('-t')")
    print("3. File: /path/to/file")
    print("3. text: 'text here'")
def debugPrint(text):
    if(debugInfo == True):
        print(text)



## make sure all arguments are provided
if len(sys.argv) < 3:
    showHelp()
    exit()


## determine mode (encrypt or decrypt)
arg1 = sys.argv[1]
if(arg1 == 'encrypt' or arg1 == 'en'):
    debugPrint('mode: encryption')
    mode = 'en'
elif(arg1 == 'decrypt' or arg1 == 'de'):
    debugPrint('mode: decryption')
    mode = 'de'
else:
    showHelp()
    exit()

## determine input type (file or string)
arg2 = sys.argv[2]
if(arg2 == "file" or arg2 == '-f'):
    debugPrint("en/decrypting file...")
    inMeth = "file"
elif(arg2 == "text" or arg2 == '-t'):
    debugPrint("en/decrypting text...")
    inMeth = "text"
else:
    showHelp()
    exit()

## determine encryption key
if(keyPath != ""):
    keyFile = open(keyPath, "r")
    key = keyFile.read()
    debugPrint("using key from file")
    debugPrint("using key: "+key)
else: # if no 'keyPath' is defined, a new key will be generated each time
    key = Fernet.generate_key()
    debugPrint("using generated key")
    debugPrint("using key: "+key)

## get text for encryption
if(inMeth == 'text'):
    input = sys.argv[3]
elif(inMeth == 'file'):
    inputFile = open(sys.argv[3], 'r')
    input = inputFile.read()
debugPrint("en/decrypting text: "+input)

## en/decrypt text
f = Fernet(key)
if(mode == 'en'):
    output = f.encrypt(input.encode())
else:
    output = f.decrypt(input.encode())

print(output.decode('utf-8'))
