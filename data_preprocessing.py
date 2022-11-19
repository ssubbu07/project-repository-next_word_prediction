import nltk
nltk.download('all-nltk')
from nltk.tokenize import word_tokenize

print("Creating token of words:")


#Sample text for testing the methods
text="I am Dileep Reddy from Team10 and I wrote this code"
tokenize_word=word_tokenize(text)
print(tokenize_word)

from nltk.stem import PorterStemmer
words=["light","lighting","lights"]
ps=PorterStemmer()
for w in words:
    rootword=ps.stem(w)
    print(rootword)



from nltk.stem import WordNetLemmatizer
lem=WordNetLemmatizer()
print(lem.lemmatize("playing"))


from nltk import word_tokenize,pos_tag
text="I am Dileep Reddy from Team10 and I wrote this code"
print(pos_tag(word_tokenize(text)))    
