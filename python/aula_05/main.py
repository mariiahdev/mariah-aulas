#EXERCÍCIO 1:
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(self.nome, "está comendo")


class Cachorro(Animal):
    def latir(self):
        print("Au au!")


cachorro = Cachorro("Rex")

cachorro.comer()
cachorro.latir()

#EXERCÍCIO 2:
class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def informacoes(self):
        print("Marca:", self.marca)
        print("Ano:", self.ano)


class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas


class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas


carro = Carro("Fiat", 2020, 4)
moto = Moto("Honda", 2022, 160)

carro.informacoes()
moto.informacoes()

#EXERCÍCIO 3:
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir(self):
        print("Nome:", self.nome)
        print("Salário:", self.salario)


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def salario_total(self):
        return self.salario + self.bonus


gerente = Gerente("Mariah", 3000, 500)

gerente.exibir()
print("Salário total:", gerente.salario_total())

#EXERCÍCIO 4:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Matrícula:", self.matricula)


class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Salário:", self.salario)


pessoas = [
    Aluno("Ana", 18, "123"),
    Professor("Carlos", 40, 5000)
]

for pessoa in pessoas:
    pessoa.apresentar()