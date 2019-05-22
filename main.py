import random
import string

def genData():
    data = ""

    for num in range(0,dataLength):
        data += random.choice(string.ascii_letters)
    
    return data
    
def encode(key):
    pass

if __name__ == "__main__":

    dataLength = random.randint(2,100)
    key = random.randint(1,25)

    data = genData()

    print(data)
