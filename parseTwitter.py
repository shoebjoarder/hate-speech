import json
import os
from glob import glob

def parseTwitter(fileName, path):
    files = glob(path + "/*.json")
    # open a write file
    outputFile = open(fileName, "a+")
    for file in files:
        try:
            # Open the json file
            with open(file, 'r') as jsonFile:
                data = jsonFile.read()
            obj = json.loads(data)
            size=obj.__len__()
            #print(size)
            for line in range(0, size):
                sentence = ""
                original = ""
                retweet = ""
                quotedRetweet = ""
                quoted = ""
                # Checks retweets and quotes from original
                try:
                    # Check if its a retweeted, get the full text of original tweet
                    retweet = str(obj[line]['retweeted_status']['extended_tweet']['full_text']).replace('\n', " ")
                    sentence = retweet
                    id = str(obj[line]['retweeted_status']['id']).replace('\n', " ")
                    outputFile.write(id + ", " + retweet)
                    outputFile.write("\n")
                    try:
                        # Check if there is a qouted tweet with full text
                        quotedRetweet = str(obj[line]['retweeted_status']["quoted_status"]['extended_tweet']['full_text']).replace('\n', " ")
                        sentence = quotedRetweet
                        id = str(obj[line]['retweeted_status']["quoted_status"]['id']).replace('\n', " ")
                        outputFile.write(id + ", " + quotedRetweet)
                        outputFile.write("\n")
                    except KeyError:
                        try:
                            # Check if there is a qouted tweet with text
                            quotedRetweet = str(obj[line]['retweeted_status']["quoted_status"]['text']).replace('\n', " ")
                            sentence = quotedRetweet
                            id = str(obj[line]['retweeted_status']["quoted_status"]['id']).replace('\n', " ")
                            outputFile.write(id + ", " + quotedRetweet)
                            outputFile.write("\n")
                        except KeyError:
                            pass
                except KeyError:
                    try:
                        # Check if its a retweeted, get the full text of original tweet
                        retweet = str(obj[line]['retweeted_status']['text']).replace('\n', " ")
                        sentence = retweet
                        id = str(obj[line]['retweeted_status']['id']).replace('\n', " ")
                        outputFile.write(id + ", " + retweet)
                        outputFile.write("\n")
                        try:
                            # Check if there is a qouted tweet with full text
                            quotedRetweet = str(obj[line]['retweeted_status']["quoted_status"]['extended_tweet']['full_text']).replace('\n', " ")
                            id = str(obj[line]['retweeted_status']["quoted_status"]['id']).replace('\n', " ")
                            sentence = quotedRetweet
                            outputFile.write(id + ", " + quotedRetweet)
                            outputFile.write("\n")
                        except KeyError:
                            try:
                                # Check if there is a qouted tweet with text
                                quotedRetweet = str(obj[line]['retweeted_status']["quoted_status"]['text']).replace('\n', " ")
                                id = str(obj[line]['retweeted_status']["quoted_status"]['id']).replace('\n', " ")
                                sentence = quotedRetweet
                                outputFile.write(id + ", " + quotedRetweet)
                                outputFile.write("\n")
                            except KeyError:
                                pass
                    except KeyError:
                        pass            
                try:
                # Check if there is a qouted tweet with full text
                    quoted = str(obj[line]["quoted_status"]["extended_tweet"]['full_text']).replace('\n', " ")
                    if quoted != quotedRetweet:
                        sentence = quoted
                        id = str(obj[line]["quoted_status"]["id"]).replace('\n', " ")
                        outputFile.write(id + ", " + quoted)
                        outputFile.write("\n")
                except KeyError:
                    try:
                        # Check if there is a qouted tweet with text
                        quoted = str(obj[line]["quoted_status"]['text']).replace('\n', " ")
                        if quoted != quotedRetweet:
                            sentence = quoted
                            id = str(obj[line]["quoted_status"]["id"]).replace('\n', " ")
                            outputFile.write(id + ", " + quoted)
                            outputFile.write("\n")
                    except KeyError:
                        pass
                if not retweet:
                    # Checks original tweet
                    try:
                        # Check if its the original tweet with full text
                        original = str(obj[line]['extended_tweet']['full_text']).replace('\n', " ")
                        sentence = original
                        id = str(obj[line]["id"]).replace('\n', " ")
                        outputFile.write(id + ", " + original)
                        outputFile.write("\n")
                    except KeyError:
                        try:
                            original = str(obj[line]['text']).replace('\n', " ")
                            sentence = original
                            id = str(obj[line]["id"]).replace('\n', " ")
                            outputFile.write(id + ", " + original)
                            outputFile.write("\n")
                        except:
                            continue
        except UnicodeDecodeError:
            continue
    outputFile.close()

def countWords(input, output):
    # Open the file in read mode 
    inputFile = open(input, "r")
    # Create an empty dictionary 
    d = dict() 
    # Loop through each line of the file 
    for line in inputFile: 
        # Remove the leading spaces and newline character 
        line = line.strip() 
        # Convert the characters in line to  
        # lowercase to avoid case mismatch 
        line = line.lower() 
        # Split the line into words 
        words = line.split(" ") 
        # Iterate over each word in line 
        for word in words: 
            # Check if the word is already in dictionary 
            if word in d: 
                # Increment count of word by 1 
                d[word] = d[word] + 1
            else: 
                # Add the word to dictionary with count 1 
                d[word] = 1
    # store the contents of dictionary
    outputFile = open(output, "a+")
    for key in list(d.keys()): 
        outputFile.write(str(key) + ": " + str(d[key]))
        outputFile.write("\n")
    outputFile.close()

def removeDuplicates(fileName, path):
    files = glob(path + "/*.txt")
    # open a write file
    for file in files:
        with open(file, 'r') as f:
            txt = f.readlines()
        d = dict()
        # Loop through each line of the file 
        for line in txt:
            linePart = ''
            count = 0
            line = line.strip()
            words = line.split(" ")
            words.pop(0)
            # remove the first RT
            for i in range(0, 2):
                if len(words) > 1 and "RT" in words[0]:
                    words.pop(0)
            # remove the second RT if exists
            """ if len(words) > 1 and "RT" in words[0]:
                words.pop(0) """
            countWords = len(words)
            if countWords == 2:
                linePart = str(words[1])
            elif countWords > 2:
                for i in range(1, countWords):
                    if countWords == 3:
                        linePart = linePart + " " + ''.join(words[i])
                    elif countWords == 4:
                        linePart = linePart + " " + ''.join(words[i])
                    elif countWords == 5:
                        linePart = linePart + " " + ''.join(words[i])
                    elif countWords >= 6 and count < 5:
                        linePart = linePart + " " + ''.join(words[i])
                        count = count + 1
                    else:
                        break
            linePart = linePart.strip()
            line = " ".join(words)
            # Check if the linePart is already in dictionary 
            if linePart not in d: 
                # Add the linePart as key and line as values
                d[linePart] = line
            else: 
                # Pass if duplicate
                pass
    # store the contents of dictionary
    outputFile = open(fileName, "a+")
    for key in list(d.keys()): 
        outputFile.write(str(d[key]))
        outputFile.write("\n")
    outputFile.close()



if __name__ == '__main__':
    """ 
    dataset= "twitter_dataset.txt"
    path = r'/home/allan/Downloads/twitter_dataset_german_election'
    #path = r'./twitter_dataset'

    # start parsing twitter text
    parseTwitter(dataset, path)
    print("\nDone twitter data parsing!\n")
    """
    #print("Run this in termimal to remove exact duplicates \"sort twitter_dataset.txt | uniq > cleaned_twitter.txt\" \n")

    path = r'./final'
    dataset= "twitter_removeDup_v3_final_2.txt"
    removeDuplicates(dataset, path)
    print("\nDone! removed duplicate!\n")

"""
    # count the number of occurence of words
    cleanText = "cleaned_twitter.txt"
    countText = "wordCount_twitter.txt"
    countWords(cleanText, countWords)
"""
