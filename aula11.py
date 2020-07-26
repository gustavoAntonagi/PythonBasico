#EXEÇÕES
#Como lançar exceções genericas
#Utilizar exceções especificas
#Else e Finally
#Criação de exceções customizadas

#Forçando erros para tratamento de exceções
lista = (1, 10)
arquivo = open('teste.txt', 'r')

try:
    divisao = 10 / 0
    numero = lista[1]
    x = 10
    texto = arquivo.read()

#ZeroDivisionError pode ser trocado por ArithmeticError por que ZeroDivision está abaixo da exceção ArithmeticError
#ou seja, ArithmeticError é a exceção pai e ZeroDivisionError é a exceção filho, so que a exceção ArithmeticError contem
#exceções de aritimetica, então a mensagem no print deve ser mudada caso use ArithmeticError
except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por 0')

except IndexError:
    print('Erro ao acessar um indice invalido da lista')

#BaseException é a exceção pai, ou seja, as outras exceções vem depois da BaseException
except BaseException as ex:
    print('Erro desconhecido, Erro: {}'.format(ex))

else:
    print('Executa quando não ocorre exceção')

finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
