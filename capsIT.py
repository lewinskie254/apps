def convertToUpper(word):
    result = ""
    for char in word:
        if 'a' <= char <= 'z':
            x = ord(char)
            y = x - ord('a') + ord('A')  # Convert lowercase to uppercase
            result += chr(y)
        else:
            result += char  # Non-alphabetic character, leave unchanged

    return result 


def main():
    word = input("Word: ")
    print(convertToUpper(word))

if __name__ == "__main__":
    main()
