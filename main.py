import streamlits as st
import nltk


nltk.download('punkt_tab')

frase = "python é legal"

token = nltk . word_tokenize (frase)

print(token)

 tagged = nltk.pos_tag(tokens)

print(token)

nltk.download('averaged_perceptron_tagger_eng')

tagged = nltk

import nltk
from nltk.corpus import treebank


nltk.download('treebank')
nltk.download('punkt_tab')


frase = "Python é muito legal"


tokens = nltk.word_tokenize(frase, language='portuguese')


print(tokens)


nltk.download('averaged_perceptron_tagger_eng')


tagged = nltk.pos_tag(tokens)


print(tagged)



t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
