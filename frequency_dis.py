from nltk.tokenize import word_tokenize
from nltk.corpus import gutenberg

sample=gutenberg.raw("blake-poems.txt")
token=word_tokenize(sample)
wlist=[]
for i in range(50):
    wlist.append(token[i])
wordfreq=(wlist.count(w) for w in wlist)
print(token)