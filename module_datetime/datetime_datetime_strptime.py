import datetime

format_ = '%a %b %d %H:%M:%S %Y'
today = datetime.datetime.today()
print('ISO: ', today)

s = today.strftime(format_)
print('strftime: ', s)

d = datetime.datetime.strptime(s, format_)
print('strptime: ', d.strftime(format_))


