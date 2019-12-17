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







# def superDigit(n, k):
#     str_li = n * k
#     # return len(str_li)
#     li = [int(i) for i in str_li]
#     sum_n = sum(li)
#     while len(str(sum_n)) != 1:
#         li = [int(i) for i in str(sum_n)]
#         sum_n = sum(li)
#     return sum_n
#
# nk = input('Enter code: ').split()
#
# n = nk[0]
#
# k = int(nk[1])
#
# result = superDigit(n, k)
# print(result)




# arr1 = [1,2,3,4,5]
# x = functools.reduce(lambda x,y: x+y,arr1)
# print(x)