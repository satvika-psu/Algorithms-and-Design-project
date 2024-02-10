import random
import math
import time
import sys
import matplotlib.pyplot as plt

# Function to heapify a subtree rooted at index i in the array
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if left child exists and is greater than the root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if right child exists and is greater than the root
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

# Function to perform heap sort
def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

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

# Function to test the heap_sort function on different input scenarios and measure time
def test_heap_sort_with_time(input_generator, *args):
    print("Input:", input_generator.__name__)
    if args:
        array = input_generator(*args)
    else:
        array = input_generator(10000)  

    # Measure the time taken to run heap_sort
    start_time = time.time()
    heap_sort(array)
    end_time = time.time()

    # Print the time taken
    time_taken_data = end_time - start_time
    print(f"Time taken: {time_taken_data:.6f} seconds\n")

    return time_taken_data

# Driver code
if __name__ == '__main__':
    time_taken_data_heap = []

    n = int(input("Enter an input size: "))

    time_taken = test_heap_sort_with_time(generate_random_integers1, n)
    time_taken_data_heap.append(time_taken)

    time_taken = test_heap_sort_with_time(generate_random_integers2, n, 999)
    time_taken_data_heap.append(time_taken)

    time_taken = test_heap_sort_with_time(generate_random_integers3, n)
    time_taken_data_heap.append(time_taken)

    time_taken = test_heap_sort_with_time(generate_random_integers4, n)
    time_taken_data_heap.append(time_taken)

    time_taken = test_heap_sort_with_time(generate_random_integers5, n)
    time_taken_data_heap.append(time_taken)

    time_taken = test_heap_sort_with_time(generate_in_order_with_swaps, n)
    time_taken_data_heap.append(time_taken)

    
    input_sizes = ['scenario1','scenario2','scenario3','scenario4','scenario5','scenario6']
    # Plotting the graph
    plt.plot(input_sizes, time_taken_data_heap, label="Heap Sort")
    
    plt.xlabel("Input Scenario")
    plt.ylabel("Time Taken (seconds)")
    plt.legend()
    plt.title("Heap Sort Performance")
    plt.show()
