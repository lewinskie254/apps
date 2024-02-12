def drawBorder(height, width):

    rowString = "+"
    columnString = "|"
    newHeight = round(height/2)

    for j in range(width):
        rowString += "-"
        columnString += " "
    rowString += "+"
    columnString += "|"
    
    print(rowString)
    for i in range(newHeight):
        print(columnString)
    print(rowString)


def main():
    height = int(input("Height: "))
    width = int(input("Width: "))

    drawBorder(height, width)

if __name__ == "__main__":
    main()
    