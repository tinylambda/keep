import sys


if __name__ == '__main__':
    print('Smallest difference (epsilon): ', sys.float_info.epsilon)

    print()
    print('Digits(dig): ', sys.float_info.dig)
    print('Mantissa digits (mant_dig): ', sys.float_info.mant_dig)

    print()
    print('Maximum (max): ', sys.float_info.max)
    print('Minimum (min): ', sys.float_info.min)

    print()
    print('Radix of exponents (radix): ', sys.float_info.radix)

    print()
    print('Maximum exponent for radix (max_exp): ', sys.float_info.max_exp)
    print('Minimum exponent for radix (min_exp): ', sys.float_info.min_exp)

    print()
    print('Max. exponent power of 10 (max_10_exp): ', sys.float_info.max_10_exp)
    print('Min. exponent power of 10 (min_10_exp): ', sys.float_info.min_10_exp)

    print()
    print('Rounding for addition (rounds): ', sys.float_info.rounds)
