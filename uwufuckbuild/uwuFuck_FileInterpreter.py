import sys
from functools import lru_cache
import msvcrt

filename = f"{sys.argv[1]}"
filenamenoex = filename.removesuffix(".uf")

@lru_cache
def uwuCodeInterpreter(uwuCode):
    array = [0]
    pointerLocation = 0
    i = 0
    c = 0
    while i < len(uwuCode):
        if uwuCode[i] == '<': # >~<
            if pointerLocation > 0:
                pointerLocation -= 1
        elif uwuCode[i] == '>': # >w<
            pointerLocation += 1
            if len(array) <= pointerLocation:
                array.append(0)
        elif uwuCode[i] == '+': # OwO
            array[pointerLocation] += 1
        elif uwuCode[i] == '-': # -w-
            if array[pointerLocation] > 0:
                array[pointerLocation] -= 1
        elif uwuCode[i] == '.': # UmU
            print(chr(array[pointerLocation]), end="")
        elif uwuCode[i] == ',': # :3
            x = input("Input:")
            try:
                y = int(x)
            except ValueError:
                y = ord(x)
            array[pointerLocation] = y
        elif uwuCode[i] == '[': # ^w^
            if array[pointerLocation] == 0:
                while uwuCode[i] != ']': # TwT
                    i += 1
        elif uwuCode[i] == ']':
            if array[pointerLocation] != 0:
                while uwuCode[i] != '[':
                    i -= 1
        i += 1

@lru_cache
def uwuCodeTranslator():
    # Opens file input into the terminal arguments, reads it, then closes it
    file = open(filename, "r+")
    stringvar = file.read()
    file.close()

    # Takes the variable (stringvar) and splits each word into seperate words, then creates a new variable (n) to call the length of the newstr variable
    newstr = stringvar.split(" ")
    n = len(newstr)

    # Makes a new variable (bfCode) that saves the input for translated uwuFuck language
    bfCode = ""
    for i in range(n):
        if newstr[i] == ">w<":
            bfCode += ">"
        elif newstr[i] == ">~<":
            bfCode += "<"
        elif newstr[i] == "OwO":
            bfCode += "+"
        elif newstr[i] == "-w-":
            bfCode += "-"
        elif newstr[i] == "UmU":
            bfCode += "."
        elif newstr[i] == ":3":
            bfCode += ","
        elif newstr[i] == "^w^":
            bfCode += "["
        elif newstr[i] == "TwT":
            bfCode += "]"
        else: # If there are any characters that arent like the ones listed above, it throws an error and tells the person where it is and what it is. Then it deletes the .uftemp file
            print(f'\nInvalid word found at index {i}: "{newstr[i]}"\n')
            
    # File gets closed again, then reopen in read mode. This is then run into the interpreter. Then it closes the .uftemp file and deletes it
    uwuCodeInterpreter(bfCode)
    print("Press any key to close...")
    msvcrt.getch()

# Looks to see if the input file is a .uf file or not. If not, it throws an error and asks for a .uf file
@lru_cache
def uwuCodeRunner():
    index = filename.split(filenamenoex)
    index = index[-1]

    if index != ".uf":
        return print("Please input a .uf file!")
    elif index == ".uf":
        uwuCodeTranslator()

uwuCodeRunner()
