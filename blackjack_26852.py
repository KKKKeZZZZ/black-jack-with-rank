#
# File:      26852_blackjack.py
# Author:    Ke Zhang
# SAIBT Id:  26852
# Version:   1.0  11 April 2017
# Description: Assignment 2 part I
#   This is my own work as defined by the University's
#   Academic Misconduct policy.
#
import random

#function get_choice
def get_choice():
    print("|")
    answer = input("| Please choose to hit or stand (h/s): ")
    while answer != "s" and answer != "h":
        answer = input("| Please choose to hit or stand (h/s): ")

    return answer
def deal_players_hand():
    scoreMan = 0
    dice1 = random.randint(1,10)
    dice2 = random.randint(1,10)
    scoreMan += dice1 + dice2
    
    if scoreMan <= 21:
        if dice1 == dice2 == 1:
            scoreMan -= dice1
            dice1 = 11
            scoreMan += dice1
        elif dice1 == 1:
            scoreMan -= dice1
            dice1 = 11
            scoreMan += dice1
        elif dice2 == 1:
            scoreMan -= dice2
            dice2 = 11
            scoreMan += dice2
    print("| Player hand:",dice1,"+",dice2,"=",scoreMan)

    #call get_choice
    ask = get_choice()
    #the limit of player's score
    if scoreMan < 15 and ask == "s":
        print("| Cannot stand on value less than 15!")
        ask = get_choice()
        
    while ask != "s" :
        dice1 = random.randint(1,10)
        if scoreMan + 11 <= 21 and dice1 == 1 :
            dice1 = 11
        scoreMan += dice1
        
        print("| Player hand:",scoreMan - dice1,"+",dice1,"=",scoreMan)
        # when to bust
        if scoreMan >21:
            print("| PLAYER BUSTS!")
            ask = "s"
        else:
            ask = get_choice()
            dice1 = random.randint(1,10)
            if scoreMan < 15 and ask == "s":
                print("| Cannot stand on value less than 15!")
                ask = get_choice()
     
    return scoreMan

#function deal_dealers_hand
def deal_dealers_hand(scoreCom):
    dice3 = random.randint(1,10)
    print("|")

    #the limit of computer's score
    while scoreCom < 17:
        dice3 = random.randint(1,10)
        if scoreCom + 11 <= 21 and dice3 == 1 :
            dice3 = 11
        scoreCom += dice3
        
        if scoreCom > 21:
            print("| Dealer hand:",scoreCom - dice3,"+",dice3,"=",scoreCom)
            print("| DEALER BUSTS!")
            print("|")
        else:
            print("| Dealer hand:",scoreCom - dice3,"+",dice3,"=",scoreCom)
    print("|")
    return scoreCom

#function determine_winner
def determine_winner(scoreMan,scoreCom):
    finalScore = 0

    #three situation
    if scoreMan <= 21 and scoreCom <= 21 :
        if scoreMan < scoreCom:
            winner = "*** Dealer Wins! ***"
            
        elif scoreMan > scoreCom:
            winner = "*** Player Wins! ***"
        else:
            winner = "*** Push - no winners. ***"
    elif scoreMan<=21 and scoreCom > 21:
        winner = "*** Player Wins! ***"
    else:
        winner = "*** Dealer Wins! ***"
    
    print("| Dealer =",scoreCom,"Player =",scoreMan,winner)

    #to get the final score
    if winner == "*** Player Wins! ***":
        finalScore = 3
    elif winner == "*** Dealer Wins! ***":
        finalScore = 0
    else:
        finalScore = 1
    return finalScore

#function play_blackjack
def play_blackjack():
    totalScore = 0
    scorePc = 0
    dice3 = random.randint(1,10)
    scorePc += dice3
    if scorePc <= 21 and dice3 == 1:
        scorePc -= dice3
        dice3 = 11
        scorePc += dice3
        
    #main process of the game
    print("---------------------- START GAME ----------------------")
    print("| Dealer hand:",scorePc)
    
    # call the functions
    scoreHuman = deal_players_hand()
    scoreComputer = deal_dealers_hand(scorePc)
    scoreFinal = determine_winner(scoreHuman,scoreComputer)
    
    print("----------------------- END GAME -----------------------\n")
    totalScore += scoreFinal

    #show the final score and ask the game to continue or not
    play = input("Your score: "+str(totalScore)+" - Play again [y|n]? ")

    #error check for invalid command
    while play != 'y' and play != 'n':
        play = input("Please enter y or n. Play again [y|n]? ")
    while play != 'n':
        print("\n")
        print("---------------------- START GAME ----------------------")
        print("| Dealer hand:",scorePc)
        
        scoreHuman = deal_players_hand()
        scoreComputer = deal_dealers_hand(scorePc)
        scoreFinal = determine_winner(scoreHuman,scoreComputer)
        
        print("----------------------- END GAME -----------------------\n")
        totalScore += scoreFinal
        play = input("Your score: "+str(totalScore)+" - Play again [y|n]? ")
        while play != 'y' and play != 'n':
            play = input("Please enter y or n. Play again [y|n]? ")
    return totalScore

########main program##########
##total = play_blackjack()
##
##print("\n\nYour score is:",total)

