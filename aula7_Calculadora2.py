class Calculadora:
    def __init__(self):
        pass
    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

Calculadora = Calculadora()
print(Calculadora.soma(10, 2))
print(Calculadora.subtracao(5, 3))
print(Calculadora.multiplicacao(10, 5))
print(Calculadora.divisao(100, 2))
