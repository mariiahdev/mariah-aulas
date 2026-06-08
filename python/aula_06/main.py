#EXERCÍCIO 1:
class Funcionario:
    def calcular_salario(self):
        return 0


class Vendedor(Funcionario):
    def __init__(self, salario, comissao):
        self.salario = salario
        self.comissao = comissao

    def calcular_salario(self):
        return self.salario + self.comissao


class Gerente(Funcionario):
    def __init__(self, salario, bonus):
        self.salario = salario
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario + self.bonus


vendedor = Vendedor(2000, 500)
gerente = Gerente(3000, 1000)

print("Salário vendedor:", vendedor.calcular_salario())
print("Salário gerente:", gerente.calcular_salario())

#EXERCÍCIO 2:
class Instrumento:
    def tocar(self):
        pass


class Violao(Instrumento):
    def tocar(self):
        print("Tocando violão")


class Bateria(Instrumento):
    def tocar(self):
        print("Tocando bateria")


class Piano(Instrumento):
    def tocar(self):
        print("Tocando piano")


instrumentos = [Violao(), Bateria(), Piano()]

for instrumento in instrumentos:
    instrumento.tocar()

#EXERCÍCIO 3:
class Forma:
    def area(self):
        return 0


class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


formas = [
    Triangulo(10, 5),
    Quadrado(4),
    Triangulo(8, 6)
]

for forma in formas:
    print("Área:", forma.area())

#EXERCÍCIO 4:
class Pagamento:
    def processar(self, valor):
        return valor


class Dinheiro(Pagamento):
    def processar(self, valor):
        return valor - (valor * 0.05)


class Cartao(Pagamento):
    def processar(self, valor):
        return valor + (valor * 0.02)


class Pix(Pagamento):
    def processar(self, valor):
        return valor


pagamentos = [
    Dinheiro(),
    Cartao(),
    Pix()
]

for pagamento in pagamentos:
    print("Valor final:", pagamento.processar(100))