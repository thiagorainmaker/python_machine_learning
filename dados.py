import csv
import pandas as pd

def carregar_acessos():
    x = []
    y = []

    arquivo = open('acesso.csv', 'rb') 
    leitor = csv.reader(arquivo)
    leitor.next()
    
    for acessou_home,acessou_como_funciona,acessou_contato,comprou in leitor: 
        x.append([int(acessou_home),int(acessou_como_funciona),int(acessou_contato)])
        y.append(int(comprou))

    return x, y



def carregar_buscas(porcentagem_teste):
    df = pd.read_csv('buscas.csv')
    #variaveis dummies
    x = df[['home', 'busca', 'logado']]
    y = df['comprou']
    
    x_dummies = pd.get_dummies(x).values
    y_dummies = y.values

    tamanho_treino  = porcentagem_teste*len(y_dummies)
    tamanho_teste   = len(y) - tamanho_treino

    treina_dados     = x_dummies[:int(tamanho_teste)]
    treina_marcacoes = y_dummies[:int(tamanho_teste)]


    teste_dados     = x_dummies[-int(tamanho_teste):]
    teste_marcacoes = y_dummies[-int(tamanho_teste):]

    return treina_dados, treina_marcacoes, teste_dados, teste_marcacoes





