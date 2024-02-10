import random
import math
import time
import sys
import matplotlib.pyplot as plt

# Function to perform merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
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

# Function to test the merge_sort function on different input scenarios and measure time
def test_merge_sort_with_time(input_generator, *args):
    print("Input:", input_generator.__name__)
    if args:
        array = input_generator(*args)
    else:
        array = input_generator(10000)  

    # Measure the time taken to run merge_sort
    start_time = time.time()
    merge_sort(array)
    end_time = time.time()

    # Print the time taken
    time_taken_data = end_time - start_time
    print(f"Time taken: {end_time - start_time:.6f} seconds\n")

    return time_taken_data

# Driver code
if __name__ == '__main__':
    time_taken_data_merge = []

    n = int(input("Enter an input size: "))

    time_taken = test_merge_sort_with_time(generate_random_integers1, n)
    time_taken_data_merge.append(time_taken)

    time_taken = test_merge_sort_with_time(generate_random_integers2, n, 999)
    time_taken_data_merge.append(time_taken)

    time_taken = test_merge_sort_with_time(generate_random_integers3, n)
    time_taken_data_merge.append(time_taken)

    time_taken = test_merge_sort_with_time(generate_random_integers4, n)
    time_taken_data_merge.append(time_taken)

    time_taken = test_merge_sort_with_time(generate_random_integers5, n)
    time_taken_data_merge.append(time_taken)

    time_taken = test_merge_sort_with_time(generate_in_order_with_swaps, n)
    time_taken_data_merge.append(time_taken)

    
    input_sizes = ['scenario1','scenario2','scenario3','scenario4','scenario5','scenario6']

    # Plotting the graph
    plt.plot(input_sizes, time_taken_data_merge, label="Merge Sort")
    
    plt.xlabel("Input Scenario")
    plt.ylabel("Time Taken (seconds)")
    plt.legend()
    plt.title("Merge Sort Performance")
    plt.show()
