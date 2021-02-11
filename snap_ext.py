#snap_ext.py - Scripts by Tommy C-H

import random
import time

#Functions
def chooseModule():
    print("Please pick a module from the following: (1), (2) or (3):")
    selection = ""
    while selection != "1" or selection != "2" or selection != "3":
        selection = input("")
        if selection == "1":
            print("")
            print("")
            print("Choice valid. You have chosen module " + str(selection) + ".")
            print("")
            break
        elif selection == "2":
            print("")
            print("")
            print("Choice valid. You have chosen module " + str(selection) + ".")
            print("")
            break
        elif selection == "3":
            print("")
            print("")
            print("Choice valid. You have chosen module " + str(selection) + ".")
            print("")
            break
        else:
            print("")
            print("Selection invalid, please select either (1), (2) or (3):")
    return selection

def getQuestions(moduleSelection):
    if str(moduleSelection) == "1":
        return module1Qs

def getAns(moduleSelection):
    if str(moduleSelection) == "1":
        return module1Ans

#Arrays
module1Qs = ["What is the name given to the 'brain' of the computer?", "What is the name for volatile, fast memory?", "What is the section of the CPU that carries out logic operations?", "What is manufacturer specific hardware data stored in?"]
module1Ans = ["CPU", "RAM", "ALU", "Read-Only Memory"]