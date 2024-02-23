def collatz(n):
    n_array = []
    n_array.append(n)
    while n > 1:
        if n == 1: 
            break 
        elif n % 2 == 0:
            n = int(n/2)
        else:
            n = int((3*n) + 1)
        n_array.append(n)
    return n_array

def main():
    while True: 
        number = input("Enter a Number: ")
        if number.isdigit():
            number = int(number)
            break 
        else: 
            print("The number must be a digit.")
    
    print(collatz(number))


if __name__ == "__main__":
    main()
