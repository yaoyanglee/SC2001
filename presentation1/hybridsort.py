<<<<<<< HEAD:presentation1/hybridsort.py
import numpy as np
from insertionsort import insertionSort
=======
# TODO: Generation of arrays of different lengths, make use of randInt() function
# TODO: Make new branches for yourselves and edit wherever

# Deliverables:
    # - Make branches
    # - For ZJ:
    #     - fucking start watching lecs from week 1 to 3 you idiot

def insertionSort(arr):
    comparisons = 0
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
>>>>>>> 8885aa703849566dc610479ef8b9594312315cf8:presentation1/code.py

# def insertionSort(arr):
#     comparisons = 0
#     # Traverse through 1 to len(arr)
#     for i in range(1, len(arr)):

#         key = arr[i]

#         # Move elements of arr[0..i-1], that are
#         # greater than key, to one position ahead
#         # of their current position
#         j = i-1
#         while j >= 0 and key < arr[j]:
#             comparisons+=1
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

#     return comparisons, arr

def hybridsort(arr, S):
    if len(arr) > 1:

        if(len(arr) <= S):
            comparisons,arr = insertionSort(arr)
            return comparisons

        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # Into 2 halves
        R = arr[mid:]

        # Sorting the first half
        comparisons_L = hybridsort(L,S)

        # Sorting the second half
        comparisons_R = hybridsort(R,S)

        i = j = k = 0
        comparisons = comparisons_L + comparisons_R

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            comparisons+=1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        return comparisons
    
    return 0


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
            
# 361, 381, 401, 421, 441, 461, 481
# hybridsort_arr = [8,4,3,6,1,9,2,4,10,14,21,66,61,15,77]
# hybridsort_arr = list(np.random.randint(1, 1000, 1000))
# printList(hybridsort_arr)
# print()