#Gere, Copie, Mova, Escreva e leia informações de arquivos externos
import shutil

def escrever_arquivo(texto):
    diretorio = 'C:/Users/solan/Music/python/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.write('Minha primeira escrita')
    arquivo.write('\nPara escrever use o "w" exemplo: '
                  '\narquivo = open("texto.txt", "w" e para atualizar use o "a"')
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)

    ##split transforma em lista pulando linha
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []

    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        #list comparation
        media = lambda notas: sum([int(i) for i in notas]) /4
        print('Sua média é: {}'.format(media(lista_notas)))
        lista_media.append({aluno:media(lista_notas)})
        return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/solan/Music/python')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/solan/Music')

if __name__ == '__main__':
    move_arquivo('notas.txt')
    #copia_arquivo('notas.txt')
    # lista_medias = media_notas('notas.txt')
    # print(lista_medias)
#escrever_arquivo('Primeira linha novamente.\n')
    # aluno = 'joao, 9, 10, 5, 5\n'
    # atualizar_arquivo('notas.txt', aluno)
# ler_arquivo('teste.txt')