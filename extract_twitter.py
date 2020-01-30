import json
import os
from glob import glob

""" path = r'./twitter_dataset'
files = glob(path + "/*.json")
# open a write file
outputFile = open("twitter_text.txt", "a+")
for file in files:
    try:
        # open the json file
        with open(file, 'r') as jsonFile:
            data = jsonFile.read()
        obj = json.loads(data)
        size=obj.__len__()
        #print(size)
        for line in range(0, size):
            try:
                outputFile.write(str(obj[line]['retweeted_status']['extended_tweet']['full_text']).replace('\n', " ") )
                outputFile.write("\n")
            except KeyError:
                try:
                    outputFile.write(str(obj[line]['text']).replace('\n', " ") )
                    outputFile.write("\n")
                except KeyError:
                    continue
    except UnicodeDecodeError:
        continue
outputFile.close() """

def delete_duplicates(input_file, output_file):
    with open(input_file, "rb") as fp:
        lines = fp.readlines()
        new_lines = []
        for line in lines:
            if line not in new_lines:
                new_lines.append(line)
    with open(output_file, "wb") as fp:
        fp.write("\n".join(new_lines))

delete_duplicates("clean.txt", "cleaned.txt")
############################################################################
# tests #
#print("full text:" + str(obj[1]['text']))
#print("full text:" + str(obj[1]['retweeted_status']['extended_tweet']['full_text']))
""" try:
outputFile.write(str(obj[999]['retweeted_status']['extended_tweet']['full_text']).replace('\n', " ") )
except KeyError:
outputFile.write(str(obj[999]['text']).replace('\n', " ") ) """