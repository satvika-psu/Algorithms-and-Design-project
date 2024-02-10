import time
import random
import math
import matplotlib.pyplot as plt

# Function to perform Tim Sort
def tim_sort(arr):
    min_run = 32
    n = len(arr)

    # Insertion sort for small chunks (min_run)
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    # Merge the sorted chunks using merge sort
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min((left + size - 1), (n - 1))
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size = 2 * size

# Function to perform insertion sort on a chunk of the array
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

# Function to merge two sorted chunks of the array
def merge(arr, left, mid, right):
    len1, len2 = mid - left + 1, right - mid
    left_chunk, right_chunk = arr[left : mid + 1], arr[mid + 1 : right + 1]

    i, j, k = 0, 0, left

    while i < len1 and j < len2:
        if left_chunk[i] <= right_chunk[j]:
            arr[k] = left_chunk[i]
            i += 1
        else:
            arr[k] = right_chunk[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left_chunk[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right_chunk[j]
        j += 1
        k += 1

# Function to generate n randomly chosen integers in the range [0...n]
def generate_random_integers1(n):
    return random.sample(range(n + 1), n)

# Function to generate n randomly chosen integers in the range [0...k], k < 1000
def generate_random_integers2(n, k):
    return [random.randint(0, k) for _ in range(n)]

# Function to generate n randomly chosen integers in the range [0...n^3]
def generate_random_integers3(n):
    return [random.randint(0, n**3) for _ in range(n)]

# Function to generate n randomly chosen integers in the range [0...logn]
def generate_random_integers4(n):
    return [random.randint(0, int(math.log(n))) for _ in range(n)]

# Function to generate n randomly chosen integers that are multiples of 1000 in the range [0...n]
def generate_random_integers5(n):
    return [random.randint(0, n) * 1000 for _ in range(n)]

# Function to generate in-order integers [0...n] with logn/2 randomly chosen values swapped with another value
def generate_in_order_with_swaps(n):
    arr = list(range(n))
    for _ in range(int(math.log(n) / 2)):
        idx1, idx2 = random.sample(range(n), 2)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

# Function to test the tim_sort function on different input scenarios and measure time
def test_tim_sort_with_time(input_generator, *args):
    print("Input:", input_generator.__name__)
    if args:
        array = input_generator(*args)
    else:
        array = input_generator(10000)  

    # Measure the time taken to run tim_sort
    start_time = time.time()
    tim_sort(array)
    end_time = time.time()

    # Print the time taken
    time_taken_data = end_time - start_time
    print(f"Time taken: {end_time - start_time:.6f} seconds\n")

    return time_taken_data

# Driver code
if __name__ == '__main__':
    time_taken_data_tim = []

    n = int(input("Enter an input size: "))

    time_taken = test_tim_sort_with_time(generate_random_integers1, n)
    time_taken_data_tim.append(time_taken)

    time_taken = test_tim_sort_with_time(generate_random_integers2, n, 999)
    time_taken_data_tim.append(time_taken)

    time_taken = test_tim_sort_with_time(generate_random_integers3, n)
    time_taken_data_tim.append(time_taken)

    time_taken = test_tim_sort_with_time(generate_random_integers4, n)
    time_taken_data_tim.append(time_taken)

    time_taken = test_tim_sort_with_time(generate_random_integers5, n)
    time_taken_data_tim.append(time_taken)

    time_taken = test_tim_sort_with_time(generate_in_order_with_swaps, n)
    time_taken_data_tim.append(time_taken)

    input_sizes = ['scenario1','scenario2','scenario3','scenario4','scenario5','scenario6']

    # Plotting the graph
    plt.plot(input_sizes, time_taken_data_tim, label="Tim Sort")
    
    plt.xlabel("Input Scenario")
    plt.ylabel("Time Taken (seconds)")
    plt.legend()
    plt.title("Tim Sort Performance")
    plt.show()
