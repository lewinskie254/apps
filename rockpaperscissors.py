import random 


choices = ['rock', 'paper', 'scissors']


def RandomChoice():
    return random.choice(choices)

def main():
    while True: 
        userChoice = input("Rock, Paper, or Scissors? ").lower()
        if userChoice in choices:
            break # Set switch to False when the input is valid
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

    


        
    computerChoice = RandomChoice()

    if computerChoice == 'rock' and userChoice == 'paper':
        print(computerChoice)
        print("You Win. ")
    elif computerChoice == 'paper' and userChoice == 'scissors':
        print(computerChoice)
        print("You Win")
    elif computerChoice == 'scissors' and userChoice == 'rock':
        print(computerChoice)
        print("You Win")
    else: 
        print("Computer Choice: ", computerChoice)
        print("Computer Wins.")
    


if __name__ == "__main__":
    main()