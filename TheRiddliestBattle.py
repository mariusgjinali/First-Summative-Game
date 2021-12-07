import random
import multiprocessing
import playsound
from pygame import mixer
import time
import art

from GordonsCode import getUserInfo
mixer.init() #Initialzing pyamge mixer
mixer.music.load('gatesofheaven.mp3') #Loading Music File
#Variables concerning the general running of the game:
whereInGame = 1
currentLocation = 0
musicPlayer = "entranceClassroom.mp3"
dayCounter = 1
actionCounter = 4
subsequentDaysCounter = ""
#Variables used exclusively for the beginning
userName = ""
userAge = ""
favColour = ""
favAnimal = ""
firstCAnswer = " "
#Variables used later in the game
riddleList = ["What's 4*7?\n","What season is it?\n","What country is UCC in?\n"]
answerList = ["28", "fal", "cana"]
riddlePoints = 0
whereToGoFromRiddle = ""
braveryPoints = 0
whereToGoFromBravery = ""
luckPoints = 0
whereToGoFromLuck = ""
earlyAcessToJeremysHouse = ""


mixer.music.play()


while whereInGame == 1:
    #This is Gordon's function, so please give him an 8 :)
    def getUserInfo():
        userName = input(str("What is your name? "))
        userAge = input("How old are you? ")
        favColour = input(str("What is your favorite colour? ")) #input Marius wants for his game
        favAnimal = input(str("What is your favorite animal? ")) #input Marius wants for his game
        infoList = [userName, userAge, favColour, favAnimal]
        print("Hello ",userName)
        

    getUserInfo()
    
    firstCAnswer = input("\nHello, my name's Joseph, and I'm 9 years old.\nJeremy told me to tell you that he's challenging you to a riddle contest, at his house in 2 days. I'll help train you so you can beat him! \nDo you accept?  ")
    whereInGame = 1 

    if "yes" in firstCAnswer.lower() or "ok" in firstCAnswer.lower() or "sure" in firstCAnswer.lower()or "alri" in firstCAnswer.lower():
        firstRight = input("\nAlright then, let's go to the school!  ")   
        whereInGame = 2
    else: 
        print("What? Please restart now...")
        whereInGame = 1
    if "no" in firstCAnswer.lower() or "nev" in firstCAnswer.lower():
        print("Ok then, go fight him now")
        whereInGame = 4
    
     
#This is the exposition code, it essentially tells the player what to do in the school
if whereInGame ==2:
    print("\nThe room we're in right now is the entrance. To the north, you have the riddle classroom. \n \nTo the east ,you have the bravery classroom.To the south, you have the luck classroom. \n\nFinally, to the west, you can exit the building, which allows you to go to Jeremy's house, where the competition is.\n\nNow, every day, you have 4 actions. Every time you complete a riddle or test, you use up 1 action. \n \nLastly, when 4 actions are done, you can move on to the next day.\n\nOh wait! I forgot something! Whenever you move to a new room, you can type 'Day Counter' or 'Action Counter' to see how many actions you have left, and what day it is!")
    whereInGame =3

dayCounter = 1
actionCounter = 4
firstDayCounter=art.text2art("Day  1")
print (firstDayCounter)
mixer.music.stop()
while whereInGame ==3 and dayCounter<3:

    mixer.init() #Initialzing pyamge mixer
    mixer.music.load(musicPlayer) #Loading Music File
    mixer.music.play()
    #OK so 0 means entrance 1 means riddle classroom 2 means bravery classroom 3 means luck classroom and 4 means Jeremy's house. 
    currentLocation = 0
    if actionCounter == 0:
            print("\nTime to move on to the next day!")
            dayCounter+=1
            actionCounter = 4
            subsequentDaysCounter=art.text2art("Day ", dayCounter)
            print (subsequentDaysCounter)
         
            currentLocation = 0
    if currentLocation == 0:


        whereToGoFromEntrance = input("\nWhat direction do you want to go in from the entrance?  ")
        
        if "nor" in whereToGoFromEntrance.lower():
            musicPlayer = "riddleClassroom.mp3"
            mixer.init() #Initialzing pyamge mixer
            mixer.music.load(musicPlayer) #Loading Music File
            mixer.music.play()
            currentLocation = 1
            riddleWelcome=art.text2art("Riddle Classroom")
            print (riddleWelcome)
        if "eas" in whereToGoFromEntrance.lower():
            musicPlayer = "braveryClassroom.mp3"
            mixer.init() #Initialzing pyamge mixer
            mixer.music.load(musicPlayer) #Loading Music File
            mixer.music.play()
            currentLocation = 2
            braveryWelcome=art.text2art("Bravery Classroom")
            print (braveryWelcome)
        if "sou" in whereToGoFromEntrance.lower():
            musicPlayer = "luckClassroom.mp3"
            mixer.init() #Initialzing pyamge mixer
            mixer.music.load(musicPlayer) #Loading Music File
            mixer.music.play()
            currentLocation = 3
            luckWelcome=art.text2art("Luck Classroom")
            print (luckWelcome)
        if "wes" in whereToGoFromEntrance.lower():
            currentLocation = 4
            jeremysHouse=art.text2art("Jeremy's House")
            print (jeremysHouse)
        if currentLocation ==4 and dayCounter<3:
            earlyAcessToJeremysHouse = input("\nAre you sure you want to do the competition now? It's not 2 days yet?  ")
        if "day" in whereToGoFromEntrance.lower() or "acti" in whereToGoFromEntrance.lower():
            print("Action Points")
            print(actionCounter)
            print("Day number")
            print(dayCounter)
            currentLocation = 0

    if currentLocation ==1:
        whereToGoFromRiddle = input("\nWhat do you want to do? Move or complete a riddle?  ")
        if "rid" in whereToGoFromRiddle.lower() or "compl" in whereToGoFromRiddle.lower():
            import GetRiddleFunctionAndPrintResult as riddle
            riddleFunction = riddle.getRiddle(riddleList, answerList)
            #I'll make them get the point every time, since they're children and making them cry would be fun but counterproductive
            riddlePoints+=1
            print("\nNow that the riddle is done, let's go to the entrance")
            actionCounter -=1
            musicPlayer = "entranceClassroom.mp3"
            mixer.init() #Initialzing pyamge mixer
            mixer.music.load(musicPlayer) #Loading Music File
            mixer.music.play()
            currentLocation = 0
        if "mov" in whereToGoFromRiddle.lower():
            directionFromRiddle = input("\nWhich direction would you like to go in?  ")
            if "nor" in directionFromRiddle.lower():
                print("\nThere is a wall here.\n")
                directionFromRiddle = input("\nWhich direction would you like to go in?  ")
            if "eas" in directionFromRiddle.lower():
                print("\nThere is a wall here.\n")
                directionFromRiddle = input("\nWhich direction would you like to go in?  ")
            if "wes" in directionFromRiddle.lower():
                print("\nThere is a wall here.\n")
                directionFromRiddle = input("\nWhich direction would you like to go in?  ")
            if "sou" in directionFromRiddle.lower():
                musicPlayer = "entranceClassroom.mp3"
                mixer.init() #Initialzing pyamge mixer
                mixer.music.load(musicPlayer) #Loading Music File
                mixer.music.play()
                print (entranceWelcome)
                
        if "day" in whereToGoFromRiddle.lower() or "acti" in whereToGoFromRiddle.lower():
            print("Action Points")
            print(actionCounter)
            print("Day number")
            print(dayCounter)
            currentLocation = 1
    if currentLocation == 2:
        whereToGoFromBravery = input("\nWhat do want to do, move or test your bravery?  ")
        if "brav" in whereToGoFromBravery.lower() or "test" in whereToGoFromBravery.lower():
            print("\nFor this test, you'll be running away from a bear. You heard what I said.\n")
            if braveryPoints<1 and currentLocation == 2:
                braveryAsk = input("Will you face it or refuse?  ")
                if "fa" in braveryAsk.lower():
                    print("That's a very brave call!")
                    braveryPoints+=1
                    print("Let's go to the entrance now.")
                    musicPlayer = "entranceClassroom.mp3"
                    mixer.init() #Initialzing pyamge mixer
                    mixer.music.load(musicPlayer) #Loading Music File
                    mixer.music.play()
                    currentLocation = 0
                    actionCounter-=1
                else:
                    print("I'm sorry, that's not it...\n\n Time to go to the entrance now...")
                    musicPlayer = "entranceClassroom.mp3"
                    mixer.init() #Initialzing pyamge mixer
                    mixer.music.load(musicPlayer) #Loading Music File
                    mixer.music.play()
                    currentLocation = 0
                    actionCounter-=1
            if braveryPoints == 1 and currentLocation == 2:
                braveryAsk = input("You've decided to face it. It's chasing you down a hallway. Do you try leaving the hallway, or hide inside a closet?  ")
                if "leav" in braveryAsk.lower():
                    print("That's the right call!")
                    braveryPoints+=1
                    print("Let's go to the entrance now.")
                    musicPlayer = "entranceClassroom.mp3"
                    mixer.init() #Initialzing pyamge mixer
                    mixer.music.load(musicPlayer) #Loading Music File
                    mixer.music.play()
                    currentLocation = 0
                    actionCounter-=1
                else:
                    print("I'm sorry, that's not it...\n\n Time to go to the entrance now...")
                    musicPlayer = "entranceClassroom.mp3"
                    mixer.init() #Initialzing pyamge mixer
                    mixer.music.load(musicPlayer) #Loading Music File
                    mixer.music.play()
                    currentLocation = 0
                    actionCounter-=1
            if braveryPoints ==2 and currentLocation==2:
                braveryAsk = input("You see that the bear chasing you is a brown bear. Do you play dead? Or maybe try shouting back at it?  ")
                if "lie" or "pla" in braveryAsk.lower()and currentLocation == 2:  
                    print("That's the right call.\n\nYou've reached the max number of Bravery Points!\n\n Let's go to the entrance now.  ")  
                    braveryPoints+=1
                    print("Let's go to the entrance now.")
                    musicPlayer = "entranceClassroom.mp3"
                    mixer.init() #Initialzing pyamge mixer
                    mixer.music.load(musicPlayer) #Loading Music File
                    mixer.music.play()
                    currentLocation = 0
                    actionCounter-=1
                else:
                    print("I'm sorry, that's not it...\n\n Time to go to the entrance now...")
                    musicPlayer = "entranceClassroom.mp3"
                    mixer.init() #Initialzing pyamge mixer
                    mixer.music.load(musicPlayer) #Loading Music File
                    mixer.music.play()
                    currentLocation = 0
                    actionCounter-=1
        if "mov" in whereToGoFromBravery.lower():
            directionFromBravery = input("\nAlright then, what direction do you wanna go in?  ")
            if "nor" in directionFromBravery.lower():
                print("\nThere is a wall here.\n")
                directionFromBravery = input("\nWhich direction do you wanna go in?  ")
            if "eas" in directionFromBravery.lower():
                print("\nThere is a wall here.\n")
                directionFromBravery = input("\nWhich direction do you wanna go in?  ")
            if "wes" in directionFromBravery.lower():
                musicPlayer = "entranceClassroom.mp3"
                mixer.init() #Initialzing pyamge mixer
                mixer.music.load(musicPlayer) #Loading Music File
                mixer.music.play()
            if "sou" in directionFromBravery.lower():
                print("\nThere is a wall here.\n")
                directionFromBravery = input("\nWhich direction do you wanna go in?  ")
        if "day" in whereToGoFromBravery.lower() or "acti" in whereToGoFromBravery.lower():
            print("Action Points")
            print(actionCounter)
            print("Day number")
            print(dayCounter)
            currentLocation = 2
    if currentLocation == 3:
        whereToGoFromLuck = input("\nWhat do want to do, move or test your luck?  ")
        if "luck" in whereToGoFromLuck.lower() or "test" in whereToGoFromLuck.lower():
            print("\The computer will pick a number between 1 and 3. If you have the same number as the computer, you win! Otherwise, you lose... \n")
            computerPick = random.randint (1,3)
            playerPick = input("\nPick your number:  ")
            if playerPick == computerPick:
                luckPoints+=1
                print("\nYou got it right!\n")
            else:
                print("\nI'm afraid you didn't get it....  ")
            print("\nNow that the luck test is done, let's go to the entrance\n")
            actionCounter -=1
            musicPlayer = "entranceClassroom.mp3"
            mixer.init() #Initialzing pyamge mixer
            mixer.music.load(musicPlayer) #Loading Music File
            mixer.music.play()
            currentLocation = 0
        if "mov" in whereToGoFromLuck.lower():
            directionFromLuck = input("\nAlright then, what direction do you wanna go in?  ")
            if "wes" in directionFromLuck.lower():
                print("\nThere is a wall here.\n")
                directionFromLuck = input("\nWhich direction do you wanna go in?  ")
            if "eas" in directionFromLuck.lower():
                print("\nThere is a wall here.\n")
                directionFromLuck = input("\nWhich direction do you wanna go in?  ")
            if "nor" in directionFromLuck.lower():
                musicPlayer = "entranceClassroom.mp3"
                mixer.init() #Initialzing pyamge mixer
                mixer.music.load(musicPlayer) #Loading Music File
                mixer.music.play()
                currentLocation = 0   
            if "sou" in directionFromLuck.lower():
                print("\nThere is a wall here.\n")
                directionFromLuck = input("\nWhich direction do you wanna go in?  ")
        if "day" in whereToGoFromLuck.lower() or "acti" in whereToGoFromLuck.lower():
            print("Action Points")
            print(actionCounter)
            print("Day number")
            print(dayCounter)
            currentLocation = 3
    if "y" in earlyAcessToJeremysHouse.lower():
        mixer.music.stop()
        mixer.init() #Initialzing pyamge mixer
        mixer.music.load('RiddleBattle.mp3') #Loading Music File
        mixer.music.play()
        print("You have")
        print(riddlePoints)
        print("riddle points")
        print(braveryPoints)
        print("bravery points")
        print(luckPoints)
        print("luck points\n")
        print("\nI wish you the best of luck.\n")
#This is a little easter egg, essentially, if you take the risk of going early, you get an easier riddle
        print("\nJeremy: Wow, you came early! Let's start!\n")

        lastRiddle = input("\nHow many provinces and territories are there in Canada?  ")

        if "13" in lastRiddle:

            print("\nOh wow, you beat me! Joseph told me of how you trained, and how nervous you were coming here. \n\n You took a big risk, but it payed off. I'm really proud of you, especially of yur ability to take risks!\n\n\n THE END")
            whereInGame = 5
        else:
            print("\nI'm sorry, you didn't win... It's alright though, I'm still really proud of you coming here, especially early.\n You took a risk, and I'm proud of you for it... You're awesome!\n\n\n THE END")
            whereInGame = 5
    else:
        musicPlayer = "entranceClassroom.mp3"
        mixer.init() #Initialzing pyamge mixer
        mixer.music.load(musicPlayer) #Loading Music File
        mixer.music.play()
        entranceWelcome=art.text2art("Entrance\n\n")
        print (entranceWelcome)
        currentLocation = 0
                
while whereInGame ==4:
    #This is essentially the common ending, with the riddle difficulty being based on bravery points. The idea is that you take the risk of going into it with less luck points and riddle points, you have more time for bravery points, which in this case are more important. 
    mixer.music.stop()
    mixer.init() #Initialzing pyamge mixer
    mixer.music.load('RiddleBattle.mp3') #Loading Music File
    mixer.music.play()
    print("\n\nThe ten days are done! You have:")
    print(riddlePoints)
    print("riddle points")
    print(braveryPoints)
    print("bravery points")
    print(luckPoints)
    print("luck points\n")
    print("\nIt's time to go to Jeremy's house\nI wish you the best of luck.")

    print("\nJeremy: \nHey man, how are you?\n Let's start the battle shall we?\n Get ready for the first riddle.")

    if braveryPoints<2:
        lastRiddleOnNormalEnding = input("\nWhat is the capital of Ontario?  ")
    else:
        lastRiddleOnNormalEnding = input("\nIs baking soda an acid or a base?  ")

    if "bas" or "toron" in lastRiddleOnNormalEnding.lower():

        print("\nOh wow, you beat me! Joseph told me of how you trained, and how nervous you were coming here. \n\n You took a big risk, but it payed off. I'm really proud of you, especially of yur ability to take risks!\n\n\n THE END")
    else:
        print("\nI'm sorry, you didn't win... It's alright though, I'm still really proud of you coming here.\n You took a risk, and I'm proud of you for it... You're awesome!\n\n\n THE END")
    whereInGame=5

while whereInGame==5:

    lastAndFinalInput = input("You can continue listening to the music if you like, by just leaving this input blank. If not, type anything.")
    print("THAT'S ALL FOLKS")
    mixer.music.stop()
    input("")
    #That's all folks!