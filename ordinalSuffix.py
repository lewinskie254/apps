def ordinalSuffix(n):
    n = str(n)
    if n == '12': 
        return f"{n}th"
    elif n.endswith(('0', '4', '5', '6', '7', '8', '9')): 
        return f"{n}th"
    elif n.endswith('1'):
        return f"{n}st"
    elif n.endswith('2'):
        return f"{n}nd"
    elif n.endswith('3'):
        return f"{n}rd"

def main():
    while True: 
        number = input("Number: ")
        if number.isdigit():
            number = int(number)
            break 
        else: 
            print("Please use a valid number without decimals.")
    
    result = ordinalSuffix(number)
    print(result)


if __name__ == "__main__":
    main()