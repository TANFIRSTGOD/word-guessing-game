import pandas as pd

useCols = ["Word"]

words = pd.read_csv("word-meaning-examples.csv", index_col=0, usecols=useCols)

for i in words.index:
    print(i)