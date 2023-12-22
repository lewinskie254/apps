def isOdd(n):
    if n % 2 == 1:
        return True
    
def isEven(n):
    if n % 2 == 0:
        return True
def prompt():
    while True: 
        n = input("Enter a number: ")
        if n.isdigit():
            return int(n)
        else:
            print("Please provide a number")


def main():

    number = prompt()
    
    if isOdd(number):
        print(f"{number} is an odd number.")
    elif isEven(number):
        print(f"{number} is an even number.")

if __name__ == "__main__":
    main()