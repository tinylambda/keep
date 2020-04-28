import statistics


data = [1, 2, 2, 5, 10, 12]
print('median: {:0.2f}'.format(statistics.median(data)))
print('low   : {:0.2f}'.format(statistics.median_low(data)))
print('high  : {:0.2f}'.format(statistics.median_high(data)))

