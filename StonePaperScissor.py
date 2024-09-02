import random
def get_computer_choice():
    choice = ['Stone', 'Paper', 'Scissors']
    return random.choice(choice)

def get_user_choice():
    user_input = input("Enter Your Choice Stone Paper Scissors : ")
    while user_input not in ['Stone', 'Paper', 'Scissors']:
        print("Invaild Input. Please Try it Again")
    user_input = input("Enter Your Choice Stone Paper Scissors : ")
    return user_input

def determin_winner(user_choice , computer_choice):
    if user_choice == computer_choice:
        print("It's Tie")
    elif (user_choice == 'Stone' and computer_choice == 'Scissors') or \
        (user_choice == 'Scissors ' and computer_choice == 'Paper') or \
        (user_choice == 'Paper' and computer_choice == 'Stone'):
        print("You won")
    else:
        print("You Loss")
def game_choice():
    print("Welcome To The Stone Paper And Scissors Game\n Lets Get Started")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determin_winner(user_choice, computer_choice)
        print(result)
    #     play_again = input("Do you Want to Play Agian (Yes\No)")
    #     if input != "Yes":
    #         break
    # if __name__ == "__main__":
    #     play_again