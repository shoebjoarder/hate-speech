from glob import glob
import pandas as pd

# preprocess dataset
searchFile = pd.read_csv("./corpus/deu-com_web_2018_10K-sentences.txt", header=None, 
                     sep='\t').iloc[:, 1]
path= r'./data'
keywordFiles = glob(path + "/*.txt") # keyword file
outputFile = open("output.txt", "a+") # output file
for keywordFile in keywordFiles:
    # keyword file dataframe
    keywords = pd.read_csv(keywordFile, header=None, index_col=None) 
    totalRows = keywords.__len__() 
    for keyword in range(0, totalRows):
        key = keywords.loc[keyword,:]
        key = str.strip(key.to_string(index=False))
        key = " " + key + " "
        for line in searchFile:
            if key in line:
                outputFile.write(line + '\n')
outputFile.close()