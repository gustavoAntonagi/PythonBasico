class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, massage):
        self.massage = massage
while True:
    try:
        x = int(input('Entre com a nota de 0 a 10: '))
        print(x)
        if x > 10:
            # raise força uma exceção
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido, Digite apenas numeros. ')
    except InputError as ex:
        print(ex)