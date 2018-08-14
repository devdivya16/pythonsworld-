import nltk
word_data="The best performation can bring the high sky sucsses."
tokenize=nltk.word_tokenize(word_data)
print(list(nltk.bigrams(tokenize)))