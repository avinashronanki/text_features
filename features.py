import textfeatures as tf
import pandas as pd

#enconding is applicable for this dataset.
df = pd.read_csv("/Users/avinashronanki/COVID-19_Tweets.csv",encoding="latin")
# print("here")
# print(df)
print(df.head())
tf.word_count(df,"Tweets","word_cnt")
word_count = df[["Tweets","word_cnt"]].head()
print(word_count)