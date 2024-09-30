print("Hello world!")

x = 10 #Inteiro
nome = 'aluno' #String
nota = 8.75 #Float
fez_inscricao = True #boolean
print(type(nome))
print(type(nota))
print(type(x))
print(type(fez_inscricao))

nome = input("Digite um nome: ")

print(nome)

print(f"Olá {nome}, seja bem-vindo")
print("-------------------------")

nota1 = int(input("Digite sua primeira nota"))
nota2 = int(input("Digite sua segunda nota"))
nota3 = int(input("Digite sua terceira nota"))
nota4 = int(input("Digite sua quarta nota"))

media = (nota1+nota2+nota3+nota4) / 4
if media >= 6:
    situacao = "aprovado"
else:
    situacao= "Reprovado"

print(f"A meida das notas é: {media} e a situação {situacao}")





