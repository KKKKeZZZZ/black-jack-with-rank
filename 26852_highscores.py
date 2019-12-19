#
# File:      26852_highscores.py
# Author:    Ke Zhang
# SAIBT Id:  26852
# Version:   1.0  10 May 2017
# Description: Assignment 2 part II
#   This is my own work as defined by the University's
#   Academic Misconduct policy.
#
import blackjack_26852

#function read_file
def read_file(filename,player_names,player_scores):
    file = open(filename,"r")
    index = 0
    txt = file.readline()
    
    #read the file and change to the list
    while txt != "":
        txtList = []
        txtList = txt.split()
        player_names[index] = txtList[0] + " " + txtList[1]
        player_scores[index] = int(txtList[2])
        txt = file.readline()
        index += 1
    file.close()

#function display_high_scores
def display_high_scores(player_names, player_scores):
    index = 0

    #print the scores form
    print("\n\n*****************************************************")
    print("******************    Blackjack    ******************")
    print("******************   HIGH SCORES   ******************")
    print("*****************************************************")
    print("*      Player Name                      Score       *")
    print("*****************************************************")
    print("*---------------------------------------------------*")
    
    #print the resault line by line
    for item in range(5):
        
        #print ? for no name in the hall
        if player_names[index] == "":
            print(format("*", '<6s'),format("????????",'<32s'),format(player_scores[index], '<11d'),"*")
            print("*---------------------------------------------------*")
        else:
            print(format("*", '<6s'),format(player_names[index],'<32s'),format(player_scores[index], '<11d'),"*")
            print("*---------------------------------------------------*")
        index += 1
    print("*****************************************************")

#function is_high_scores
def is_high_score(player_scores, new_score):
    index = 4
    position = -1

    #check if the score is a high enough and what position it should be
    for num in player_scores:
        if new_score >= player_scores[index]:
            position = index
        index -= 1
    return position

#function write_to_file
def write_to_file(filename, player_names, player_scores):
    
    #open and writer to the file
    outfile = open(filename,"w")
    index = 0
    
    for num in range(len(player_names)):
        if player_names[index] != "":
            outfile.write(player_names[index] + " " +str(player_scores[index]))
            outfile.write("\n")
        else:
            outfile.write("\n")
        index += 1
    outfile.close()

#function find_player    
def find_player(player_names, name):
    index = 0
    insert_num = -1

    #check the name in high scores or not if so where it is 
    for names in player_names:
        if name == player_names[index]:
            insert_num = index
        index += 1
    return insert_num

#function add_player
def add_player(player_names, player_scores, new_name, new_score, insert_position):
    nameIndex = 4 
    scoreIndex = 4

    #change the list with the new name in the right position
    for num in range(5 - insert_position):
        if insert_position != 4:
            player_scores[scoreIndex] = new_score
        if insert_position != 4:
            if insert_position == scoreIndex:
                player_scores[scoreIndex] = new_score
            else:
                player_scores[scoreIndex] = player_scores[scoreIndex - 1]
        scoreIndex -= 1
        
    #change the list with the new score in the right position
    for num in range(5 - insert_position):
        if insert_position != 4:
            player_names[nameIndex] = new_name
        if insert_position != 4:
            if insert_position == nameIndex:
                player_names[nameIndex] = new_name
            else:
                player_names[nameIndex] = player_names[nameIndex - 1]
        nameIndex -= 1
    return len(player_scores)
    
################main program##################

player_name = ["","","","",""]
player_score = [0,0,0,0,0,]

#call read_file
filenames = "high_scores.txt"
read_file(filenames,player_name,player_score)

#start
ask = input("Please enter command [scores, search, play, quit]: ")

#error check for menu command
while ask != 'scores' and ask != 'search' and ask != 'play' and ask != 'quit':
    print("\nNot a valid command - please try again.")
    ask = input("\nPlease enter command [scores, search, play, quit]: ")

# the menu
while ask != "quit":

    #the play section
    if ask == 'play':

        #play blackjack in part I
        newScore = blackjack_26852.play_blackjack()
        #call is_high_score
        insertPosition = is_high_score(player_score,newScore)

        #the result about if this player can join the hall
        if insertPosition != -1:
            print("\nCongratulations! You have made it into the BlackJack Hall of Fame!")
            newName = input("\nPlease enter your name: ")
            add_player(player_name, player_score, newName, newScore, insertPosition)
            print("\nSuccessfully added Homer Simpson to BlackJack Hall of Fame.\n")
        else:
            print("\nSorry - you did not make it into the BlackJack Hall of Fame!\n")

    #the scores section
    elif ask == 'scores':
        #call display_high_scores
        display_high_scores(player_name, player_score)

    #the search section
    elif ask == 'search':
        searchName = input("\nPlease enter player's name: ")
        #call find_player function
        insertNum = find_player(player_name, searchName)
        
        #the result about if the player in the list or not if so show the score
        if insertNum != -1:
            print("")
            print(player_name[insertNum],"has a high score of",player_score[insertNum])
        else:
            print("")
            print(searchName,"does not have a high scores entry.")
            print("")
            
    ask = input("\nPlease enter command [scores, search, play, quit]: ")
    while ask != 'scores' and ask != 'search' and ask != 'play' and ask != 'quit':
        print("\nNot a valid command - please try again.\n")
        ask = input("\nPlease enter command [scores, search, play, quit]: ")

#the quit section
print("\nGoodbye - thanks for playing!")
print("\nNOTE: Your program should output the following information to a file called new_scores.txt.\n")
index = 0
for name in player_name:
    if player_name[index] != "":
        print(player_name[index] + " " +str(player_score[index]))

    index += 1
print("")

#call write_to_file function to store the final resault
outputFileName = "new_scores.txt"
write_to_file(outputFileName, player_name, player_score)
        
