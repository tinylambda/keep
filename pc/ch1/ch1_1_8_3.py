from pc.ch1.ch1_1_8_2 import prices


print(min(prices))
print(max(prices))

print(min(prices.values()))
print(max(prices.values()))

print(
    min(prices, key=lambda k: prices[k])
)
print(
    max(prices, key=lambda k: prices[k])
)

min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)

prices = {
    'AAA': 45.23,
    'ZZZ': 45.23,
}

print(
    min(zip(prices.values(), prices.keys()))
)

print(
    max(zip(prices.values(), prices.keys()))
)

