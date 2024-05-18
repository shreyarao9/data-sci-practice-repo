import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk import pos_tag,ne_chunk
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text='''Natural Language Processing (NLP) is a field of artificial intelligence concerned with the interaction between computers and humans in natural language. It enables computers to understand, interpret, and generate human language. NLP techniques are used for a variety of tasks such as sentiment analysis, language translation, named-entity recognition and more.'''

tokens=word_tokenize(text)
sentences=sent_tokenize(text)

#remove stepwords
stop_words = set(stopwords.words('english'))
filtered_tokens=[word for word in tokens if word.lower() not in stop_words]

#part-of-speech tagging
pos_tags=pos_tag(tokens)

#named-entity recognition (NER)
ner_entities=ne_chunk(pos_tags)

#stemming
stemmer=PorterStemmer()
stemmed_words=[stemmer.stem(word) for word in filtered_tokens]

#lemmatization
lemmatizer=WordNetLemmatizer()
lemmatized_words=[lemmatizer.lemmatize(word) for word in filtered_tokens]

#create word cloud
wordcloud = WordCloud(width=800,height=400,background_color='white').generate(' '.join(filtered_tokens))

#display word cloud
plt.figure(figsize=(10,5))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud')
plt.show()

#print results
print("original text:")
print(text)
print('\nTokenization:')
print(tokens)
print('\nSentences:')
print(sentences)
print('\nStopwords removed:')
print(filtered_tokens)
print('\nPart-of-speech tags:')
print(pos_tags)
print('\nNamed entities:')
print(ner_entities)
print('\nStemmed words:')
print(stemmed_words)
print('\nLemmatised words:')
print(lemmatized_words)