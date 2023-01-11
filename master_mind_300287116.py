import random

name = input("What is your name? ")
print("Welcome to Mastermind " + name + "!")
print("The code maker is here. Available colours are")
print("Red, Yellow, Blue, Green, Orange, Pink, Purple, Cyan, Silver, Teal")
print("You have 15 guesses, total of 5 penalties are allowed but avoid penalties.")
print("The code maker selected 4 colours.")
print("You can start guessing " + name + ".")

penalties = 0
guesses = 15
colours = ["red", "yellow", "blue", "green", "orange", "pink", "purple", "cyan", "silver", "teal"]
coloursTwo = ["red", "yellow", "blue", "green", "orange", "pink", "purple", "cyan", "silver", "teal"]
code = []
maxNum = 9
black = 0
white = 0
count = 0

for i in range (0, 4):
    randNum = random.randint(0, maxNum)
    code.append(colours[randNum])
    colours.pop(randNum)
    maxNum -= 1

while guesses > 0 and penalties < 5 and black != 4:
    guess = input("Enter guess number " + str(16-guesses) + ": ")
    userGuesses = guess.lower().split()
    uniqueGuesses = set(userGuesses)
    black = 0
    white = 0
    count = 0
    notEnough = False
    duplicate = False
    invalid = False
    
    for i in userGuesses:
        if i not in coloursTwo:
            count += 1
    
    if len(uniqueGuesses) < len(userGuesses):
        duplicate = True
    if count > 0:
        invalid = True
    if len(userGuesses) != 4:
        notEnough = True
    
    if duplicate and not invalid and not notEnough:
        print("Sorry " + name + ", repeated colours are not allowed in this game. One penalty is considered.")
        penalties += 1
        print("Total penalties =", penalties)
    elif not duplicate and invalid and not notEnough:
        print("Sorry " + name + ", cannot recognize the colours you entered. One penalty is considered.")
        penalties += 1
        print("Total penalties =", penalties)
    elif not duplicate and not invalid and notEnough:
        print("Sorry " + name + ", you need to enter 4 colours for each guess. One penalty is considered.")
        penalties += 1
        print("Total penalties =", penalties)
    elif duplicate and invalid and not notEnough:
        print("Sorry " + name + ", repeated colours are not allowed in this game. Also, cannot recognize the colours you entered. One penalty is considered.")
        penalties += 1
        print("Total penalties =", penalties)
    elif duplicate and not invalid and notEnough:
        print("Sorry " + name + ", repeated colours are not allowed in this game. Also, you need to enter 4 colours for each guess. One penalty is considered.")
        penalties += 1
        print("Total penalties =", penalties)
    elif not duplicate and invalid and notEnough:
        print("Sorry " + name + ", cannot recognize the colours you entered. Also, you need to enter 4 colours for each guess. One penalty is considered.")
        penalties += 1
        print("Total penalties =", penalties)
    elif duplicate and invalid and notEnough:
        print("Sorry " + name + ", repeated colours are not allowed in this game. Also, cannot recognize the colours you entered. Also, you need to enter 4 colours for each guess. One penalty is considered.")
        penalties += 1
        print("Total penalties =", penalties)
    else:
        guesses -= 1
        for i in range (0, 4):
            if userGuesses[i] == code[i]:
                black += 1
                userGuesses[i] = "X"
        for i in userGuesses:
            if i == "X":
                userGuesses.remove(i)
        for i in range (0, len(userGuesses)):
            if userGuesses[i] in code:
                white += 1
        if black == 4:
            print("You got 4 blacks " + name + ".")
        else:
            if (black == 0 or black >= 2) and (white == 1):
                print("You got", black, "blacks and", white, "white for this guess")
            elif (white == 0 or white >= 2) and (black == 1):
                print("You got", black, "black and", white, "whites for this guess")
            elif (black == 0 or black >= 2) and (white == 0 or white >= 2):
                print("You got", black, "blacks and", white, "whites for this guess")
            elif black == 4 and white == 0:
                print("You got 4 blacks" + name + ".")
            else:
                print("You got", black, "black and", white, "white for this guess")
    
if black == 4:
    print("You won the game with", 15 - guesses, "guesses and", penalties, "penalties. Congratulations.")
elif penalties == 5:
    print(name + ", you lost the game by reaching the maximum number of allowed penalties.")
else:
    print("Sorry " + name + ", you ran out of guesses and you lost the game with " + str(penalties) + " penalties.")