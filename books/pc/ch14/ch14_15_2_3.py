def compute_roots(nums):
    from math import sqrt

    result = []
    for n in nums:
        result.append(sqrt(n))
    return result


if __name__ == "__main__":
    nums = range(1000000)
    for n in range(100):
        compute_roots(nums)

# time python books/pc/ch14/ch14_15_3.py
