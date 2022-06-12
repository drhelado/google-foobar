
def base_n(n, b):
    n = int(n)
    output = []

    while n >= b:
        r = n % b
        output.append(str(r))
        n = (n - r) // b

    output.append(str(n))

    return ''.join(output[::-1])


def base_10(n, b):
    x, y = ''.join(n[::-1]), 0

    for i, v in enumerate(x):
        y += int(v) * (b ** i)

    return y


def solution(n, b):
    #Your code here

    k = len(n)

    minions = []

    while n not in minions:
        minions.append(n)

        n = sorted(n)

        x, y = ''.join(n[::-1]), ''.join(n)

        if b == 10:
            z = int(x) - int(y)
            n = str(z)
        else:
            z = base_10(x, b) - base_10(y, b)
            n = base_n(str(z), b)

        zeros = (k - len(n)) * '0'
        n = zeros + n

    return len(minions) - minions.index(n)
