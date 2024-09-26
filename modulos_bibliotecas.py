import matplotlib.pyplot as plt

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
vendas = [120, 90, 150, 80, 200]

plt.bar(meses, vendas, color='royalblue')

plt.xlabel("Mês")
plt.ylabel('Vendas (em Unidades)')

plt.title('Vendas mensais')

#plt.show()


print("------------------------")

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"{self.titulo} por {self.autor}, publicado em {self.ano_publicacao}"


biblioteca = []

anos = []

def adicionar_livro(titulo, autor, ano_publicacao):
    novo_livro = Livro(titulo, autor, ano_publicacao)
    biblioteca.append(novo_livro)
    anos.append(ano_publicacao)
    print(f"O livro '{titulo}' foi adionado à biblioteca.")

def listar_livros():
    print("Livros na Biblioteca")
    for livro in biblioteca:
        print(livro)

adicionar_livro("Dom Quixote", "Miguel de Cervantes", 1605)
adicionar_livro("Orgulho e Preconceito", "Jane Austen", 1813)
adicionar_livro("1984", "George Orwell", 1949)

listar_livros()

anos = list(set(anos))
anos.sort()

contagem_por_ano = [anos.count(ano) for ano in anos]

plt.plot(anos, contagem_por_ano, marker='o', linestyle='-')
plt.xlabel('Ano de publicação')
plt.ylabel('Numero de Livros')
plt.title("Distribuição de Livros na biblioteca por ano de publicação")

for i, valor in enumerate(contagem_por_ano):
    plt.text(anos[i], valor, str(valor), ha= 'center', va = 'bottom')

plt.grid(True)
plt.show()