import random

def create_list(list):
    tmp_list = []
    zero_ary = [-1] * 5
    ct = 0
    for i in range(0, 5):
        x = []
        if i == 0 or i == 4:
            tmp_list.append(zero_ary)
        else:
            for j in range(0, 5):
                if j == 0 or j == 4 or ct == 9:
                    x.append(-1)
                else:
                    x.append(list[ct])
                    ct += 1
            tmp_list.append(x)
    return tmp_list

first_list = [1,2,3,4,5,6,7,8,0]
correct_list = create_list(first_list)
random_list  = create_list(random.sample(first_list, len(first_list)))

def disp():
    # for a in random_list: print(*a)
    for i in range(1,4):
        for j in range(1,4):
            print(random_list[i][j], end='')
        print()

def search(search_num):
    for i in range(1,4):
        if search_num in random_list[i]:
            return i, random_list[i].index(search_num)

while True:
    disp()
    select_num = int(input('入れ替えする数字を入力：'))
    coor = search(select_num)
    x, y = coor[0], coor[1]
    bool = False
    for i in [-1, 1]:
        if random_list[x][y+i] == 0 or random_list[x+i][y] == 0:
            bool = True

    zero_coor = search(0)
    zero_x, zero_y = zero_coor[0], zero_coor[1]
    if bool:
        tmp = random_list[x][y]
        random_list[zero_x][zero_y] = tmp
        random_list[x][y] = 0
        if list == correct_list:
            print('claer')
            break
    else:
        print('no change')
