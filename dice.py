import random 



def rollDice(times): 
    total = 0

    for i in range(times):
        prompt = input("Would you like to roll the dice? Y or N. ").lower()

        if prompt == 'y':
            roll = random.randint(1, 6)
            total += roll
            print(f"{i + 1} Round. You rolled {roll}, your score is now {total}")
        elif prompt == 'n':
            break 
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
    
    print(f"Game Over. Your final score is {total}")


def main():
    while True: 
        times = input("How many times would you like to roll? ")
        if times.isdigit():
            times = int(times)
            break
        else:
            print("Please input a valid number")
    
    str(rollDice(times))



if __name__ == "__main__":
    main()