import sys

from functools import lru_cache

@lru_cache
def uwuCodeInterpreter(uwuCode):
    array = [0]
    pointerLocation = 0
    i = 0
    c = 0
    while i < len(uwuCode):
        if uwuCode[i] == '<':
            if pointerLocation > 0:
                pointerLocation -= 1
        elif uwuCode[i] == '>':
            pointerLocation += 1
            if len(array) <= pointerLocation:
                array.append(0)
        elif uwuCode[i] == 'O': # +
            array[pointerLocation] += 1
        elif uwuCode[i] == '-':
            if array[pointerLocation] > 0:
                array[pointerLocation] -= 1
        elif uwuCode[i] == 'm': # .
            print(chr(array[pointerLocation]), end="")
        elif uwuCode[i] == '3': # ,
            x = input("Input:")
            try:
                y = int(x)
            except ValueError:
                y = ord(x)
            array[pointerLocation] = y
        elif uwuCode[i] == '^': # [
            if array[pointerLocation] == 0:
                while uwuCode[i] != 'T': # ]
                    i += 1
        elif uwuCode[i] == 'T': # ]
            if array[pointerLocation] != 0:
                while uwuCode[i] != '^':
                    i -= 1
        i += 1

def run():
    file = open(f"{sys.argv[1]}", "r+")

    filename = f"{sys.argv[1]}"

    index = filename.removesuffix(".uf")

    index = filename.split(index)

    index = index[-1]

    if index != ".uf":
        print("Please input a .uf file!")
    else:
        uwuCodeInterpreter(f"{file.read()}")

run()