import statistics


data = [10, 20, 30, 40]

print('1: {:0.2f}'.format(statistics.median_grouped(data, interval=1)))
print('2: {:0.2f}'.format(statistics.median_grouped(data, interval=2)))
print('3: {:0.2f}'.format(statistics.median_grouped(data, interval=3)))

