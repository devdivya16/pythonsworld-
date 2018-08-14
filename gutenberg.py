import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
field=gutenberg.raw("blake-poems.txt")
token=sent_tokenize(field)
for id in range(5):
    print(token[id])