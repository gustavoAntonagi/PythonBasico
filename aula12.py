#Entender o que são pacotes
#Aprender a instalar e utilizar pacotes
#Aprender a fazer requisições http (chamada de APIS

#Detalhes
#O que são pacotes
#O que é o instalador de pacotes python (PIP)
#Como instalar um pacote no python
#Como listar pacotes instalados no Python
#Como utilizar um pacote
#Instalar nosso primeiro pacote (Request)
#Realizar uma requisição http com request

#Basta colocar import requests e instalar as requests atraves do erro que for informado,
# caso não apareça na IDE após a instalação no Powershell ou CMD
import requests


def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/09110560/json/'.format(cep))
    print(response.status_code)
    #200 retornou sucesso
    print(response.text)

    #retorna o texto da API
    print(type(response.text))

    #json retorna um formato dicionario
    print(response.json())
    print(type(response.json()))

    #Retorna aquilo que for colocado
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    #retorna o html da pagina google ou a que colocar
    # response  = retorna_response('https://www.google.com/?gws_rd=ssl')
    # print(response)
    #retorna_dados_cep('09110560')
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon['sprites']['front_shiny'])