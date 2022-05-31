prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "HPQ": 37.20, "FB": 10.75}

if __name__ == "__main__":
    min_price = min(zip(prices.values(), prices.keys()))
    print(min_price)

    max_price = max(zip(prices.values(), prices.keys()))
    print(max_price)

    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    print(prices_sorted)

    print({v: k for k, v in prices_sorted})

    prices_and_names = zip(prices.values(), prices.keys())
    print(min(prices_and_names))
    print(min(prices_and_names))  # value error: max() arg is an empty sequence
