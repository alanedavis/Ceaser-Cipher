import random
import re
    
def encrypt(text,key):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if text[i] == " ":
            result += " "
            continue
        elif char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
        
    return result

if __name__ == "__main__":
    text = input("Enter any sentence you'd like: ")
    re.sub('[^A-Za-z0-9]+', '', text)
    key = random.randint(1,25)
    print("Text         : " + text)
    print("Key          : " + str(key))
    print("Cipher       : " + encrypt(text,key))
