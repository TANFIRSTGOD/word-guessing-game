import pandas as pd
import random

useCols = ["Word"]
num = random.randint(0, 13161)
ingame = True

words = pd.read_csv("word-meaning-examples.csv", index_col=0, usecols=useCols)

wordArr = []

for i in words.index[num]:
    wordArr.append([i, "_"])

print(words.index[num])

usrAns = ""

while ingame:
    string = ""
    for i in wordArr:
        string += i[1] + " "
        usrAns += i[1]

    print(string)
    usrInpt = input(">>")

    for i in wordArr:
        if i[0] == usrInpt:
            i[1] = i[0]

    completeString = ""

    for i in wordArr:
        completeString += i[0]

    if string == words.index[num]:
        print("You won")
        break