from dados import carregar_buscas
from sklearn.naive_bayes import MultinomialNB

dados_treino, marcacao_treino, teste_dados, teste_marcacoes = carregar_buscas(0.9)



model = MultinomialNB()
model.fit(dados_treino, marcacao_treino)
resultado = model.predict(teste_dados)
diferencas = resultado - teste_marcacoes

acertos = [d for d in diferencas if d == 0]
total_acertos = len(acertos)
total_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_acertos / total_elementos

print("Total de elementos no teste %d " % total_elementos)
print("percentual de acerto no algoritmo %d" % taxa_de_acerto)

#testar a eficiencia de um algoritmo que chuta tudo 0 ou tudo 1

acerto_de_um    = sum(marcacao_treino)+sum(teste_marcacoes)
acerto_de_zero  = sum(marcacao_treino)+sum(teste_marcacoes) - acerto_de_um

taxa_de_acerto_base = 100*max(acerto_de_um, acerto_de_zero)/(len(marcacao_treino)+len(teste_marcacoes))

print("percentual base de acerto base: %f " % taxa_de_acerto_base)





