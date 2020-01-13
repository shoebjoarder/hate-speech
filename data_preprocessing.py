# import libraries
import pandas as pd
import seaborn as sns

from textblob import TextBlob
from nltk.tokenize import TweetTokenizer
from nltk.tokenize.casual import remove_handles
from nltk.stem.snowball import GermanStemmer

# import dataset
columns = ['article', 'goldLabel', 'type']
dataset = pd.read_csv('./dataset/germeval2018.training.txt', sep='\t',
                      header=None, names=columns)

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
        
        # Remove emojis
        german_char = " 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZöäüÖÄÜ"
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
dataset['text_clean']= dataset['article'].apply(text_cleaner)



