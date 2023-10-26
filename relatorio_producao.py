# Construa um código que exiba a quantidade produzida de cada produto nesse e-mail"

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]

print("Por meio deste relatório identifica-se os produtos e a quantidade produzida: ")
for i in range (len(produtos)):
    print(produtos[i], producao[i])
