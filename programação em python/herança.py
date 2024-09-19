class Empregado:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
    
    def calcular_salario(self):
        return self.salario_base

class Gerente(Empregado):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus
    
    def calcular_salario(self):
        return self.salario_base + self.bonus

class Vendedor(Empregado):
    def __init__(self, nome, salario_base, vendas, comissao):
        super().__init__(nome, salario_base)
        self.vendas = vendas
        self.comissao = comissao
    
    def calcular_salario(self):
        return self.salario_base + (self.vendas * self.comissao)

gerente = Gerente("angela", 2000, 2000)
vendedor = Vendedor("cesar", 1412, 41000, 0.026)

print(f"Salário Gerente {gerente.nome}: R${gerente.calcular_salario():.2f}")
print(f"Salário Vendedor {vendedor.nome}: R${vendedor.calcular_salario():.2f}")
