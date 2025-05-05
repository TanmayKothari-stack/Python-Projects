import random
guess = 1
winner = random.randint(1,5)
num = int(input("Guess A Number: "))

game_over = False
while not game_over:
    if(num == winner):
        if(num == 1):
            print(f"You Won The Game in {guess} attempt")
            game_over = True
        elif(num > 1):
            print(f"You Won The Game in {guess} attempts")
            game_over = True
    else:
        if(num > winner):
            print("You Guess A Too High number Try Again")
            num = int(input("Guess Again: "))
            guess = guess + 1
        else:
            if(num < winner):
                print("You Guess A Too Low number Try Again")
                num = int(input("Guess Again: "))
                guess = guess + 1


      
