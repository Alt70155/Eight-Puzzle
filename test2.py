# def split_list(l, n):
#     return [l[idx:idx + n] for idx in range(0, len(l), n)]

split_list = lambda l, n: [l[idx:idx + n] for idx in range(0, len(l), n)]
x = split_list([1,2,3,4,5,6,7,8,9], 3)

print(x)
