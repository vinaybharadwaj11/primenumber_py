import math


def SoE(limit):
    max = int(math.sqrt(limit))
    prime = [ x for x in range(2, limit + 1)]
    for n in prime:
        if n == -1:
            continue
        if n > max:
            break
        m = n
        for x in range(m + m - 2, len(prime), m):
            prime[x] = -1
    return [i for i in prime if i != -1]


value = int (input("Enter the range : "))
prime_number = SoE(value)
print(prime_number)