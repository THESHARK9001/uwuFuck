from functools import lru_cache
import sys
import os

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

code = input("Enter your uwuFuck Code!\n:")

file = open("~.uftemp", "w+")
file.close()
file = open("~.uftemp", "a+")

newstr = code.split(" ")
n = len(newstr)

    #print ("stringcount = " + str(n))
for i in range(n):
        # print ("string " + str(i) + " = " + str(newstr[i])) 
    if newstr[i] == ">w<":
        file.write(">")
    elif newstr[i] == ">~<":
        file.write("<")
    elif newstr[i] == "OwO":
        file.write("+")
    elif newstr[i] == "-w-":
        file.write("-")
    elif newstr[i] == "UmU":
        file.write(".")
    elif newstr[i] == ":3":
        file.write(",")
    elif newstr[i] == "^w^":
        file.write("[")
    elif newstr[i] == "TwT":
        file.write("]")
file.close()
file = open("~.uftemp", "r+")

uwuCodeInterpreter(file.read())
file.close()
os.remove("~.uftemp")