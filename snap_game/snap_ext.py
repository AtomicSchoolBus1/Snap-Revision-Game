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


#Arrays
module1Qs = []
module1Ans = []

module2Qs = []
module2Ans = []

module3Qs = []
module3Ans = []


#Retrieves the questions and answers from the external files
def prelim():
    Qs1Object = open('1qs.txt', 'r')
    Ans1Object = open('1ans.txt', 'r')

    Qs2Object = open('2qs.txt', 'r')
    Ans2Object = open('2ans.txt', 'r')

    Qs3Object = open('2qs.txt', 'r')
    Ans3Object = open('2ans.txt', 'r')

    for x in range(1, 3):
        if x == 1:
            currentQs = Qs1Object.readlines()
            currentAns = Ans1Object.readlines()
            currentModuleQs = module1Qs
            currentModuleAns = module1Ans
        if x == 2:
            currentQs = Qs2Object.readlines()
            currentAns = Qs2Object.readlines()
            currentModuleQs = module2Qs
            currentModuleAns = module2Ans
        if x == 3:
            currentQs = Qs3Object.readlines()
            currentAns = Ans3Object.readlines()
            currentModuleQs = module3Qs
            currentModuleAns = module3Ans

        
        for y in range(0, (len(currentQs))):
                currentModuleQs.append(currentQs[y].strip())
        currentModuleQs.append(currentQs[(len(currentQs)):])
        index = len(currentModuleQs) - 1
        currentModuleQs.pop(index)
        
        for y in range(0, (len(currentAns))):
                currentModuleAns.append(currentAns[y].strip())
        currentModuleAns.append(currentAns[(len(currentAns)):])
        index2 = len(currentModuleAns) - 1
        currentModuleAns.pop(index2)


    Qs1Object.close()
    Ans1Object.close()

    Qs2Object.close()
    Ans2Object.close()

    Qs3Object.close()
    Ans3Object.close()


def getQuestions(moduleSelection):
    if str(moduleSelection) == "1":
        return module1Qs
    if str(moduleSelection) == "2":
        return module2Qs
    if str(moduleSelection) == "3":
        return module3Qs

def getAns(moduleSelection):
    if str(moduleSelection) == "1":
        return module1Ans
    if str(moduleSelection) == "2":
        return module2Ans
    if str(moduleSelection) == "3":
        return module3Ans

def addNewData(newQ, newAns, currentModule):
    if currentModule == "1":
        questionModuleObject = open("1qs.txt", "a")
        answerModuleObject = open("1ans.txt", "a")
    if currentModule == "2":
        questionModuleObject = open("2qs.txt", "a")
        answerModuleObject = open("2ans.txt", "a")
    if currentModule == "3":
        questionModuleObject = open("3qs.txt", "a")
        answerModuleObject = open("3ans.txt", "a")
    
    questionModuleObject.write("\n" + str(newQ))
    answerModuleObject.write("\n" + str(newAns))

    questionModuleObject.close()
    answerModuleObject.close()
