lista = (1, 3, 5, 7, 5)
lista_animais = ('cachorro', 'gato', 'elefante', 'arara')
lista_animais[0] = 'macaco'
print(lista_animais)

tupla = (1, 10, 12, 14)
print(tupla[3])
print(len(tupla))
print(len(lista_animais))

#converter lista para tupla
tupla_animal = tuple(lista_animais)
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)

lista_numerica[0] = 100
print(lista_numerica)

tupla = tuple(tupla)
print(type(tupla))
print(tupla)



print(lista_animais[1])
print(sum(lista))
print(max(lista)) #ou lista animal
print(min(lista)) #ou lista_animal
print(type(lista_animais))

print(lista.sort())
print(lista_animais.sort())
print(lista)
print(lista_animais)

lista_animais.reverse()
print(lista_animais)


if 'lobo' in lista_animais:
    print('Existe um lobo na lista')
else:
    print('Não existe um lobo na lista')
lista_animais.append('lobo')
print(lista_animais)

lista_animais.pop(0)
print(lista_animais)

lista_animais.remove('gato')
print(lista_animais)




#mostra e multiplica os valores que existem
nova_lista = lista_animais * 3
print(nova_lista)



if 'gato' in lista_animais:
    print('Existe um gato na lista')
else:
    print('Não existe um gato na lista')

soma = 0
for x in lista:
    print(x)
    soma += x
print(soma)

