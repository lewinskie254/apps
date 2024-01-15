total = 0 
cups = int(input("cups: "))
costPerCup = int(input("cost per cup: "))

for i in range(cups):
    cup = i + 1
    cost = costPerCup
    if cup % 8 == 0:
        cost = 0
    else: 
        cost= costPerCup
    
    total += cost
    print(f"Cup: {cup}, Cost: {cost}, Total Cost so far: {total}")
