def CamelCase(word):
    result = word.split()

    new_phrase = ""

    for i in range(len(result)):
        new_word = ""
        if 'a' <= result[i][0] <= 'z':
            x=  ord(result[i][0]) 
            y = x - ord('a') + ord('A')
            new_char = chr(y)
            new_word += new_char
            for j in range(1, len(result[i])):
                new_word += result[i][j]
        else: 
            for j in range(len(result[i])):
                new_word += result[i][j]
        
        new_word += " "
        new_phrase += new_word

    return new_phrase

def main(): 

    word = input("Enter word or phrase: ")
    result = CamelCase(word)

    print(result)

if __name__ == "__main__":
    main()