import time

# Insertion sort (nondecreasing)


def insertion_sort_asc(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        print(key)
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i -1
        A[i+1] = key
    return A


def insertion_sort_des(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        print(key)
        while i >= 0 and A[i] < key:
            A[i+1] = A[i]
            i = i -1
        A[i+1] = key
    return A



A = [5, 2, 4, 6, 1, 3]
start_time = time.time()
print(insertion_sort_des(A))
print("--- %s seconds ---" % (time.time() - start_time))