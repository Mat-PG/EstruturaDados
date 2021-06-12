import glob, os, codecs, sys
import nltk
from funcoes import *

'''from nltk.stem import PorterStemmer

sentences = nltk.sent_tokenize(texto)
wordstokenized = nltk.word_tokenize(texto)'''

for arq in glob.glob("docs/*.txt"):

    docTemporario = ''

    f = codecs.open(arq, "r", "UTF-8")
    linhas = f.readlines()

    for linha in linhas:
        docTemporario += linha.strip()
    f.close()

    docTemporario = tokenizacao(docTemporario)
    docTemporario = remove_pontuacao(docTemporario)
    docTemporario = remove_stopwords(docTemporario)
    
    indexacao(docTemporario, arq)


    print(docTemporario)