def rot13(word): 
    new_word =""

    for char in word: 
        if "a" <= char <= "z": 
            if char > "m": 
                x = chr(ord(char) - 13)
            elif char < "m":
                x = chr(ord(char) + 13)
        elif "A" <= char <= "Z":
            if char > "M": 
                x = chr(ord(char) - 13)
            elif char < "M":
                x = chr(ord(char) + 13)
        else: 
            x = char
        
        new_word += x

    return new_word

def main():

    word = input("Enter a word: ")
    result = rot13(word)
    print(result)


if __name__ == "__main__":
    main()