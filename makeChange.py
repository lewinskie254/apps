def changeAmount(amount):
    remainder = amount % 1

    convertible_amount = round(remainder * 100)
    
    quarter = 25 
    dime = 10 
    nickel = 5

    
    dollar = round(amount // 1)

    b = convertible_amount // quarter 
    rem_b = convertible_amount % quarter 

    c= rem_b // dime
    rem_c = rem_b % dime 

    d = rem_c // nickel
    rem_d = rem_c % nickel 
    balance = ""

    if dollar:
        balance += f"Dollars: {dollar}, " 
    if b:
        balance += f"Quarters: {b}, "
    if c: 
        balance += f"Dimes: {c}, "
    if d: 
        balance += f"Nickels: {d}, " 
    if rem_d:
        balance += f"Pennies: {rem_d}."

    

    return balance 


def main(): 
    while True: 
        amount = input("Amount: ")
        try:
            amount = float(amount)
            break
        except ValueError:
            print("Amount has to be a number.")
    print(changeAmount(amount))


if __name__ == "__main__":
    main()
