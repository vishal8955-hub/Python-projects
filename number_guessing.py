import random

def number_guess():
    print("Guess a Under 1 to 10")
    li = [1,2,3,4,5,6,7,8,9,10]
    user = int(input("Enter your Guessed Number : "))
    if user <= 10:
        print("Valid Choice")
    else:
        print("Invaild Input")

    computer = random.choice(li)
    print(f"The Computer choice was : {computer}")

    if user == computer:
        print("Congratulation!! You Won the Match")
    else:
        print("Sorry!! You Loss The Match")
        return number_guess()
    
number_guess()