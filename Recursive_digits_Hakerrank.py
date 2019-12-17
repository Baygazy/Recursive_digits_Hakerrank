import functools

def superDigit(n, k):
    li = list(map(int, list(str(n))))
    if k:
        sum_n = [functools.reduce(lambda a, b: a + b, li)] * k
    else:
        sum_n = [functools.reduce(lambda a, b: a + b, li)]
    n = functools.reduce(lambda a, b: a + b, sum_n)
    k = 0
    if n < 10:
        return n
    else:
        return superDigit(n, k)



nk = input('Enter code: ').split()
n = nk[0]

k = int(nk[1])
superDigit
result = superDigit(n, k)
print(result)


