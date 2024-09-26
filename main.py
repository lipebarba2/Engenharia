import numpy as np

# Dados dos participantes

participantes = [

    {
        'nome': 'Alice',

        'localizacao': 'EUA',

        'afiliacao': 'Universidade A',

        'interesses': ['Física', 'Astronomia']

    },
    {

        'nome': 'Bob',

        'localizacao': 'Brasil',

        'afiliacao': 'Instituto B',

        'interesses': ['Biologia', 'Astronomia']

    },

    {

        'nome': 'Charlie',

        'localizacao': 'Índia',

        'afiliacao': 'Instituto C',

        'interesses': ['Química', 'Engenharia']

    }

    # Adicione mais participantes conforme necessário

]

print(participantes)

regioes = set(participante['localizacao'] for participante in participantes)

afiliacoes = {}

for participante in participantes:

    afiliacao = participante['afiliacao']

    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []

    afiliacoes[afiliacao].append(participante['nome'])

    areas_de_interesse = np.array(
        [interesse for participante in participantes for interesse in participante['interesses']])

    interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)

    area_mais_popular = interesses_unicos[np.argmax(contagem)]

    # Resultados

    print('Regiões dos participantes: ', regioes)

    print('Afiliações dos participantes: ')

    for afiliacao, nomes in afiliacoes.items():
        print(f'{afiliacao}: {", ".join(nomes)}')

        print('Área de interesse mais popular: ', area_mais_popular)

print('###############################################')

##CLASSES E MÉTODOS

class Pessoa:

    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    def aniversario(self):
        self.idade += 1


pessoa1 = Pessoa('Joao', 30, 'Masculino')

print(pessoa1.cumprimentar())

print(f'Idade: {pessoa1.idade} ')

pessoa1.aniversario()

print(f'Nova idade: {pessoa1.idade}')

print('##########################################\n')
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_barulho(self):
        pass

class Cachorro(Animal):
    def fazer_barulho(self):
        return 'Latir'

class Gato(Animal):
    def fazer_barulho(self):
        return 'Miar'


rex = Cachorro('Rex')
whiskers = Gato('Whiskers')

print(f'{rex.nome} faz: {rex.fazer_barulho()}')
print(f'{whiskers.nome} faz: {whiskers.fazer_barulho()}')

print('\n#############################')

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0


    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento

    def status(self):
        return f'Marca {self.marca}, Modelo: {self.modelo}, ano: {self.ano}, velocidade {self.velocidade} km/h'


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia

    def acelerar(self, incremento):
        self.velocidade += incremento + self.potencia

class Bicicletas(Veiculo):
    def __init__(self, marca, modelo, tipo, ano):
        super().__init__(marca,modelo,ano)
        self.tipo = tipo

    def status(self):
        return f'Marca {self.marca} Modelo {self.modelo}, Ano: {self.ano}, Tipo: {self.tipo }'




carro1 = Carro('Toyota', 'Corolla', 2022, 150)
bicicleta1 = Bicicletas('Trek', 'Moutain Bike', 2021, 'MTB')

carro1.acelerar(50)
bicicleta1.acelerar(20)

print(carro1.status())
print(bicicleta1.status())