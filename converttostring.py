def convertToString(integer):
    return str(integer)

def main():
    integer = input("Enter a number: ")
    print(f"'{convertToString(integer)}'")

if __name__ == "__main__":
    main()