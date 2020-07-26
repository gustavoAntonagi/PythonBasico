a = int(input("Digite a nota da B1: "))
if a > 10:
    a = int(input('Digitou errado a nota da B1, por favor digite novamente: '))

b = int(input("Digite a nota da B2: "))
if b > 10:
    b = int(input('Você digitou a nota B2 errada, por favor digite novamente: '))

c = int(input("Digite a nota da B3: "))
if c > 10:
    c = int(input('Você digitou a nota da B3 errada, por favor digite novamente: '))

d = int(input("Digite a nota da B4: "))
if d > 10:
    d = int(input('Você digitou a nota da B4 errada, por favor digite novamente: '))

media = (a + b + c + d) / 4
print('media: {}'.format(media))


if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print("media: {}" .format(media))
else:
    print('notas incorretas, favor verificar novamente')




a = int(input('Digite o numero: '))
b = int(input('Digite o segundo valor: '))
resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or not resto_b > 0:
    print('O numero é par')
else:
    print('Nenhum numero par foi digitado :(')




a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

if a > b and a > c:
    print('o maior numero é: {} '.format(a))
elif b > a and b > c:
    print('o maior numero é: {}'.format(b))
else:
    print('o maior numero é {}'.format(c))

print('final do programa')





