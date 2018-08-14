import nltk
nltk.download('conll2000')
from nltk.corpus import conll2000
x=(conll2000.tagged_sents())
for i in range(5):
    print(x[i])