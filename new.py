def getChessSquareColor(x, y):
    x += 1
    y += 1 
    sum = x + y
    color = 'white' if sum % 2 == 0 else 'black'
    return color

def getValidInput(prompt):
    while True: 
        value = input(prompt)
        if value.isdigit():
            value = int(value)
            if 0 <= value <= 7:
                return value
        print('Please select a digit between 0 and 7.')

def main():
    x = getValidInput("Value of X: ")
    y = getValidInput("Value of Y: ")

    color = getChessSquareColor(x, y)
    print(f"The color for the Square at X: {x}, and Y: {y} is: {color.capitalize()}")

if __name__ == "__main__":
    main()
