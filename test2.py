ary = [["A","B","C"],["D","E","F"],["G","H","I","J"]]

def search_index(search_num):
    for i, in_ary in enumerate(ary):
        if search_num in in_ary:
            # それぞれ二次元配列のy,x座標になる
            return [i, in_ary.index(search_num)]
    return -1
x = search_index('I')

print(x)
print(ary[x[0]][x[1]])
