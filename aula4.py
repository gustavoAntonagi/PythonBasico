#Laços de repetição
#WHILE

a = int(input("Digite a nota da B1: "))
while a > 10:
    a = int(input('Digitou errado a nota da B1, por favor digite novamente: '))

b = int(input("Digite a nota da B2: "))
while b > 10:
    b = int(input('Você digitou a nota B2 errada, por favor digite novamente: '))

c = int(input("Digite a nota da B3: "))
while c > 10:
    c = int(input('Você digitou a nota da B3 errada, por favor digite novamente: '))

d = int(input("Digite a nota da B4: "))
while d > 10:
    d = int(input('Você digitou a nota da B4 errada, por favor digite novamente: '))

media = (a + b + c + d) / 4
print('media: {}'.format(media))


nota = int(input('Digite sua nota: '))
while nota > 10:
    nota = int(input('"Erro" Digite novamente sua nota: '))
print(nota)

a = 0
while a < 10:
    print(a)
    a += 1



# #FOR

a = int(input("Digite um número: "))

div = 0
for x in range(1, a+1):
    resto = a % x
    print(x, resto)
    if resto == 0:
       div += 1

if div == 2:
    print('Número {} é primo'.format(a))
else:
    print('Número {} não é primo'.format(a))


for dentro de for, laços de repetição
a = int(input('Digite um valor: '))
for num in range(a+1):
    div = 0
    for x in range(1, num+1) :
        resto = num % x
        #print(x, resto)
        if resto == 0:
            div += 1
    if div == 2:
        print(num)
