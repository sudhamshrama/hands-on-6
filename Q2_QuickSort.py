import random
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
    stack = []
    stack.append((low, high))
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = partition(arr, low, high)
            stack.append((low, pivot - 1))
            stack.append((pivot + 1, high))

def generate_best_case_input(n):
    return list(range(n))

def generate_worst_case_input(n):
    return list(range(n, 0, -1))

def generate_average_case_input(n):
    return [random.randint(1, n) for _ in range(n)]

def benchmark(inputs):
    timings = []
    for arr in inputs:
        time = timeit.timeit(lambda: quicksort(arr, 0, len(arr) - 1), number=1)
        timings.append(time)
    return timings

# Benchmarking
input_sizes = [100, 500, 1000, 2000, 5000]  # Array input sizes "n"
best_case_inputs = [generate_best_case_input(n) for n in input_sizes]
worst_case_inputs = [generate_worst_case_input(n) for n in input_sizes]
average_case_inputs = [generate_average_case_input(n) for n in input_sizes]

best_case_timings = benchmark(best_case_inputs)
worst_case_timings = benchmark(worst_case_inputs)
average_case_timings = benchmark(average_case_inputs)

# Plotting
plt.plot(input_sizes, best_case_timings, label='Best Case')
plt.plot(input_sizes, worst_case_timings, label='Worst Case')
plt.plot(input_sizes, average_case_timings, label='Average Case')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Quicksort Benchmark (Non-Random Pivot)')
plt.legend()
plt.show()
