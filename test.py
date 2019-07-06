def create_list(list):
    outside_list = [-1] * 5
    tmp_list = [outside_list]
    ct = -1
    for i in range(1, 4):
        tmp_list.append([ -1 if j == 0 or j == 4 else list[j+ct] for j in range(0, 5)])
        ct += 3
    tmp_list.append(outside_list)
    return tmp_list

# 管理用配列作成
first_list = list(range(1,9))
first_list.append(0)

print(create_list(first_list))
