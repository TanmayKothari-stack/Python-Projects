import random
winner = random.randint(1,100)
guess = 1
number = int(input("Guess a Number: "))
game_over = False
while not game_over:
    if number == winner:
        print(f"YOU WON THE GAME IN {guess} ATTEMPTS")
        game_over = True
    else:
        if number > winner:
            print("TOO HIGH NUMBER")
            guess = guess + 1
            number = int(input("Guess Again: "))
        else:
            if number < winner:
                print("TOO LOW NUMBER")
                guess = guess + 1
                number = int(input("Guess Again: "))
                
