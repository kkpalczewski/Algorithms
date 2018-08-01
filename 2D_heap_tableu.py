import math
import numpy as np


class heap():
    def __init__(self, L):
        self.L = L
        self.num_tree = int(math.sqrt(len(self.L)))

    def __getitem__(self, item):
        return self.L[item]

    def __setitem__(self, key, item):
        self.L[key] = item

    def __len__(self):
        return len(self.L)

def position(L, index):
    return L[index], math.floor(index/L.num_tree), int(index % L.num_tree)

def right(L, index):
    row = position(L, index)[2]
    if row == (L.num_tree - 1):
        return None
    else:
        return index+1

def down(L, index):
    col = position(L, index)[1]
    if col == (L.num_tree - 1):
        return None
    else:
        return index+L.num_tree

def heapify(L, index):
    r = right(L, index)
    d = down(L, index)
    max_index = index
    if not r == None:
        if L[r] > L[max_index]:
            max_index = r
    if not d == None:
        if L[d] > L[max_index]:
            max_index = d
    if index != max_index:
        temp = L[index]
        L[index] = L[max_index]
        L[max_index] = temp
        heapify(L, max_index)


def do_tableu(L):
    for i in reversed(range(len(L))):
        heapify(L, i)

def printable_tableu(L):
    A = []
    for col in range(L.num_tree):
        A.append(L[L.num_tree*col:L.num_tree*col+L.num_tree])
    return np.matrix(A)

if __name__ == '__main__':
    B = heap([int(1000*np.random.rand()) for x in range(int(math.pow(10,2)))])
    L = heap([0,1,2,3,4,5,6,7,8])
    do_tableu(B)
    A = printable_tableu(B)
    print(A)