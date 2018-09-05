print("hello making")
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag



dataset="""hello Mr watson how are doing today?
            make sure """

print(sent_tokenize(dataset,language='english'))
for i in sent_tokenize(dataset):
    print(i)

for i in word_tokenize(dataset):
    print(i)


print(" check 1 for stop words")
filtered_sentence=[]
words=word_tokenize(dataset)
stop_words=set(stopwords.words('english'))
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)

print("check2 porter stemmer")
ps=PorterStemmer()

data=["love","lover","loving","loved","lovingly"]

for w in data:
    print(ps.stem(w))

print(pos_tag(words))
