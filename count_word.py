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

countWords("cleaned_twitter_text.txt", "wordCount_twitter.txt")