def drawBox(size):
    stick = "|"
    plus = "+"
    stroke = "/"
    x = plus
    y = stick 
    z = ""
    c = ""
    a = " "


    bottomSpace = ""
    for i in range(size):
        a += " "
        bottomSpace += " "


    count = 0

    z += stroke
    for i in range((size * 2)):
        x += "-"
        y += " "
        z += " "

    x += plus
    y += stick
    z += stroke

    print(f"{a}{x}")
    for i in range(size):
        count += 1
        a = a[:-1]
        b = f"{a}{z}{c}{stick}"
        print(b)
        c += " "


    print(f"{x}{bottomSpace}+")
    for i in range(size):
        bottomSpace = bottomSpace[:-1]  
        print(f"{y}{bottomSpace}{stroke}")
    print(x)

def main():
    while True: 
        size = input("Size (between 1 and 10): ")
        if size.isdigit():
            size = int(size)
            if 0 < size < 11:
                break 
            else:
                print("Maximum size is 10. ")
        else:
            print("Size has to be a number.")
    
    drawBox(size)


if __name__ == "__main__":
    main()