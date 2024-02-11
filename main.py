import pandas as pd
import random

useCols = ["Word"]
num = random.randint(0, 13161)

words = pd.read_csv("word-meaning-examples.csv", index_col=0, usecols=useCols)

print(words.index[num])