# winning_num = 56
winning_number = random.randint(1,100)
guess = 1
number = int(input("guess any number between 0 to 100: "))
while True:
    if number == winning_num:
        print(f"you win, and you guessed this number {guess} times")
        break
    else:
        if number < winning_num:
            print("too low")
        else:
            print("too high")
    
        guess+=1
        number = int(input("guess again : "))