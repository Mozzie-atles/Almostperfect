import sys
import math

# Ctrl + z or Ctrl + c to see on console.


def main(num):
    sums = []
    for factor in range(1, int(math.sqrt(num) + 1)):
        if num % factor == 0:
            yield factor
            if factor*factor != num:
                sums.append(int(num/factor))
    for divisor in reversed(sums):
        yield divisor


for line in sys.stdin.readlines():
    line = int(line)
    divisor = list(main(line))[:-1]
    divisor_sum = sum(divisor)
    if divisor_sum == line:
        print(f"{line} perfect")
    elif divisor_sum in range(line - 2, line + 3):
        print(f"{line} almost perfect")
    else:
        print(f"{line} not perfect")
