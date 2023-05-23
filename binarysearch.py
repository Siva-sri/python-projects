import random
import time
# Implementation of Binary Search Algorithm
# We will prove that Binary Search is faster than Naive Search

# naive search : scan entire list and ask if its equal to the target
# if yes, return index
# if no, return -1

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1
    
# binary search : uses divide and conquer algorithm
# we will leverage the fact that our list is SORTED

def binary_search(l, target, low = None, high = None):
    # Recursive Search
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    # Base case
    if low > high:
        return -1 # Element not found
    
    midpoint = (low+high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else: # target > l[midpoint]
        return binary_search(l, target, midpoint + 1, high)

if __name__ == '__main__':
    l = [1,3,5,10,13,20]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))

    # Proving binary search is better than naive search
    length = 10000

    # building a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))
    # make each element as target and run search for each element, calculating time for the search

    # naive search
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time:",end-start,"seconds")

    # binary search
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time:",end-start,"seconds")
