def printASCIITable(): 
    for i in range(32, 127):
        print(i, chr(i))


def convertToAscii(name):
    unpacked = [*name]

    for i in range(len(unpacked)):
        print(unpacked[i], ord(str(unpacked[i])))

def main(): 
    while True: 
        question = input("Would you like to (A) print the entire ASCII table for commonly used characters or (B) type a word and convert it to ASCII? [Choose A or B.] ").lower()

        if question == 'a':
            printASCIITable()
            break
        elif question == 'b': 
            name = input("Enter a name you would like converted to ASCII: ")
            convertToAscii(name)
            break
        else: 
            print("Invalid Choice. You can only choose between A and B.")
            print()


if __name__ == "__main__":
    main()