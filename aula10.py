#Trabalhando com datas

from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A/%B/%Y')
    print(type(data_atual))
    print(data_atual)
    print(type(data_atual_str))
    # print(data_atual.strftime('%d/%m/%Y'))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%d/%m/%y %H:%M:%S '))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.month)
    print(data_atual.year)
    print(data_atual.hour)
    print(data_atual.minute)
    print(data_atual.second)
    print(data_atual.microsecond)
    print(data_atual.date())
    print(data_atual.weekday())

    #mostrar os dias da semana traduzido
    tupla = ('Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabádo', 'Domingo')
    print(tupla[data_atual.weekday()])

    #Mostrar os meses traduzido
    tupla_meses = ('?', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
                   'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    print(tupla_meses[data_atual.month])

    #Mostrando data criada pelo usuario
    data_criada = datetime(2020, 7, 26, 13, 23, 20)
    print(data_criada)
    print(data_atual.strftime('%c'))

    #Convertendo string para datetime
    data_string = '15 do 04 de 1502 às 18 e 30'
    #data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')

    #inicio de um exercicio
    data_convertida = datetime.strptime(data_string, '%d do %m de %Y às %H e %M')
    #fim do exercicio acima

    #LEMBRETE: STRPTIME faz conversões de string para datetime

    print(type(data_convertida))
    print(data_convertida)

    #Subtração e soma entre datas, representa a diferença entre datas
    #nao se esqueça de importar timedelta la no inicio
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)



if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()