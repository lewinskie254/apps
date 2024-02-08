import random 

small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
characters = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
choices = [small, capital, numbers, characters]



def generatePassword(length):
    password = ""
    for i in range(length):
        x = random.choice(random.choice(choices))
        password += x
    return password


def main():
    while True: 
        length = input("Length: ")
        if length.isdigit():
            length = int(length)
            if length < 12:
                length = 12
                break 
            else: 
                length = length 
                break 
        else:
            print("Length has to be a number: ")
    

    password = generatePassword(length)
    print(password)

if __name__ == "__main__":
    main()