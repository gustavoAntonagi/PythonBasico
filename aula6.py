

#uniao de conjuntos
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))

# print(type(conjunto))

#inteseccao o numero que se repete
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

#Diferença
conjunto_diferenca1 = conjunto.difference(conjunto2)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))

conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))

#Diferença Simetrica - Mostra os numeros que nao se repetem
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_dif_simetrica))


#Pertinencia
conjunto_a = (1, 2, 3)
conjunto_b = (1, 2, 3, 4, 5)

#Se não rodar o codigo abaixo, entao deve verificar o tipo da variavel e transforma-la em set
# conjunto_subset = conjunto_a.issubset(conjunto_b)
# print(conjunto_subset)

#Verificando o tipo
print(type(conjunto_a))

#Transformando as variaveis em set
conjunto_a = set(conjunto_a)
print(type(conjunto_a))
print(conjunto_a)

conjunto_b = set(conjunto_b)
print(type(conjunto_b))
print(conjunto_b)

#Subset
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}' .format(conjunto_subset))

conjunto_subset1 = conjunto_b.issubset(conjunto_a)
print('B é subconjunto de A: {}' .format(conjunto_subset1))
#FUNCIONOU :)


#Superset
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(conjunto_superset))

conjunto_superset1 = conjunto_a.issuperset((conjunto_b))
print('A é um superconjunto de B: {}'.format(conjunto_superset1))


#Conversao da lista para set, tira duplicidade
lista = ['Cachorro', 'Gato', 'Gato', 'Elefante']
conjunto_animais = set(lista)
print(conjunto_animais)


#Conversão da lista para list
conjunto_animais = list(conjunto_animais)
print(conjunto_animais)

# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)

