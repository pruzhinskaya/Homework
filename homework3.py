#!/usr/bin/env python3

k1 = (1, 2)
k2 = (3, 4)
spisok = [k1, k2]
print(spisok)

s = set(spisok)
print(s)

k3 = (5, 6)
s.add(k3)
print(s)

d = dict(s)
print(d)

d['key2'] = {7,8}
print(d)

C = list(d)
print(C)

C.insert(1, -15)
print(C, len(C))

t = str(C) 
print(t)

# а) Вам нужно написать функцию, которая на вход принимает имя файла, а возвращает словарь словарей множеств:
# {магазин1: {полка1: {товар1, товар2, ...}, полка2: {товар1,...} }, магазин:{...}, ...}

def sortirovka(name='table.csv'):
    with open(name, encoding='utf-8') as fd:  # encoding нужен для систем, где UTF-8 не по умолчанию
        # text = fd.read()  -  так можно было бы прочесть текст целиком, сейчас нам это не нужно
        shop = []
        shell = []
        goods = []
        for line in fd:
            # a = line.split() - разбивает строку по пробельным символам и кладет подстроки в список
            x, y, z = line.split()
            shop.append(x)
            shell.append(y)
            goods.append(z)

    dic = {}
    for i, j, k in zip(shop,shell,goods):
        group = dic.setdefault(i, [])
        group.append([j,k])

    for k in dic.keys():
        dic_in = {}
        for n in dic[k]:
            group2 = dic_in.setdefault(n[0], set())
            group2.add(n[1])
        dic[k] = dic_in
    return dic

# б) Напишите функцию, которая на вход принимает два аргумента: получившийся словарь и товар, а возвращает
# None, если товара нигде нет, или пару магазин и полка, если товар есть. Если товар есть на нескольких полках, то вернуть можно любую подходящую пару.

def check_goods(dic, goods):
    a = []
    for key, value in dic.items():
        for key_in, value_in in value.items():
            if goods in value_in:
                return key, key_in                   
    return None

if __name__ == '__main__':
    print(check_goods(sortirovka(), "СКОТЧ"))
    print(check_goods(sortirovka(), "ВИСКИ"))
