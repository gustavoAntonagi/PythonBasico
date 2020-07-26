#MODULOS E FUNÇÕES ANONIMAS (LAMBDA)
#modulos sao arquivos .py que podem se interagir entre eles

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
        self.volume = 10

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

    def max_volume(self):
        if self.ligada:
            if self.volume <= 100:
                self.volume += 1

    def min_volume(self):
        if self.ligada:
            if self.volume >= 0:
                self.volume -= 1

if __name__ == '__main__':

    televisao = Televisao()

    print('A TV está ligada?: {}'.format(televisao.ligada))
    televisao.power()

    print('A TV está ligada?: {}'.format(televisao.ligada))
    televisao.power()
    print('A TV está ligada?: {}'.format(televisao.ligada))

    print('Canal: {}'.format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('A TV está ligada?: {}'.format(televisao.ligada))

    televisao.max_volume()
    print(televisao.volume)

    televisao.min_volume()
    print(televisao.volume)
