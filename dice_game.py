import random
def dice_game():

    user = int(input("Enter the Guess Number : "))
    if user <= 6:
        print("Valid Choice") 
    else:
        print("Invaild Input")

    number = [1,2,3,4,5,6]
    com = random.choice(number)
    print(f"The Computer choice was : {com}")

    if user == com:
        print("You Won the Match")
        return ("Congratulation You Won The Match!!")
    else:
        print("You Loss!")
    return dice_game()

dice_game()

