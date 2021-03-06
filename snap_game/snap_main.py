#snap_main.py - Scripts by Tommy C-H

import snap_ext
import snap_gui
import random
import time

#Startup script - chooses module and questions/answers (dependant on functions from snap_ext.py)
while True:
    print("Welcome to snap!")
    print("")
    print("Main menu:")
    print("Type (1) to play the game with the current questions and answers.")
    print("Type (2) to add a new question and answer to the list.")
    print("Type (3) to view the instructions on how to play.")
    print("")
    mainMenuChoice = input("")
    if mainMenuChoice == "1":
        break
    if mainMenuChoice == "2":
        print("")
        print("What module do you want to add a new question to? Choose either (1), (2) or (3):")
        inputAccepted = 0
        while inputAccepted == 0:
            choiceOfModule = input("")
            if choiceOfModule == "1":
                inputAccepted = 1
            if choiceOfModule == "2":
                inputAccepted = 1
            if choiceOfModule == "3":
                inputAccepted = 1
            else:
                print("Invalid input, please retype your choice:")
                print("")
        print("")
        print("")
        print("Module accepted. Please type your new question: ")
        newQ = input("")
        print("")
        print("Now please type the answer to that question: ")
        newAns = input("")
        print("")
        print("")
        snap_ext.addNewData(newQ, newAns, choiceOfModule)
        print("Data submitted! Returning to main menu.")
        time.sleep(1)
        print("")
    if mainMenuChoice == "3":
        print("")
        print("Instructions:")
        print("Welcome to snap! In this game, the aim is to match up the correct answer with the question.")
        print("First, the game will randomly produce a question, and an answer will pop up beneath it. if the answer is not correct, press (ENTER) and the game will present a new answer. Keep going until you have found the right answer. Then, type (Y) in the input box and press (ENTER). If you guessed right, 100 points will be added to your overall score. If not, the game will move on to the second question without awarding any points. After 5 turns have passed, the game will show you your final score. After that, you can either choose to play again to increase your current score even further, or quit the game.")
        print("")
        print("Have fun!")
        print("")
        print("")
        print("Press (ENTER) to return to the main menu:")
        input()
        print("")
        print("")
    else:
        print("")
        print("Invalid command, please choose either (1), (2) or (3):")


snap_ext.prelim()
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
                    previousAnsPosition = currentAnsPosition
                    currentAnsPosition = random.randint(0, ((len(chosenAns)) - 1))
                else:
                    break
            print(chosenAns[currentAnsPosition] + (" " * len(chosenAns[previousAnsPosition])))
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