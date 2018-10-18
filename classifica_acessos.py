from dados import carregar_acessos

x, y = carregar_acessos()

treino_dados = x[:90]
treino_marcacoes = y[:90]

teste_dados = x[-9:]
teste_marcacoes = y[-9:]

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()


model.fit(treino_dados, treino_marcacoes)

resultado = model.predict(teste_dados)
diferencas = resultado - teste_marcacoes

acertos = [d for d in diferencas if d == 0]
total_acertos = len(acertos)
total_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_acertos / total_elementos

print("Total de elementos", total_elementos)
print("Taxa de acerto", taxa_de_acerto)




