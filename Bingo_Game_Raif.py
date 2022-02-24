'''
This program is a bingo game. In this program users can select the number of plays they would like.
There may be 1 - 3 players playing at the same time. Once players are selected, a 5 by 5 bingo card
is generated for the players. Users can than select the game mode they would like to play, it can
be either full card, single line or four corners. Once game mode is selected, users can input
when a new bingo word should be generated, as its generated the word is checked with each players
card, if found the word on the card is changed to FOUND. Once the requirement for the chosen game
mode is met, a winner is declared. There can be more than one winner.

Author: Raif Rizwan Karkal
Student Number: 20261498
Date: 28th Nov 2021
'''

# imports used within program
import urllib.request
import ssl
import random

ssl._create_default_https_context = ssl._create_unverified_context


def bingo_list():
    """
    This function is responsible for reading through the list of words on the given url.
    It will then add the words to a list which can than be used within the program. The
    function returns the list.

    Parameters:  None
    Return Value: Bingo_word_list
     """

    # Reading through the given url and assigning the whole content to variable response
    response = urllib.request.urlopen("https://research.cs.queensu.ca/home/cords2/bingo.txt")
    # each line of the content is assigned to variable html
    html = response.readline()

    # assigning empty list for use in program
    bingo_word_list = []

    # while loop used. The while make sure each line of html is not zero. If its zero, loop has gone through each line.
    while len(html) != 0:

        # each line of variable html is decoded
        data = html.decode('utf-8')
        # the words (data) is than appended into bingo word list. The last part of each word is removed as it displays "\n"
        bingo_word_list.append(data[:-1])
        # the next line of the url is read and stored to variable html
        html = response.readline()


    return bingo_word_list


def player_dictionary (bingo_word_list):
    """
    This function is responsible for determining how many players are in the game and there names.
    Based on those given information from user, a dictionary is created with the key being the names.
    The values of the dictionary are randomly generated 25 bingo words for each player.

    Parameters:  order_queue, food_price, food_item_list
    Return Value: None
     """

    # assigning empty dictionary to a variable
    player_bingo_dictionary = {}
    # assigning empty list to a variable
    bingo_word_player = []

    # asking user how many users are playing
    print("How many users are playing Bingo? ")
    # number input is saved to a variable
    num_of_players = int(input("> "))

    # for loop in which variable i is assigned number from range 1 to the number of players + 1 due to for loop
    for i in range(1, num_of_players + 1):
        # user asked for names of each players
        print("Input the name of player" +" " + str(i ))
        # players name saved as a variable
        name_of_player = input("> ")

        # while loop which runs until the length of the bingo word player exceeds 25 words
        while len(bingo_word_player) < 26:
            # randomly generating a word from the bingo word list and assigning to a variable
            word = random.choice(bingo_word_list)
            # if word generated does not already exist in the bingo word player list, program continues
            if word not in bingo_word_player:
                # bingo word player list appended with word
                bingo_word_player.append(word)

        # dictionary appended with keys as player names and values as the random generated bingo words
        player_bingo_dictionary[name_of_player] = bingo_word_player
        # bingo word player list empty again in order to add bingo word for the next player
        bingo_word_player = []

    # returning the bingo dictionary
    return player_bingo_dictionary


def bingo_user_interface_format (bingo_dictionary ):
    """
    This function is responsible for displaying the user interface. It uses the information
    in the bingo dictionary and creates a 5 by 5 grid card as the user interface.

    Parameters:  bingo_dictionary
    Return Value: None
     """

    # for loop in which variable names is assigned to each keys in the bingo dictionary
    for names in bingo_dictionary.keys():

        # printing name of player and cards
        print(names+"'s", "cards: ")

        # for loop in which variable counter assigned number from range 0 to 5
        for counter in range(0, 5):
            # the word generated from the bingo_dictionary with specific key (name) and index is assigned to a variable
            word = bingo_dictionary[names][counter]
            # the word is printed with a tab as the ending
            print(str(word), end="\t")

        # an extra print statement for spacing
        print("")

        # for loop in which variable counter2 assigned number from range 5 to 10
        for counter2 in range(5, 10):
            # the word generated from the bingo_dictionary with specific key (name) and index is assigned to a variable
            word2 = bingo_dictionary[names][counter2]
            # the word is printed with a tab as the ending
            print(str(word2), end="\t")

        # an extra print statement for spacing
        print("")

        # for loop in which variable counter3 assigned number from range 10 to 15
        for counter3 in range(10, 15):
            # the word generated from the bingo_dictionary with specific key (name) and index is assigned to a variable
            word3 = bingo_dictionary[names][counter3]
            # the word is printed with a tab as the ending
            print(str(word3), end="\t")

        # an extra print statement for spacing
        print("")

        # for loop in which variable counter4 assigned number from range 15 to 20
        for counter4 in range(15, 20):
            # the word generated from the bingo_dictionary with specific key (name) and index is assigned to a variable
            word4 = bingo_dictionary[names][counter4]
            # the word is printed with a tab as the ending
            print(str(word4), end="\t")

        # an extra print statement for spacing
        print("")

        # for loop in which variable counter5 assigned number from range 20 to 25
        for counter5 in range(20, 25):
            # the word generated from the bingo_dictionary with specific key (name) and index is assigned to a variable
            word5 = bingo_dictionary[names][counter5]
            # the word is printed with a tab as the ending
            print(str(word5), end="\t")

        # an extra print statement for spacing
        print("")
        print("")

    # returning back to the function that called this function
    return


def bingo_winning_format (names, bingo_dictionary):
    """
    This function is responsible for displaying the user interface when a player
    or players win. The format is the same 5 by 5 grid card however, only the
    winner player(s) cards are printed with there names.

    Parameters:  keys, bingo_dictionary
    Return Value: None
     """

    # printing the name of which the card that won, belongs to
    print(names+"'s", "Cards:")

    # for loop in which variable counter is assigned range 0 to 5
    for counter in range(0, 5):
        # the word generated from the bingo_dictionary with specific key (name) and index is assigned to a variable
        word = bingo_dictionary[names][counter]
        # the word is printed with a tab as the ending
        print(str(word), end="\t")

    # an extra print statement for spacing
    print("")

    # for loop in which variable counter2 is assigned range 5 to 10
    for counter2 in range(5, 10):
        # the word generated from the bingo_dictionary with specific key (name) and index is assigned to a variable
        word2 = bingo_dictionary[names][counter2]
        # the word is printed with a tab as the ending
        print(str(word2), end="\t")

    # an extra print statement for spacing
    print("")

    # for loop in which variable counter3 is assigned range 10 to 15
    for counter3 in range(10, 15):
        # the word generated from the bingo_dictionary with specific key (name) and index is assigned to a variable
        word3 = bingo_dictionary[names][counter3]
        # the word is printed with a tab as the ending
        print(str(word3), end="\t")

    # an extra print statement for spacing
    print("")

    # for loop in which variable counter4 is assigned range 15 to 20
    for counter4 in range(15, 20):
        # the word generated from the bingo_dictionary with specific key (name) and index is assigned to a variable
        word4 = bingo_dictionary[names][counter4]
        # the word is printed with a tab as the ending
        print(str(word4), end="\t")

    # an extra print statement for spacing
    print("")

    # for loop in which variable counter2 is assigned range 20 to 25
    for counter5 in range(20, 25):
        # the word generated from the bingo_dictionary with specific key (name) and index is assigned to a variable
        word5 = bingo_dictionary[names][counter5]
        # the word is printed with a tab as the ending
        print(str(word5), end="\t")

    # an extra print statement for spacing
    print("")
    print("")

    # printing the name of the winners
    print(names, "Wins!")
    # returning back to the function that called this function
    return


def full_card (caller_word, bingo_dictionary, winner_option):
    """
    This function represents one of the 3 game modes available in this bingo program.
    The full_card game mode looks through each players card after a word is generate
    and determines if all 25 words in the player(s) card are found they are declared as a winner.
    There can be multiple winners.

    Parameters: caller_word, bingo_dictionary, winner_option
    Return Value: winner_option
    """

    # for loop in which variable names assigned to each key bingo dictionary keys
    for names in bingo_dictionary.keys():
        # for loop, in which variable counter assigned from range 0 to 25
        for counter in range(0, 25):
            # fetching words in the bingo dictionary for specific names and index
            word = bingo_dictionary[names][counter]

            #  if word equals to the caller word program continues here
            if word == caller_word:
                # the specific word in the specific key and index is changed to FOUND
                bingo_dictionary[names][counter] = "FOUND"

                # if the number of word FOUND in the specific key list is equal to 25, means all words in the card is found.
                if bingo_dictionary[names].count("FOUND") == 25:
                    # bingo winning format function is called with names and bingo dictionary as parameter
                    bingo_winning_format(names, bingo_dictionary)
                    # winner option status is turned into true
                    winner_option = True

    # if winner option is equal to false, program continues here
    if winner_option == False:
        # calling bingo user interface format function with bingo dictionary as parameter
        bingo_user_interface_format(bingo_dictionary)

    # returning winner option variable
    return winner_option


def single_line(caller_word,bingo_dictionary,winner_option):
    """
    This function represents one of the 3 game modes available in this bingo program.
    The single_line game mode looks through each players card after a word is generated
    and determines if all words in a row or column of the card is found.
    If it is, a winner is declared. There can be multiple winners.


    Parameters: caller_word, bingo_dictionary, winner_option
    Return Value: winner_option
    """

    for names in bingo_dictionary.keys():
        # for loop, in which variable counter assigned from range 0 to 25
        for counter in range(0, 25):
            # fetching words in the bingo dictionary for specific names and index
            word = bingo_dictionary[names][counter]

            #  if word equals to the caller word program continues here
            if word == caller_word:
                # the specific word in the specific key and index is changed to FOUND
                bingo_dictionary[names][counter] = "FOUND"

                # if the word generated from the specific key and index is equal to FOUND for index 0,1,2,3,4, program continues
                if bingo_dictionary[names][0] == "FOUND" and bingo_dictionary[names][1] == "FOUND" and \
                        bingo_dictionary[names][2] == "FOUND" and bingo_dictionary[names][3] == "FOUND" and \
                        bingo_dictionary[names][4] == "FOUND":

                    # calling bingo winning format, with parameter names and bingo dictionary. This print the winning format
                    bingo_winning_format(names, bingo_dictionary)
                    # winner option variable assigned to True indicating a winner is found
                    winner_option = True

                    # returning winner option variable
                    return winner_option

                # if the word generated from the specific key and index is equal to FOUND for index 5,6,7,8,9, program continues
                if bingo_dictionary[names][5] == "FOUND" and bingo_dictionary[names][6] == "FOUND" and \
                        bingo_dictionary[names][7] == "FOUND" and bingo_dictionary[names][8] == "FOUND" and \
                        bingo_dictionary[names][9] == "FOUND":

                    # calling bingo winning format, with parameter names and bingo dictionary. This print the winning format
                    bingo_winning_format(names, bingo_dictionary)
                    # winner option variable assigned to True indicating a winner is found
                    winner_option = True

                    # if winner option remains false program continues here
                    if winner_option == False:
                        # bingo user interface format function is called with bingo dictionary as parameter.
                        bingo_user_interface_format(bingo_dictionary)

                    # returning winner option variable
                    return winner_option

                # if the word generated from the specific key and index is equal to FOUND for index 10,11,12,13,14, program continues
                if bingo_dictionary[names][10] == "FOUND" and bingo_dictionary[names][11] == "FOUND" and \
                        bingo_dictionary[names][12] == "FOUND" and bingo_dictionary[names][13] == "FOUND" and \
                        bingo_dictionary[names][14] == "FOUND":

                    # calling bingo winning format, with parameter names and bingo dictionary. This print the winning format
                    bingo_winning_format(names, bingo_dictionary)
                    # winner option variable assigned to True indicating a winner is found
                    winner_option = True

                    # if winner option remains false program continues here
                    if winner_option == False:
                        # bingo user interface format function is called with bingo dictionary as parameter.
                        bingo_user_interface_format(bingo_dictionary)

                    # returning winner option variable
                    return winner_option

                # if the word generated from the specific key and index is equal to FOUND for index 15,16,17,18,19, program continues
                if bingo_dictionary[names][15] == "FOUND" and bingo_dictionary[names][16] == "FOUND" and \
                        bingo_dictionary[names][17] == "FOUND" and bingo_dictionary[names][18] == "FOUND" and \
                        bingo_dictionary[names][19] == "FOUND":

                    # calling bingo winning format, with parameter names and bingo dictionary. This print the winning format
                    bingo_winning_format(names, bingo_dictionary)
                    # winner option variable assigned to True indicating a winner is found
                    winner_option = True

                    # if winner option remains false program continues here
                    if winner_option == False:
                        # bingo user interface format function is called with bingo dictionary as parameter.
                        bingo_user_interface_format(bingo_dictionary)

                    # returning winner option variable
                    return winner_option

                # if the word generated from the specific key and index is equal to FOUND for index 20,21,22,23,24, program continues
                if bingo_dictionary[names][20] == "FOUND" and bingo_dictionary[names][21] == "FOUND" and \
                        bingo_dictionary[names][22] == "FOUND" and bingo_dictionary[names][23] == "FOUND" and \
                        bingo_dictionary[names][24] == "FOUND":

                    # calling bingo winning format, with parameter names and bingo dictionary. This print the winning format
                    bingo_winning_format(names, bingo_dictionary)

                    # winner option variable assigned to True indicating a winner is found
                    winner_option = True

                    # returning winner option variable
                    return winner_option

    # equating row variable to zero
    row = 0
    # equating counter variable to zero
    counter = 0

    # while loop in which while row value is less than zero loop continues
    while row != 5:

        # checking if the first row word is == found, if it is program continues here
        if bingo_dictionary[names][row] == "FOUND":

            # for loop in which variable i assigned from row to row + 21 in steps of 5. This is used to loop through each vertical line
            for i in range (row, row+21, 5):

                # if statement, if word generated by the specific key and index is equal to found program continues
                if bingo_dictionary[names][i] == "FOUND":
                    # counter variable increased by one
                    counter += 1

        # if statement, if counter equal 5 which means when all 5 words in a row or column is found program continues
        if counter == 5:

            # calling bingo winning format, with parameter names and bingo dictionary. This print the winning format
            bingo_winning_format(names, bingo_dictionary)

            # winner option variable assigned to True indicating a winner is found
            winner_option = True

            # returning winner option variable
            return winner_option

        # else statement, if not all words are found than counter is set back to zero and the row is increased by one to switch to the next row.
        else:
            counter = 0
            row = row + 1

    # if winner option remains false program continues here
    if winner_option == False:

        # bingo user interface format function is called with bingo dictionary as parameter.
        bingo_user_interface_format(bingo_dictionary)

        # returning winner option variable
        return winner_option


def four_corners (caller_word, bingo_dictionary, winner_option):
    """
    This function represents one of the 3 game modes available in this bingo program.
    The four_corners game mode looks through each players card after a word is generated
    and determines if each word in the four corners of a card is found.
    If it is, a winner is declared. There can be multiple winners.


    Parameters: caller_word, bingo_dictionary, winner_option
    Return Value: winner_option
    """

    # for loop, variable names assigned to each key in the dictionary, the keys represent names
    for names in bingo_dictionary.keys():

        # if the word in the specific dictionary key and list index equals to the caller word, program continues
        if bingo_dictionary[names][0] == caller_word:
            # the specific word that was found in the list, is changed to word FOUND
            bingo_dictionary[names][0] = "FOUND"

        # if the word in the specific dictionary key and list index equals to the caller word, program continues
        if bingo_dictionary[names][4] == caller_word:
            # the specific word that was found in the list, is changed to work FOUND
            bingo_dictionary[names][4] = "FOUND"

        # if the word in the specific dictionary key and list index equals to the caller word, program continues
        if bingo_dictionary[names][20] == caller_word:
            # the specific word that was found in the list, is changed to work FOUND
            bingo_dictionary[names][20] = "FOUND"

        # if the word in the specific dictionary key and list index equals to the caller word, program continues
        if bingo_dictionary[names][24] == caller_word:
            # the specific word that was found in the list, is changed to work FOUND
            bingo_dictionary[names][24] = "FOUND"

        # if specific dictionary key and list index stated (0, 4, 20, 24) equal to FOUND the program continues here. The index stated are the four corners of the card
        if bingo_dictionary[names][0] == "FOUND" and bingo_dictionary[names][4] == "FOUND" and bingo_dictionary[names][20] == "FOUND" and bingo_dictionary[names][24] == "FOUND":
            # calling bingo winning format, with parameter names and bingo dictionary. This print the winning format
            bingo_winning_format(names, bingo_dictionary)
            # winner option variable assigned to True indicating a winner is found
            winner_option = True

    # if winner option remains false program continues here
    if winner_option == False:
        # bingo user interface format function is called with bingo dictionary as parameter.
        bingo_user_interface_format(bingo_dictionary)

    # returning winner option variable
    return winner_option


def main():
    """
    The main function controls the program flow. This is where execution will start. The main function
    also holds some of the user interface that is displayed to the user. Furthermore, different
    functions are called from the main function.

    Parameters: None
    Return: None
    """

    # creating a variable round option and setting default option to Y
    round_option = "Y"
    # calling bingo_list function which is a list of all the bingo words, return list is assigned to a variable
    bingo_word_list = bingo_list()

    # while loop, while the round option is "Y" the loop continues
    while round_option == "Y":
        # Winner option variable declared and set to false as no winner is declared
        winner_option = False

        # calling player_dictionary function which creates the dictionary of players. Assigning the bingo word list as parameter. Return value assigned to a variable
        bingo_dictionary = player_dictionary(bingo_word_list)
        #calling bingo user interface format function for user interface. Assigning bingo dictionary as parameter.
        bingo_user_interface_format(bingo_dictionary )

        # printing a list of game modes for user to select
        print ("Which game mode would you like? \n"
               "1. Full Card \n"
               "2. Single Line \n"
               "3. Four Corners \n")
        # asking user to select a game mode number
        game_mode_input = int(input("choose a number: "))

        # asking user if they would like to call an item (word) from the bingo word list
        print("Would you like to call an item for bingo game? (Y for yes and N for no)")
        # user input saved in variable
        caller_option = input("> ").upper()

        # declaring a empty list to caller word list, in order to keep track of all the words that were called.
        caller_word_list = []

        # if caller option is Y the while loop begins here.
        while caller_option == "Y":
            # generating a random word from the bingo word list. assigning word to caller word
            caller_word = random.choice(bingo_word_list)

            # if caller word generated is in the caller word list, loop begins until a word is found that is not in the list
            while caller_word in caller_word_list:
                caller_word = random.choice(bingo_word_list)

            # if statement, if caller word not in caller word list, word printed and appended to the list. program continues
            if caller_word not in caller_word_list:
                print(caller_word)
                caller_word_list.append(caller_word)

            # if game_mode chosen is 1 program continues here
            if game_mode_input == 1:
                # full card function called with caller word, bingo dictionary and winner option as parameter. Return value assigned to updated winner option
                updated_winner_option = full_card(caller_word, bingo_dictionary,winner_option)

                # if updated winner option remains false, program continues here
                if updated_winner_option == False:
                    # asking user if they would like to print another item (word) from bingo word list.
                    print("Would you like to call an item for bingo game? (Y for yes and N for no) ")
                    # option selected by user saved as a variable
                    caller_option = input("> ").upper()

                # if updated winner option equal to true, caller option is set to N as a winner is selected.
                if updated_winner_option == True:
                    caller_option = "N"

            # if game_mode chosen is 2 program continues here
            if game_mode_input == 2:
                updated_winner_option = single_line(caller_word, bingo_dictionary, winner_option)

                # if updated winner option remains false, program continues here
                if updated_winner_option == False:
                    # asking user if they would like to print another item (word) from bingo word list.
                    print("Would you like to call an item for bingo game? (Y for yes and N for no) ")
                    # option selected by user saved as a variable
                    caller_option = input("> ").upper()

                # if updated winner option equal to true, caller option is set to N as a winner is selected.
                if updated_winner_option == True:
                    caller_option = "N"

            # if game mode chosen is 3 program continues here.
            if game_mode_input == 3:
                # four corners function called with caller word, bingo dictionary and winner option as parameter. Return value assigned to updated winner option
                updated_winner_option = four_corners(caller_word, bingo_dictionary,winner_option)

                # if updated winner option remains false. program continues here
                if updated_winner_option == False:
                    # user informed if they would like to print another item (word) bingo word list
                    print("Would you like to call an item for bingo game? (Y for yes and N for no) ")
                    # option selected by user is saved as a variable
                    caller_option = input("> ").upper()

                # if updated winner option is true, a winner is selected hence caller option is set to N to end round
                if updated_winner_option == True:
                    caller_option = "N"

        # user asked if they would like to play another round, depending on option either the game will reset and start again or end
        round_option = input("Would you like to play another round (Y for yes or N for no):").upper()

# calling main function for the program to begin
main()









