texto = "Explorando Python"

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de e no texto = {texto.count('e')}")
print(f"As 5 primeiras letras são: {texto[:5]}")

print('-----------------')

cores=['vermelho', 'azul', 'verde', 'amarelo', 'roxo']
for cor in cores:
    print(f"Posição = {cores.index(cor) +1}, cor = {cor}")

cores=['vermelho', 'azul', 'verde', 'amarelo', 'roxo']
print("Antes da listcomp = ", cores)
cores = [item.upper() for item in cores]
print("\nDepois da listcomp = ", cores)

print("\n")

precos_em_dolares = [100,50,75,120]
taxa_de_cambio = 5.25
precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))
print(precos_em_reais)

numeros = range(1,11)
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

print("\n")

vogais = ('a','e','i','o','u')
print(f'Tipo de objeto vogais = {type(vogais)}')
for p, x in enumerate(vogais):
    print(f"Posição  = {p +1}, valor = {x}")


convidados = ("ana", "maria", "joão", "lucia", "izac")
confirmados =  ["ana", "joão"]
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

print("Convidados que ainda não confirmaram: ")
for pessoa in nao_confirmados:
    print(pessoa)

print(f"\nEnviando lembretes para os convidados que ainda não confirmaram {nao_confirmados[0]}.")
print(f"\nEnviando lembretes para os convidados que ainda não confirmaram {nao_confirmados[1]}.")
print(f"\nEnviando lembretes para os convidados que ainda não confirmaram {nao_confirmados[2]}.")