import sys
import math

# Ctrl + z or Ctrl + c to see on console.


def main(num):
    sums = 1
    for factor in range(1, int(math.sqrt(num) + 1)):
        if num % factor == 0:
            if factor > 1 and factor != int(num/factor):
                sums += int(num / factor)
                sums += factor
    return sums


for line in sys.stdin.readlines():
    line = int(line)
    divisor_sum = main(num=line)
    if divisor_sum == line:
        print(f"{line} perfect")
    elif abs(divisor_sum - line) <= 2:
        print(f"{line} almost perfect")
    else:
        print(f"{line} not perfect")
