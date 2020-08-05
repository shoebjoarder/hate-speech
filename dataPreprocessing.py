# import libraries
import pandas as pd
#import seaborn as sns
import re

from textblob import TextBlob
from nltk.tokenize import TweetTokenizer
from nltk.tokenize.casual import remove_handles
from nltk.stem.snowball import GermanStemmer

# import dataset
# =============================================================================
# columns = ['article', 'goldLabel', 'type']
# dataset = pd.read_csv('./dataset/germeval2018.training.txt', sep='\t',
#                       header=None, names=columns)
# =============================================================================
columns = ['sentenceID','sentence']
dataset1 = pd.read_csv('./dataset/deu-com_web_2018_1M-sentences.txt', sep='\t',
                      header=None, names=columns)
dataset2 = pd.read_csv('./dataset/deu-eu_web_2017_1M-sentences.txt', sep='\t',
                      header=None, names=columns)

frames = [dataset1, dataset2]

result = pd.concat(frames)
# =============================================================================
# # Plot count
# sns.countplot(x= 'goldLabel',data = dataset)
# =============================================================================

# Punctuation, emojis and username handle removal
# Tokenization / German Stemmer
def text_cleaner(text):
        use_GermanStemmer = False
        tokens = False
        
        # Remove username handles 
        # -? do we need the user names
        text = remove_handles(text) 
        
        # Remove punctuation marks
        text_blob = TextBlob(text)
        text = ' '.join(text_blob.words)
        
        # replace the umlauts
# =============================================================================
#         text = re.sub('ä', 'ae', text)
#         text = re.sub('ö', 'oe', text)
#         text = re.sub('ü', 'ue', text)
#         text = re.sub('Ä', 'Ae', text)
#         text = re.sub('Ö', 'Oe', text)
#         text = re.sub('Ü', 'Ue', text)
#         text = re.sub('ß', 'ss', text)
# =============================================================================

        # remove the numbers
        text = re.sub(r'[0-9]+', '', text)

        # Remove emojis
        german_char = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZäöüÄÖÜ"
        text = ''.join(c for c in text if c in german_char)
    
        tokenizer = TweetTokenizer(preserve_case=True, reduce_len=True)
        if tokens:
            return tokenizer.tokenize(text)
        elif use_GermanStemmer: 
            stemmer = GermanStemmer()
            return [stemmer.stem(token) for token in tokenizer.tokenize(text)]
        else:
            return text

# Data cleaning        
# =============================================================================
# dataset['text_clean'] = dataset['article'].apply(text_cleaner)
# =============================================================================
result['text_clean'] = result['sentence'].apply(text_cleaner)

# Save in csv
result['text_clean'].to_csv("cleaned_text.csv", index=False)