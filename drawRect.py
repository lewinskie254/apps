def drawRect(width, height):
    for i in range(height):
        for j in range(width):
            print("#", end="")
        print()

def main():
    height = int(input("Height: "))
    width = int(input("Width: "))

    drawRect(width, height)

if __name__ == "__main__":
    main()