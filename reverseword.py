def reverseString(word):

    new_phrase = word.split()
    phrase_updated = ""

    for h in range(len(new_phrase)):
        new_word = ""
        word_updated = ""
        
        new_word += new_phrase[h]
        print("New Word: ", new_word)

        
        for i in range(len(new_word), 0, -1):
            word_updated += new_word[i - 1]
            
        print("Word Updated", word_updated)
        phrase_updated += word_updated
        phrase_updated += " "

    return phrase_updated

def main():
    word = input("Word: ")
    print(reverseString(word))


if __name__ == "__main__":
    main()