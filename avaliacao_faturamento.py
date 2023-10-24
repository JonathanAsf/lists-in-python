
#Apresentação dos dados
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]
vendas_totais = vendas_1sem + vendas_2sem #Concatenação das listas

melhor_vendas = max(vendas_totais) #Maior faturamento mensal
print(melhor_vendas)
pior_vendas = min(vendas_totais) #Pior faturamento mensal

melhor_mes = vendas_totais.index(melhor_vendas)
pior_mes = vendas_totais.index(pior_vendas)

print(f"O Melhor mês em vendas foi: {meses[melhor_mes]}\n o Pior mês de vendas foi: {meses[pior_mes]}")
print(f"O faturamento anual foi de R${sum(vendas_totais):,}")
#Otimizar mais tarde a busca pelos tres maiores valores
vendas_totais.sort(reverse=True)

top3 = []
top3.append(vendas_totais[0])
top3.append(vendas_totais[1])
top3.append(vendas_totais[2])

print(f"Os três melhores faturamentos foram: {top3}")
