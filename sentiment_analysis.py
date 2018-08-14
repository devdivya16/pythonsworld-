import nltk
import nltk.sentiment.sentiment_analyzer
def Onewor():
    positive_words=['good','progress','luck']
    text="hard work brings progress and good luck .".split()
    analysis=nltk.sentiment.util.extract_unigram_feats(text,positive_words)
    print(analysis)
def twoword():
    word=[('regular,fit'),('fit','fine')]
    text = 'Regular excercise makes you fit fine'.split()
    analysis= nltk.sentiment.util.extract_bigram_feats(text,word)
    print(analysis)
def negword():
    text ='Lack of good health can not bring success to students'.split() 
    analysis=nltk.sentiment.util.mark_negation(text)
    print(analysis)
Onewor()
twoword()
negword()