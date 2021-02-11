#snap_main.py - Scripts by Tommy C-H

import snap_ext
import snap_gui
import random
import time

#Startup script - chooses module and questions/answers (dependant on functions from snap_ext.py)
print("Welcome to snap!")
print("")
selection = snap_ext.chooseModule()
chosenQuestions = snap_ext.getQuestions(selection)
chosenAns = snap_ext.getAns(selection)

#Displays random questions and randomly shuffles through the answers
playRequest = 1
questionLevel = 0
answerPosition = 0
score = 0
while playRequest == 1:
    for x in range(0, 5):
        questionLevel = questionLevel + 1
        print("Question " + str(questionLevel) + ":")
        currentQuestionPosition = random.randint(0, (len(chosenQuestions) - 1))
        print(chosenQuestions[currentQuestionPosition])
        ansCorrect = 0
        currentAnsPosition = 0
        previousAnsPosition = 0
        print("")
        while True:
            currentAnsPosition = random.randint(0, ((len(chosenAns)) - 1))
            while True:
                if currentAnsPosition == previousAnsPosition:
                    currentAnsPosition = random.randint(0, ((len(chosenAns)) - 1))
                else:
                    break
            print(chosenAns[currentAnsPosition] + (" " * len(chosenAns[previousAnsPosition])), end = "\r")
            previousAnsPosition = currentAnsPosition
            choice = input("")
            if choice == "Y":
                break
            else:
                print("")
        print("")
        print("")
        if currentAnsPosition == currentQuestionPosition:
            print("Congratulations! That was the correct answer!")
            time.sleep(1.5)
            print("")
            print("Score increased by 100")
            score = score + 100
            print("")
            print("")
            print("Next question:")
        else:
            print("")
            print("Answer incorrect!")
    
    #End of round selection
    print("")
    print("")
    print("You achieved a score of " + str(score) + " points. Would you like to play again? (Y/N)")
    choiceContinue = input("")
    while True:
        if choiceContinue == "Y":
            print("")
            print("Great! Let's continue, try to increase your score!")
            print("")
            print("")
            print("")
            break
        if choiceContinue == "N":
            print("")
            print("Thanks for playing!")
            playRequest = 0
            break
        else:
            print("Invalid response, please enter either (Y) or (N)")