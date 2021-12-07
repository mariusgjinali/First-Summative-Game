#Author: Marius Gjinali
#Date: November 13
#parameters: none
#preconditions: You need to have imported random and added the riddleList and answerList, as well as having input your own riddles/ answers. Of course, you can use these ones if you wish.
#result is in the terminal
#return value: none

import random

def getRiddle(riddleList, answerList):
    

    riddlePicker = random.randint (0,len(riddleList)-1)

    playerAnswer = input(riddleList[riddlePicker])
    correctOrNot = 0

    n = 0
    while n <len(riddleList):
        if answerList[n] in playerAnswer.lower():
            correctOrNot = 1
            print("That is correct!")
            
        n+=1
    if correctOrNot ==0:
        print("That is false...")

    
riddleList = ["Very well. What has 5 letters, and adding 2 makes it shorter?\n ","Very well then. What moves, yet does not walk. What roars, without a mouth? What eats, yet has no stomach?\n ","Ah, a classic: Which creature has one voice and yet becomes four-footed and two-footed and three-footed\n" ]
answerList = ["short","fire","man","three"]
getRiddle(riddleList,answerList)
