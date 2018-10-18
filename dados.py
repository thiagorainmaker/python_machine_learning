import csv

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



