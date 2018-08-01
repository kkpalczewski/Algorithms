import time
import numpy as np
import math

def find_max_elem(L, start, end):
    now_sum = max(L)
    for l in range(end-start):
        new_sum = sum(L[start:start+l+1])
        if new_sum > now_sum:
            now_sum = new_sum
    return now_sum

def search_array(L):
    now_sum = max(L)
    for l in range(len(L)):
        new_sum = find_max_elem(L,l,len(L))
        if new_sum > now_sum:
            now_sum = new_sum
    return now_sum

def find_max_crossing_subarray(L, start, mid, end):
    left_sum = -10
    right_sum = -10
    new_sum = 0
    for i in reversed(range(len(L[start:mid])+1)):
        new_sum = new_sum + L[i]
        if new_sum > left_sum:
            left_sum = new_sum
            max_left = i
    new_sum = 0
    for i in range(len(L[mid:end])):
        new_sum = new_sum + L[mid+i+1]
        if new_sum > right_sum:
            right_sum = new_sum
            max_right = mid+i+1
    return(max_left, max_right, left_sum + right_sum)

def find_max_subarray(L, start, end):
    if start == end:
        return(start, end, L[start])
    else:
        mid = math.floor((start+end)/2)
        (left_low, left_high, left_sum) = find_max_subarray(L,start, mid)
        (right_low, right_high, right_sum) = find_max_subarray(L, mid+1, end)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(L, start, mid, end)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return(left_low, left_high, left_sum)
        elif right_sum >= right_sum and right_sum >= cross_sum:
            return(right_low, right_high, right_sum)
        else:
            return(cross_low, cross_high, cross_sum)

if __name__ == "__main__":
    for x in range(100,1000,25):
        sum_brute = 0
        sum_elegant = 0
        for y in range(10):
            A = [np.random.rand() for a in range(x)]
            start = time.clock()
            out1 = search_array(A)
            elapsed = time.clock() - start
            start = time.clock()
            (_, _, out2) = find_max_subarray(A,0, len(A)-1)
            elapsed = time.clock() - start
            sum_brute += out1
            sum_elegant += out2
        print(x, sum_brute, sum_elegant, sum_elegant >= sum_brute)