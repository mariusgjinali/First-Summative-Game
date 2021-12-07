#G. Wu
#November 10, 2021
#Collects info from the player and stores them in a list
#parameters: none
#precondition: none
#result: saves info in a list and returns the list, you can take any info from the list using the index.
#return value: none

def getUserInfo():
    userName = input(str("What is your name? "))
    userAge = input("How old are you? ")
    favColour = input(str("What is your favorite colour? ")) #input Marius wants for his game
    favAnimal = input(str("What is your favorite animal? ")) #input Marius wants for his game
    infoList = [userName, userAge, favColour, favAnimal]
    return infoList
