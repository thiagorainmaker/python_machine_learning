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

print("Total de elementos no teste", total_elementos)
print("Taxa de acerto", taxa_de_acerto)







