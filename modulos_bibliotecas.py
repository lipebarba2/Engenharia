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
#plt.show()

import sqlite3

# Criação da tabela Produtos
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER
);
"""

cursor.execute(create_table)
conn.commit()
conn.close()

# Inserção de um novo produto
conn = sqlite3.connect('exemplo.db')  # Corrigi aqui
cursor = conn.cursor()

novo_produto = ('Camiseta', 19.99, 50)
inserir_produto = "INSERT INTO Produtos (nome, preco, estoque) VALUES (?,?,?)"
cursor.execute(inserir_produto, novo_produto)

conn.commit()
conn.close()

# Selecionando produtos
conn = sqlite3.connect('exemplo.db')  # Corrigi aqui também
cursor = conn.cursor()

selecionar_produtos = "SELECT * FROM Produtos"
cursor.execute(selecionar_produtos)

produtos = cursor.fetchall()
for produto in produtos:
    print(produto)

conn.close()

# Atualizando o preço de um produto
conn = sqlite3.connect('exemplo.db')  # Corrigi aqui também
cursor = conn.cursor()

novo_preco = '24.99'
produto_id = 1

atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
cursor.execute(atualizar_preco, (novo_preco, produto_id))

conn.commit()
conn.close()


import sqlite3

conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    telefone TEXT
    )
''')

dados_exemplo = [
    ('João', 'joao@email.com', '123-456-7890'),
    ('Maria', 'maria@email.com', '987-654-3210'),
    ('Carlos', 'carlos@email.com', '555-555-5555')
]

cursor.executemany('INSERT INTO Contatos (nome, email, telefone) VALUES (?,?,?)', dados_exemplo)

conn.commit()

cursor.execute('SELECT * FROM Contatos')
contatos = cursor.fetchall()
print('Contatos: ')
for contato in contatos:
    print(contato)

novo_telefone = '999-999-9999'
contato_id = 2
cursor.execute('UPDATE Contatos SET telefone = ? WHERE id = ?', (novo_telefone,contato_id))
conn.commit()

contato_id_para_excluir = 1

cursor.execute('DELETE FROM Contatos WHERE id = ?', (contato_id_para_excluir,))
conn.commit()

conn.close()