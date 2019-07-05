import random

def create_list(list):
    tmp_list = []
    zero_ary = [0] * 5
    ct = 0
    for i in range(0, 5):
        x = []
        if i == 0 or i == 4:
            tmp_list.append(zero_ary)
        else:
            for j in range(0, 5):
                if j == 0 or j == 4 or ct == 9:
                    x.append(0)
                else:
                    x.append(list[ct])
                    ct += 1
            tmp_list.append(x)
    return tmp_list
first_list = [1,2,3,4,5,6,7,8,0]
correct_list = create_list(first_list)
random_list  = create_list(random.sample(first_list, len(first_list)))
print(random_list)
