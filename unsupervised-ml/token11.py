import textblob
from textblob import TextBlob

#sample text
text="Tokenization is the process of splitting a text into smaller units, typically"

#create a TextBlob object
blob=TextBlob(text)

#Tokenize into words
words=blob.words

#Tokenize into sentences
sentences=blob.sentences

print('Words:',words)