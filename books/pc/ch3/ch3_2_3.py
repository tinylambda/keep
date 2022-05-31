import math

if __name__ == "__main__":
    nums = [1.23e18, 1, -1.23e18]
    print(sum(nums))  # output 0.0

    print(math.fsum(nums))  # output 1.0
