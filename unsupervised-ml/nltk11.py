import nltk
""" nltk.download("maxent_ne_chunker")
nltk.download("words")
nltk.download("stopwords") """
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import ne_chunk
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#sample text
text="Barack Obama was born in Hawaii. He served as the 44th President of the United States from 2009 to 2017."

#tokenization
tokens=word_tokenize(text)

#named-entity recognition (NER)
ner_tags=nltk.pos_tag(tokens)
ner_entities=ne_chunk(ner_tags)

#stemming
stemmer=PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in tokens]

#Lemmatization
lemmatizer=WordNetLemmatizer()
lemmatized_words =[lemmatizer.lemmatize(word) for word in tokens]

#remove stopwords
stop_words=set(stopwords.words('english'))
filtered_words= [word for word in tokens if word.lower() not in stop_words]

#create word clouds
def generate_word_cloud(words,title):
    wordcloud=WordCloud(width=800,height=800, background_color='white',stopwords=stop_words,
    min_font_size=20).generate(' '.join(words))
    plt.figure(figsize=(8,8),facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.title(title)
    plt.show()

generate_word_cloud(tokens,"Word Cloud - Original Text")
generate_word_cloud(filtered_words,"Word Cloud- Without Stopwords")
generate_word_cloud(stemmed_words,"Word Cloud - Stemmed Words")
generate_word_cloud(lemmatized_words,"Word Cloud - Lemmatized Words")