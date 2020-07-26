from aula7_Televisao import Televisao
from aula7_Calculadora1 import Calculadora
from aula8_contador_letras import contador_letras, teste

if __name__ == '__main__':

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('O total de letras da lista por palavras é: {}'.format(total_letras))

    Teste = teste()
    print(teste())