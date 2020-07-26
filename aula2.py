a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
#print(type(a))
soma = a + b
subtracao = a - b
multiplcacao = a * b
divisao = a / b
resto = a % b


resultado = ('Soma: {soma}. \nSubtracao: {subtracao}. '
      '\nMultiplicacao: {multiplicacao}. '
      '\ndivisao: {divisao}. '
      '\nresto: {resto}.'
      .format(soma=soma, subtracao=subtracao, multiplicacao=multiplcacao, divisao=divisao, resto=resto))
print(resultado)

# print(type(soma))
# soma = str(soma)
# print(type(soma))
# print('soma: ' + soma)
# print('subtracao: ' + str(subtracao))
# print('multiplcacao: ' + str(multiplcacao))
# print(int(divisao))
# print(resto)
#x = '1'
#soma2 = int(x) + 1
#print(soma2)