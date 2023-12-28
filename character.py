def findAndReplace(word, character, replacement): 
    new_word = ""
    for letter in word: 
        if letter == character: 
            new_word += replacement
        else: 
            new_word += letter
    return new_word


    
def main():
    word = input("Word: ").lower()
    character = input("Character you want to replace: ").lower()
    replacement = input("Letter to replace with: ").lower()

    result = findAndReplace(word, character, replacement).capitalize()

    print(result)


if __name__ == "__main__":
    main()