from sklearn.naive_bayes import MultinomialNB
from dados import load_access


X, Y = load_access()

treino_X = X[:90]
treino_marcacoes = Y[:90]

teste_dados = X[-9:]
teste_marcacoes = Y[-9:]

modelo = MultinomialNB()
modelo.fit(treino_X, treino_marcacoes)


result = modelo.predict(teste_dados)
print()
diferencas = result - teste_marcacoes

acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos


print(f'Taxa de acerto: {taxa_de_acerto}')
