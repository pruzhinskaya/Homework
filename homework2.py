#!/usr/bin/env python3

def isint(n):
    return int(n) == float(n)

def word(name):
    for i in range(len(name)):
        if i == 0:
            print(name)
        else:
            i = -i
            print(name[:i])

def word2(name):
    for i in range(len(name)):
        if i == 0:
            print(name)
        else:
            i = -i
            print(name[i:] + name[:i])

def change_order(listik):
    for i in range(len(listik)-1):
        j = i/2
        if isint(j):
            a = listik[i]
            listik[i] = listik[i+1]
            listik[i+1] = a

def pair(listik):
    k = 0
    for i in range(len(listik)):
        for j in listik[i+1:]:
            if listik[i] == j:
                k = k + 1
    return k



if __name__ == '__main__':
    word('abracadabra')
    word2('abracadabra')
    Spisok = [2, 1, 1 ,2, 1, 'SNIa', 'SNIa', 'SNII']
    change_order(Spisok)
    print(Spisok)   
    print(pair(Spisok))

# x = [[]]*3 # the list contains 3 empty lists is created
# x[0].append('a') # all lists are the same that's why 'a' is added to all of them
# x[1].append('b')
# x[2].append('c')
# x[0]=['d']