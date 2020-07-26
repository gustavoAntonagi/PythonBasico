from datetime import datetime, time, timedelta
data = datetime(1815, 12, 10, 00, 00, 00).strftime('%d/%m/%Y')
hora = time(hour=13, minute=14, second=00)
print('{} às {}'.format(data, hora))
