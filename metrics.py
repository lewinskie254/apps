def area(a, b):
    return a * b

def perimeter(a, b):
    return 2*(a + b)

def volume(a, b, c):
    return a * b * c

def surfaceArea(a, b, c):
    return 2 * (a*b + b*c + c*a)

def prompt():
    while True: 
        formula = input("What would you like to calculate (perimeter, area, volume, surface area)").lower()

        if formula == "area":
            while True: 
                length = input("Length: ")
                width = input ("Width: ")
                if length.isdigit() and width.isdigit():
                    length = int(length)
                    width = int(width)
                    return area(length, width)
                else: 
                    print("Please provide a valid number.")
        elif formula == "volume":
            while True: 
                length = input("Length: ")
                width = input ("Width: ")
                height = input ("height: ")
                if length.isdigit() and width.isdigit() and height.isdigit():
                    length = int(length)
                    width = int(width)
                    height = int(height)
                    return volume(length, width, height)
                else: 
                    print("Please provide a valid number.")
        elif formula == "surface area":
            while True: 
                length = input("Length: ")
                width = input ("Width: ")
                height = input ("height: ")
                if length.isdigit() and width.isdigit() and height.isdigit():
                    length = int(length)
                    width = int(width)
                    height = int(height)
                    return surfaceArea(length, width, height)
                else: 
                    print("Please provide a valid number.")
        elif formula == "perimeter":
            while True: 
                length = input("Length: ")
                width = input ("Width: ")
                if length.isdigit() and width.isdigit():
                    length = int(length)
                    width = int(width)
                    return perimeter(length, width)
                else: 
                    print("Please provide a valid number.")
        else: 
            print(f"Please provide a valid choice between perimeter, area, surface area, and volume. You wrote {formula}, which is not valid.")

def main():
    result = prompt()
    print(f"The answer is {str(result)}")

if __name__ == "__main__":
    main()