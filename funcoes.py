import glob, os, codecs, sys
import nltk

stopwords = ['de', 'a', 'o', 'que', 'e', 'é', 'do', 'da', 'em', 'um', 'para', 'com', 'não', 'uma', 'os', 'no', 'se',
             'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'ao', 'ele', 'das', 'à', 'seu', 'sua', 'ou', 'quando',
             'muito', 'nos', 'já', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'depois', 'sem',
             'mesmo', 'aos', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'você', 'essa', 'num', 'nem', 'suas', 'meu',
             'às', 'minha', 'numa', 'pelos', 'elas', 'qual', 'nós', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este',
             'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso',
             'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles',
             'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos',
             'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 'estejam',
             'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'há', 'havemos',
             'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse',
             'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos',
             'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era', 'éramos', 'eram',
             'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos',
             'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam',
             'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram',
             'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver',
             'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam']

def ler_remover_espacoIF():
    for arq in glob.glob("docs/*.txt"):
        print("[{}]".format(arq))
        docTemporario = ''

        # Abrir arquivo
        f = codecs.open(arq, "r", "UTF-8")
        linhas = f.readlines()

        for linha in linhas:
            # remove espaços em branco no inicio e fim de cada linha lida
            docTemporario += linha.strip()
        f.close()

        print(docTemporario)
        print()

def tokenizacao(doc_inicial):
  return doc_inicial.split(' ')

def substitui_especiais(token):
  token.replace('á', 'a')
  token.replace('à', 'a')
  token.replace('â', 'a')
  token.replace('ã', 'a')
  token.replace('é', 'e')
  token.replace('è', 'e')
  token.replace('ê', 'e')
  token.replace('í', 'i')
  token.replace('ì', 'i')
  token.replace('ó', 'o')
  token.replace('ò', 'o')
  token.replace('ô', 'o')
  token.replace('õ', 'o')
  token.replace('ú', 'u')
  token.replace('ù', 'u')
  token.replace('ç', 'c')
  

def indexacao(doc, arq):
    # doc: list | arq: str (nome do arquivo)
    dic = dict()
    for palavra in doc:
        if palavra in dic:
            lista_docs = dic[palavra]
            lista_docs.append(arq)
        else:
            dic[palavra] = [arq]

def remove_stopwords(lista):
    nova_lista = []

    for token in lista:
        if token.lower() not in stopwords:
            nova_lista.append(token)

    return nova_lista

def remove_pontuacao(token):
  novo_token = ''
  pontuacoes = '!()[]{};:\'\"\,<>.?@#%^&*_~'
  
  for char in token:
    if char not in pontuacoes:
      novo_token = novo_token + char
  
  return novo_token
