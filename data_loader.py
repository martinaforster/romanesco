import pandas as pd

dataPath = 'movie_review.csv'
devDataPath = 'dev.txt'
trainDataPath = 'train.txt'

df = pd.read_csv(dataPath, usecols=['text'])

# shuffle data
df = df.sample(frac=1)

#convert to list
sentences = df.values.tolist()

print("There are ", len(sentences), " sentences in the data set.")

#write dev set
devData = sentences[:2000]
with open(devDataPath, 'w') as f:
    for item in devData:
        f.write("%s\n" % item[0])

#write training set
trainData = sentences[2000:]
with open(trainDataPath, 'w') as f:
    for item in trainData:
        f.write("%s\n" % item[0])



