def three(n):
    if n % 3 == 0:
        return True
    
def five(n):
    if n % 5 == 0:
        return True
    
def both(n):
    if n % 5 == 0 and n % 3 == 0:
        return True

def main():
    while True: 
        number = input("Number: ")
        if number.isdigit():
            number = int(number)
            break 
        else:
            print("Please input a valid number with no decimals.")
    
    if both(number):
        print("FizzBuzz")
    elif five(number):
        print("Buzz")
    elif three(number):
        print("Fizz")
    else:
        print(f"{number}")

if __name__ == "__main__":
    main()