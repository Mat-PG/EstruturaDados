# encoding: utf-8
import os, pickle, nltk
from funcoes import monster
from nltk.stem import RSLPStemmer
nltk.download('rslp')

# Agrupando as funções previamente

# Stemming para retornar como string
def stemming_singular(palavra):
    nucleo = RSLPStemmer()
    palavra1 = substitui_especiais(palavra)
    return nucleo.stem(palavra1)

def substitui_especiais(token):
    return token.replace('á', 'a').replace('à', 'a').replace('â', 'a').replace('ã', 'a')\
        .replace('é', 'e').replace('è', 'e').replace('ê', 'e').replace('í', 'i')\
        .replace('ì', 'i').replace('ó', 'o').replace('ò', 'o').replace('ô', 'o')\
        .replace('õ', 'o').replace('ú', 'u').replace('ù', 'u').replace('ç', 'c')

# Stemming para retornar como lista
def stemming(frase):
    nucleo = RSLPStemmer()
    fraseNucleo = []
    for palavra in frase:
        fraseNucleo.append(nucleo.stem(palavra.lower()))
    return fraseNucleo

def remove_pontuacao(token):
  novo_token = ''
  pontuacoes = '!-()[]{};:\'\"\/,<>.?@#%^&*_~'
  
  for char in token:
    if char not in pontuacoes:
      novo_token = novo_token + char
  
  return novo_token

def remover_stop_words(palavras):
    for i, c in enumerate(palavras):  # Percorre todas as palavras da list
        if i == len(palavras):
            break
        elif palavras[i] in stopwords:
            palavras.remove(palavras[i])
        if i == len(palavras):
            break
        elif palavras[i] in stopwords:
            palavras.remove(palavras[i])
        if i == len(palavras):
            break
        elif palavras[i] in stopwords:
            palavras.remove(palavras[i])
    return palavras

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

caminho = "./docs/"

while True:
    os.system('cls')
    # Menu e ciclo de execução da aplicação
    print('------- INDEXAÇÃO -------')
    print('''0. Encerrar a aplicação
1. Criar Novo Documento
2. Indexar documentos '.txt' presentes na pasta docs/
3. Realizar consultas
    1. Usando operador OR
    2. Usando operador AND
    3. [opcional] Usando expressões booleanas
4. Mostrar Índice Invertido (para debug / print)''')
    # O que o usuário deseja fazer
    decision = input(str("Digite a opção: "))
    if "0" in decision:
        break
    # Verificando se o comando é válido ou não
    elif decision not in '01234' and decision != "dahaf":
        print("Comando inváido")

    else:
        # Instanciando as variáveis necessárias
        indexados = {}
        frase_final = []

        if decision == "1":
            nome = input(str('Nome do arquivo [incluindo o .txt]: '))
            arquivo = open(caminho + nome, 'w')  # cria um aquivo no caminho
            conteudo = input(str(u'Digite o conteúdo do arquivo: ')).lower()
            conteudo = remove_pontuacao(conteudo)
            arquivo.write(conteudo)  # Escreve o conteúdo

        elif decision == "2":
            # Instanciando o objeto pickle responsável por criar/escrever o arquivo
            # "wb" = write binary
            pickle_out = open("dict_index.txt", "wb")

            for _, _, arquivos in os.walk(caminho):
                # Le os arquivos presentes na pasta

                for arquivo in arquivos:  # Percorre os arquivos .txt

                    print(arquivo)
                    ler = open(caminho + arquivo, 'r', encoding='UTF-8')  # Abre os arquivos .txt

                    for texto in ler:
                        texto = substitui_especiais(texto)
                        texto = remove_pontuacao(texto)
                        texto = texto.lower()
                        # Transforma o conteudo dos arquivos de list para string
                        palavras = texto.split()  # Remove os espaços e retorna uma list com cada palavra indentada
                        remover_stop_words(palavras)

                        palavras = stemming(palavras)
                        for palavra in palavras:
                            if palavra in texto:
                                if palavra not in indexados:
                                    listaDeValores = []
                                    listaDeValores.append(arquivo)
                                    indexados[palavra] = listaDeValores # Indexa a palavra
                        
                                else:
                                    if arquivo not in indexados[palavra]: # Indexa o arquivo como value para a key palavra
                                        indexados[palavra].append(arquivo)

            # Salva o dicionário e fecha o objeto pickle
            pickle.dump(indexados, pickle_out)
            pickle_out.close()

        elif decision == "3":
            pickle_in = open("dict_index.txt", "rb")
            final_dict = pickle.load(pickle_in)

            while True:
                option = str(input('''
0. Sair
1. Usando operador OR
2. Usando operador AND
3. [opcional] Usando expressões booleanas
Sua opção: '''))
                if option not in '0123':
                    print("Comando inválido")

                if option == "0":
                    break

                elif option == "3":

                    # Lista doc palavra 1
                    # Lista doc palavra 2
                    # Lista doc palavra 3
                    # Primeira expressão (palavra2 OR palavra3)
                    # Segunda expressão res(1 expressão) AND palavra1
                    print('''Favor inserir as operações com seus operadores lógicos
Exemplo de input:
Primeira operação => palavra1 OR palavra2
Segunda operação => AND palavra3\n''')
                    primeira_operacao = str(input("Primeira operação: ").strip())
                    segunda_operacao = str(input("Segunda operação: ").strip())

                    print('\nDesculpe, ainda estamos trabalhando nesta funcionalidade...')

                else:
                    palavra1 = str(input("palavra 1: ").strip()) # Preserva a palavra pesquisada
                    palavra2 = str(input("palavra 2: ").strip())
                    palavra1Stemming = stemming_singular(palavra1) # Faz Stemming na palavra pesquisada
                    palavra2Stemming = stemming_singular(palavra2)

                if option == "1":
                    if palavra1Stemming == palavra2Stemming:

                        if palavra1Stemming in final_dict:
                            print(palavra1Stemming + ": " + final_dict.get(palavra1Stemming).to_s)
                        else:
                            print("Palavra(s) não encontradas")

                    if palavra1Stemming in final_dict.keys():
                        print(f"A palavra {palavra1} esta no(s) arquivo(s): {final_dict.get(palavra1Stemming)}")
                    else:
                        print(f"A palavra {palavra1} não está indexada")

                    if palavra2Stemming in final_dict.keys():
                        print(f"A palavra {palavra2} esta no(s) arquivo(s): {final_dict.get(palavra2Stemming)}")
                    else:
                        print(f"A palavra {palavra2} não está indexada")

                if option == "2":
                    if palavra1Stemming not in final_dict or palavra2Stemming not in final_dict: # Se ambas as palavras não estão indexadas
                        print("Alguma palavra não está indexada")

                    elif palavra1Stemming == palavra2Stemming:

                        if palavra1Stemming in final_dict:
                            print(final_dict.get(palavra1Stemming))
                        else:
                            print("Palavras não relacionadas22")
                    else:
                        lista = []
                        
                        valorPalavra1 = final_dict.get(palavra1Stemming) # Pegar os Values da key palavra
                        valorPalavra2 = final_dict.get(palavra2Stemming)
                        
                        for item1 in valorPalavra1:
                            lista.append(item1)
                        for item2 in valorPalavra2:
                            lista.append(item2)
                        local = []
                        for item in lista:
                            if item in valorPalavra1 and item in valorPalavra2:
                                if item not in local:
                                    local.append(item)
                        print(f'Ambas palavras se encontram em {local}',end=' ')
                         # Verifica a Intersecção dos Values

        elif decision == "4":
            # Instancia o objeto pickle, abre o arquivo em modo "rb" = read byte
            pickle_in = open("dict_index.txt", "rb")
            final_dict = pickle.load(pickle_in)
            for k, v in final_dict.items():
                print(f"Palavra: {k}, Docs: {v}")
            input('\nPressionar tecla "enter" assim que concluir debug!')

        elif decision == 'dahaf':
            monster()
