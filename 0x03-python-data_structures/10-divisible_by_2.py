#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    l_new = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            l_new[i] = 1
        else:
            l_new[i] = 0
            return l_new
