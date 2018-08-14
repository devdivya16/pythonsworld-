import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
antonyms = []

for syn in wordnet.synsets("ahead"):
    for lm in syn.lemmas():
        if lm.antonyms():
            antonyms.append(lm.antonyms()[0].name())

print(set(antonyms))