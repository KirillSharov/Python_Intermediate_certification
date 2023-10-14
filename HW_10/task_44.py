"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""

# Решение задачи 44 без get_dummies


import pandas as pd
import random


def create_lst(lst, lst_dict):
    print(lst, lst_dict)
    res_1, res_2 = [], []
    for el in lst_dict:
        res_1 = [1 if x == el else 0 for x in lst]
        res_2 = [0 if y == el else 1 for y in lst]
        for i in range(len(lst)):
            res_2[i] = [res_2[i],res_1[i]]
    return res_2


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
a_column = list(set(el for el in lst))
a_lst = create_lst(lst, a_column)


df = pd.DataFrame(a_lst, columns=a_column)
print(df)