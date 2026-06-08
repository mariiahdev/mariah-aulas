#EXERCÍCIO 1: 
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Preço inválido")


produto = Produto("Caderno", 15)

print("Nome:", produto.get_nome())
print("Preço:", produto.get_preco())

produto.set_preco(20)

print("Novo preço:", produto.get_preco())

#EXERCÍCIO 2:
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome
        else:
            print("Nome inválido")

    def set_idade(self, idade):
        if idade >= 0 and idade <= 120:
            self.__idade = idade
        else:
            print("Idade inválida")

    def apresentar(self):
        print("Nome:", self.__nome)
        print("Idade:", self.__idade)


pessoa = Pessoa("Mariah", 20)

pessoa.apresentar()

pessoa.set_idade(21)

pessoa.apresentar()

#EXERCÍCIO 3: 
class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def get_saldo(self):
        return self.__saldo

    def extrato(self):
        print("Titular:", self.__titular)
        print("Saldo:", self.__saldo)


conta = ContaBancaria("Mariah")

conta.depositar(100)
conta.depositar(50)

conta.sacar(30)

print("Saldo atual:", conta.get_saldo())

conta.extrato()

#EXERCÍCIO 4: 
class Sensor:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    def set_temperatura(self, temperatura):
        if temperatura >= -50 and temperatura <= 150:
            self.__temperatura = temperatura
        else:
            print("Temperatura inválida")

    def status(self):
        if self.__temperatura <= 80:
            return "Normal"
        elif self.__temperatura <= 120:
            return "Alerta"
        else:
            return "Crítico"


sensor = Sensor(25)

temperaturas = [25, 90, 121, -10]

for temperatura in temperaturas:
    sensor.set_temperatura(temperatura)
    print("Temperatura:", temperatura)
    print("Status:", sensor.status())