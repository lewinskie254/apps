def getCostOfCoffee(cups, costPerCup):
    total = 0 

    for i in range(cups):
        cup = i + 1
        cost = costPerCup
        if cup % 8 == 0:
            cost = 0
        else: 
            cost = costPerCup
        
        total += cost
    
    return total 
    


def main(): 
    while True: 
        cups = input("How many cups do you want? ")
        if cups.isdigit():
            cups = int(cups)
            break 
        else: 
            print("Please input a valid number.")

    while True: 
        costPerCup = input("How much does each cup cost? ")
        if costPerCup.replace('.', '', 1).isdigit():
            costPerCup = float(costPerCup)
            break 
        else: 
            print("Please input a valid number.")
    
    print(f"Your total cost is: {getCostOfCoffee(cups, costPerCup)}")


if __name__ == "__main__":
    main()