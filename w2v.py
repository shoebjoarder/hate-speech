from gensim.models import KeyedVectors
import pandas as pd
from glob import glob
import re
import os

model = KeyedVectors.load_word2vec_format('embed_tweets_de_300D_fasttext', binary=False)

# print(model.most_similar('merkel'))

path = r'./data'
process = './process_data/'
files = glob(path + "/*.txt")
for file in files:
    df = pd.read_csv(file, header=None, index_col=None)
    totalRows = df.__len__()
    li = []
    document = process + str(os.path.splitext(os.path.basename(file))[0].split('.')).strip("'[]'") + '.txt'
    f = open(document, 'w')
    for i in range(0, totalRows):
        data = df.loc[i,:]
        data = str.strip(data.to_string(index=False))
        if '#' in data:
            data = str.strip(re.sub('#', ' ', data))
            print('#' + data)
            list = ""
            for j in range(0, 5):
                try:
                    if i != totalRows:
                        list = list + model.most_similar(data)[j][0] + ", "
                    else:
                        list = list + model.most_similar(data)[j][0]
                except KeyError:
                    continue
            list = '#' + data + ', ' + list
            f.write(list)
            f.write('\n')
        elif '@' in data:
            data = str.strip(re.sub('@', ' ', data))
            print('@' + data)
            list = ""
            for j in range(0, 5):
                try:
                    print('  ' + model.most_similar(data)[j][0])
                    if i != totalRows:
                        list = list + model.most_similar(data)[j][0] + ", "
                    else:
                        list = list + model.most_similar(data)[j][0]
                except KeyError:
                    continue
            list = '@' + data + ', ' + list
            f.write(list)
            f.write('\n')
        else:
            print(data)
            list = ""
            for j in range(0, 5):
                try:
                    if i != totalRows:
                        list = list + model.most_similar(data)[j][0] + ", "
                    else:
                        list = list + model.most_similar(data)[j][0]
                except KeyError:
                    continue
            list = data + ', ' + list
            f.write(list)
            f.write('\n')
    f.close()


'''    
filename = './data/Sonstige.txt'
filename1 = str(os.path.splitext(os.path.basename(filename))[0].split('.')).strip('[]')
print(filename1)


df = pd.read_csv('./data/Ausländer_Migranten.txt', header=None, index_col=None)
data = df.loc[1,:]
data = str.strip(data.to_string(index=False))
if '#' in data:
    data = str.strip(re.sub('#', ' ', data))
data
 '''       