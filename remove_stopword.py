from nltk.corpus import stopwords
en_stop=set(stopwords.words('english'))
all_words=['this','is','near','the','river']
for words in all_words:
    if words not in en_stop:
        print(words)
