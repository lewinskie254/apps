def makePyramid(height):
    x = " "
    count = height

    for i in range(height):
        count -= 1
        print(count * x, end="") 
        for j in range(i):
            print("#", end="")
        for k in range(1, i):
            print("#", end="")
        print()

def main():
    while True: 
        height = input("Height: ")

        if height.isdigit():
            height = int(height)
            break
        else:
            print("Height must be a digit.")
    
    makePyramid(height)

if __name__ == "__main__":
    main()

