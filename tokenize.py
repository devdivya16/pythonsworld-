import nltk
from translate import Translator
german_tokenize=nltk.data.load('tokenizers/punkt/german.pickle')
german_tokens=german_tokenize.tokenize('Wie geht es Ihnen?  Gut, danke.')
print(german_tokens)
trans=Translator(to_lang="German")
transl=trans.translate("good morning")
print (transl)
from nltk.corpus import stopwords
stopwords.words('english')
print(stopwords.words()[620:680])
print(stopwords.fileids())