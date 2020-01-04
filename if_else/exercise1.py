winning_number = 25
guessed_number = int(input("plz! guess the number : "))
if guessed_number == winning_number:
    print("YOU WIN !!!!")
else:
    if guessed_number<25:
        print("Too low!!")
    else:
        print("Too high!!")