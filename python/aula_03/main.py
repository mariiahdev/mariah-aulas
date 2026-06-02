#EXERCÍCIO 1 E 2
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        desconto = self.preco - (self.preco * percentual / 100)
        return desconto

produto1 = Produto("Raquete de Tênis", 349.99)
produto2 = Produto("Suporte Atlético", 79.99)

print(produto1.nome)
print(produto1.preco)
print(f"{produto1.desconto(10):.2f}")
print(produto2.nome)
print(produto2.preco)
print(f"{produto2.desconto(10):.2f}")

#EXERCÍCIO 3: 
class Carro:
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0
        
    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        if self.velocidade >= 10:
            self.velocidade -= 10

carro1 = Carro("Corolla", "Toyota", "Corolla")
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.frear()

print(carro1.velocidade)

#EXERCÍCIO 4: 
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor 

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def extrato(self):
        print("Titular: ", self.titular)
        print("Saldo: ", self.saldo)

conta = ContaBancaria("Mariah", 400)
conta.depositar(50)
conta.sacar(100)

conta.extrato()