# Importing Modules
import math
import random
import graphics

class Object:
    def __init__(self, Word, Cat, Diff, Len):
        self.Word = Word
        self.Cat = Cat
        self.Diff = Diff
        self.Len = Len

# Defining Functions
def validation(size):
    opt = []
    for count in range(1, size + 1):
        opt.append(str(count))

    ask = input("Select from the given options: ")
    while ask not in opt:
        print("INVALID INPUT!")
        ask = input("Please select from the given options: ")

    return ask

def start_screen():
    print("\n>> List of Available Operations: ")
    print("1) Choose a Category")
    print("2) Random Category")
    print("3) Exit the Game")

    user_selection = validation(3)
    return user_selection

def select_category():
    print("\n>> List of Available Categories: ")
    print("1) Name of Games")
    print("2) Name of Countries")
    print("3) Name of Cities")
    print("4) Name of Animals")
    print("5) Name of Personalities")

    return validation(5)

def choose_difficulty():
    print("\n>> Difficulty Level? ")
    print("1) Easy")
    print("2) Medium")
    print("3) Hard")
    print("4) Random")

    Ask = validation(4)
    DiffList = ["Easy", "Medium", "Hard"]

    if Ask == "1":
        return "Easy"
    elif Ask == "2":
        return "Medium"
    elif Ask == "3":
        return "Hard"
    elif Ask == "4":
        return random.choice(DiffList)

def choose_word(category, difficulty):
    Array = categories.get(category)
    potential_objects = []
    for a in Array:
        if a.Diff == difficulty:
            potential_objects.append(a)

    return random.choice(potential_objects)

def num_of_missing_char(word, difficulty):
    length = len (word)
    if difficulty == "Easy":
        missing = 3
        while (length - missing) < 5:
            missing -= 1
    elif difficulty == "Medium":
        missing = 7
        while (length - missing) < 3:
            missing -= 1
    elif difficulty == "Hard":
        missing = 20
        while (length - missing) < 2:
            missing -= 1

    return missing


# Initialising the Game
def set_difficulty(input_list, category):
    Easy = 0
    Medium = 0
    Hard = 0

    list_len = len(input_list)
    
    increment = (math.ceil(list_len / 3))
    sorted_list = sorted(input_list, key=len)

    for count in range(0, list_len):
        this_ele = sorted_list[count]
        if count <= increment:
            sorted_list[count] = Object(this_ele, category, "Easy", len(this_ele))
            Easy += 1
        elif count <= (increment * 2):
            sorted_list[count] = Object(this_ele, category, "Medium", len(this_ele))
            Medium += 1
        elif count <= (increment * 3):
            sorted_list[count] = Object(this_ele, category, "Hard", len(this_ele))                 

    return sorted_list

Word_Bank_Animals = []
with open("animals.txt", "r") as file:
    Word_Bank_Animals = file.readlines()
Word_Bank_Animals = [line.rstrip() for line in Word_Bank_Animals]
file.close()

Word_Bank_Games = []
with open("games.txt", "r") as file:
    Word_Bank_Games = file.readlines()
Word_Bank_Games = [line.rstrip() for line in Word_Bank_Games]
file.close()

Word_Bank_Countries = []
with open("countries.txt", "r") as file:
    Word_Bank_Countries = file.readlines()
Word_Bank_Countries = [line.rstrip() for line in Word_Bank_Countries]
file.close()

Word_Bank_Cities = []
with open("cities.txt", "r") as file:
    Word_Bank_Cities = file.readlines()
Word_Bank_Cities = [line.rstrip() for line in Word_Bank_Cities]
file.close()

Word_Bank_Personalities = []
with open("personalities.txt", "r") as file:
    Word_Bank_Personality = file.readlines()
Word_Bank_Personality = [line.rstrip() for line in Word_Bank_Personality]
file.close()
                    
Word_Bank_Games_Details = set_difficulty(Word_Bank_Games, "Games")
Word_Bank_Countries_Details = set_difficulty(Word_Bank_Countries, "Countries")
Word_Bank_Cities_Details = set_difficulty(Word_Bank_Cities, "Cities")
Word_Bank_Animals_Details = set_difficulty(Word_Bank_Animals, "Animals")
Word_Bank_Personality_Details = set_difficulty(Word_Bank_Personality, "Personalities")

# Setting up dictionaries
categories = {
    1: Word_Bank_Games_Details,
    2: Word_Bank_Countries_Details,
    3: Word_Bank_Cities_Details,
    4: Word_Bank_Animals_Details,
    5: Word_Bank_Personality_Details
}

# Main Program Loop
def main():
    interested = True
    while interested:
        # Start Screen and Game Mode
        start_screen_input = start_screen()
        if start_screen_input == "3":
            interested = False
            break
        elif start_screen_input == "2":
            game_category = random.randint(1, 5)
        elif start_screen_input == "1":
            game_category = int(select_category())

        # Selecting Difficulty
        game_difficulty = choose_difficulty()

        # Selecting a random word from selected category and difficulty
        mystery_object = choose_word(game_category, game_difficulty)
        mystery_word = mystery_object.Word

        # Informing user about thier game settings
        print("")
        print("You are guessing: " + mystery_object.Cat)
        print("The difficulty is: " + game_difficulty)
        # print("The mystery word is: " + mystery_word)

        # Number of missing characters in the word, according to difficulty
        missing_chars = num_of_missing_char(mystery_word, game_difficulty)
        print("Number of Missing Characters: " + str(missing_chars))

        # Guessing Time!
        graphics.Hanger()
        missing_characters = random.sample(mystery_word, missing_chars)

        def update_out_string():
            outString = ""
            for count in range(len(mystery_word)):
                if mystery_word[count] in missing_characters:
                    outString = outString + "_"
                else: 
                    outString = outString + mystery_word[count]
            print(outString)
            
        update_out_string()
        Won = False
        Lives = 7
        while (Won == False) and (Lives > 0):
            guess_char = input("Guess a character: ")
            if guess_char.lower() in missing_characters:
                missing_characters.remove(guess_char.lower())
            elif guess_char.upper() in missing_characters:
                missing_characters.remove(guess_char.upper())
            else:
                graphics.hangman_state(Lives)
                Lives -= 1

            update_out_string()
            if len(missing_characters) == 0:
                Won = True

        if Won:
            print("\n|========================|")
            print("| You've FOUND the Word! |")
            print("|========================|")
        else:
            print("\nYou Couldn't Guess the Word! ")
            print("The Word was: " + mystery_word)

        # Restarting/Ending the Game
        print("")
        play_again = input("Do you want to play agian? (y) for yes, and (n) for no: ")
        if play_again.lower() != "y":
            interested = False

main()