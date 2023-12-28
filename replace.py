def findAndReplace(phrase, word, replacement): 
    return phrase.replace(word, replacement)
    
def main():
    phrase = input("Phrase: ").lower()
    word = input("Word you want to replace: ").lower()
    replacement = input("Word to replace with: ").lower()

    result = findAndReplace(phrase, word, replacement)

    print(result.capitalize())


if __name__ == "__main__":
    main()