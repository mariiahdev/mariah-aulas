class Funcionario: 
    def __init__(self, nome, matricula, salario_fixo):
        self.nome = nome
        self.matricula = matricula
        self.salario_fixo = salario_fixo

    @property
    def matricula(self):
       return self.__matricula
   
    @matricula.setter
    def matricula(self, new_matricula):
        if len(str(new_matricula)) != 6:
            raise ValueError("A matrícula tem que ter 6 números.")
        self.__matricula = new_matricula
        
    @property
    def salario_fixo(self):
        return self.__salario_fixo
    
    @salario_fixo.setter
    def salario_fixo(self, new_salario):
        if new_salario <= 0:
            raise ValueError("O salário não pode ser negativo.")
        self.__salario_fixo = new_salario

    def calcular_salario():
        return print('Tipo de usuário não específicado.')
    def exibir():
        return print('Tipo de usuário não específicado.')
    
class CLT(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return f'R$ {self.salario_fixo:.2f}'
    
    def exibir(self):
        return f'[CLT #{self.matricula}] {self.nome} - {self.calcular_salario()}'
    
class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_fixo, total_vendas):
        self.total_vendas = total_vendas

        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        salario_final = self.salario_fixo + (self.total_vendas * 0.1)
        return f'R$ {salario_final:.2f}'
    
    def exibir(self):
        return f'[VENDEDOR #{self.matricula}] {self.nome} - {self.calcular_salario()}'
    
class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        salario_final = self.salario_fixo + 1500.0
        return f'R$ {salario_final:.2f}'
    
    def exibir(self):
        return f'[GERENTE #{self.matricula}] {self.nome} - {self.calcular_salario()}'
    
funcionarios = [
    Gerente(nome='Mariah', matricula='456789', salario_fixo=3000),
    CLT(nome='João', matricula='096782', salario_fixo=2000),
    Vendedor(nome='Valentina', matricula='028642', salario_fixo=2500, total_vendas=1500)
]

for funcionario in funcionarios:
    print(funcionario.exibir())
