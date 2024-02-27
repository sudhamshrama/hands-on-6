# hands-on-6

In the code above:

- quicksort_random function implements quicksort with a random choice for the pivot.
- quicksort_nonrandom function implements quicksort with a non-random choice for the pivot (usually the first element).
- partition function is a helper function that partitions the array around the pivot.
- Example usage demonstrates how to use both implementations of quicksort.


### 2.a) Best Case Scenario:

The best case for quicksort is when the pivot chosen always divides the array into two nearly equal halves. In this case, the time complexity is \( O(n \log n) \). We'll generate arrays already sorted in ascending order.

```python
import timeit
import matplotlib.pyplot as plt

def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[low] = arr[low], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)

def generate_best_case_input(n):
    return list(range(n))

def benchmark(inputs):
    timings = []
    for arr in inputs:
        time = timeit.timeit(lambda: quicksort(arr, 0, len(arr) - 1), number=1)
        timings.append(time)
    return timings

# Benchmarking
input_sizes = [100, 500, 1000, 2000, 5000]  # Array input sizes "n"
best_case_inputs = [generate_best_case_input(n) for n in input_sizes]

best_case_timings = benchmark(best_case_inputs)

# Plotting
plt.plot(input_sizes, best_case_timings, label='Best Case')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Quicksort Benchmark - Best Case')
plt.legend()
plt.show()
```

### 2.b) Worst Case Scenario:

The worst case for quicksort is when the pivot chosen always partitions the array in such a way that one partition has no elements. In this case, the time complexity is \( O(n^2) \). We'll generate arrays sorted in descending order.

```python
def generate_worst_case_input(n):
    return list(range(n, 0, -1))

# Benchmarking
worst_case_inputs = [generate_worst_case_input(n) for n in input_sizes]

worst_case_timings = benchmark(worst_case_inputs)

# Plotting
plt.plot(input_sizes, worst_case_timings, label='Worst Case')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Quicksort Benchmark - Worst Case')
plt.legend()
plt.show()
```

### 2.c) Average Case Scenario:

The average case for quicksort occurs when the pivot chosen divides the array into two partitions of roughly equal size. We'll generate arrays with random elements.

```python
import random

def generate_average_case_input(n):
    return [random.randint(1, n) for _ in range(n)]

# Benchmarking
average_case_inputs = [generate_average_case_input(n) for n in input_sizes]

average_case_timings = benchmark(average_case_inputs)

# Plotting
plt.plot(input_sizes, average_case_timings, label='Average Case')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Quicksort Benchmark - Average Case')
plt.legend()
plt.show()
```

By running these three scripts, you'll get benchmarks for the best case, worst case, and average case scenarios of quicksort with non-random pivot selection.
