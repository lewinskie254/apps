import re

def reverseAlphabeticWords(word):
    def reverse_word(match):
        return match.group(0)[::-1]

    reversed_result = re.sub(r'\b\w+\b', reverse_word, word)
    return reversed_result

def main():
    word = input("Enter a sentence: ")
    reversed_result = reverseAlphabeticWords(word)
    print("Reversed Result:", reversed_result)

if __name__ == "__main__":
    main()
