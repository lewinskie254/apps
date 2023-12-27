def getChessSquareColor(x, y):
    x += 1
    y += 1 
    for i in range(9):
        numberY = i
        for j in range(9):
            numberX = j + 1
            sum = numberX + numberY
            color = ''
            if sum % 2 == 0:
                color= 'white'
            else:
                color = 'black'
            if x == numberX and y == numberY: 
                return color


def main():
    while True: 
        x = input("Value of X: ")
        if x.isdigit():
            x= int(x)
            if 0 <= x <= 7:
                break
            else: 
                print('Please select a digit between 0 and 7.')
        else: 
            print('Please select a digit between 0 and 7.')
    
    while True: 
        y = input("Value of Y: ")
        if y.isdigit():
            y= int(y)
            if 0 <= y <= 7:
                break
            else: 
                print('Please select a digit between 0 and 7.')
        else: 
            print('Please select a digit between 0 and 7.')

    print (f"The color for the Square at X: {x}, and Y: {y} is: {getChessSquareColor(x, y).capitalize()}")


if __name__ == "__main__":
    main()

    