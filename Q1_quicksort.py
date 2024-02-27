import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort_random(arr, low, high):
    if low < high:
        pivot_index = random.randint(low, high)  # Random pivot selection
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot = partition(arr, low, high)
        quicksort_random(arr, low, pivot - 1)
        quicksort_random(arr, pivot + 1, high)

def quicksort_nonrandom(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)  # Non-random pivot selection
        quicksort_nonrandom(arr, low, pivot - 1)
        quicksort_nonrandom(arr, pivot + 1, high)

# Example usage:

# Taking comma-separated input
#input_str = input("Enter comma-separated integers: ")
#arr = [int(x.strip()) for x in input_str.split(",")]

arr = [3, 6, 8, 10, 1, 2, 1]
quicksort_random(arr, 0, len(arr)-1)
print("Sorted array using random pivot:", arr)

arr = [3, 6, 8, 10, 1, 2, 1]
quicksort_nonrandom(arr, 0, len(arr)-1)
print("Sorted array using non-random pivot:", arr)
