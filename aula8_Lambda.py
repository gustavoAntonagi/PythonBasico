#LAMBDA uma função anonima (simplificacao de algo que sera utilizado mais de uma vez no codigo

contador_letra = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letra(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b
resto = lambda a, b: a % b

print(soma(5, 10))
print(subtracao(10, 5))
print(multiplicacao(10, 5))
print(divisao(5, 10))
print(resto(3, 5))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtração': lambda a, b: a - b,
    'multiplicaçao': lambda a, b: a * b,
    'divisão': lambda a, b: a / b,
    'resto': lambda a, b: a % b,
}

print(type(calculadora))
soma = calculadora['soma']
subtracao = calculadora['subtração']
multiplicacao = calculadora['multiplicaçao']
divisao = calculadora['divisão']
resto = calculadora['resto']

print('A soma em lambda é: {}'.format(soma(10, 5)))
print('A subtração em lambda é: {}'.format(subtracao(10, 6)))
print('A multiplicação em lambda é: {}'.format(multiplicacao(15, 5)))
print('A divisão em lambda é: {}'.format(divisao(10, 4)))
print('O resto em lambda é: {}'.format(resto(112, 54)))
