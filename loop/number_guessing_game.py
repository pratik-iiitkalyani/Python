winning_num = 56
guess = 1
number = int(input("guess any number between 0 to 100: "))
game_over = False
while not game_over:
    if number == winning_num:
        print(f"you win, and you guessed this number {guess} times")
        game_over = True
    else:
        if number < winning_num:
            print("too low")
        else:
            print("too high")
    if game_over == False:
        guess+=1
        number = int(input("guess again : "))