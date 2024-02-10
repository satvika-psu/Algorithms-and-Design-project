import time
import random
import math
import matplotlib.pyplot as plt


# Function to perform radix sort
def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    exp = 1

    # Perform counting sort for every digit place
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Function to perform counting sort for a specific digit place (exp)
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of each digit
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Modify count array to store the position of the next occurrence
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the sorted elements back to the original array
    for i in range(n):
        arr[i] = output[i]

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

# Function to test the radix_sort function on different input scenarios and measure time
def test_radix_sort_with_time(input_generator, *args):
    print("Input:", input_generator.__name__)
    if args:
        array = input_generator(*args)
    else:
        array = input_generator(10000)  
    # Measure the time taken to run radix_sort
    start_time = time.time()
    radix_sort(array)
    end_time = time.time()

    # Print the time taken
    time_taken_data = end_time - start_time
    print(f"Time taken: {end_time - start_time:.6f} seconds\n")

    return time_taken_data

# Driver code
if __name__ == '__main__':
    time_taken_data_radix = []

    n = int(input("Enter an input size: "))

    time_taken = test_radix_sort_with_time(generate_random_integers1, n)
    time_taken_data_radix.append(time_taken)

    time_taken = test_radix_sort_with_time(generate_random_integers2, n, 999)
    time_taken_data_radix.append(time_taken)

    time_taken = test_radix_sort_with_time(generate_random_integers3, n)
    time_taken_data_radix.append(time_taken)

    time_taken = test_radix_sort_with_time(generate_random_integers4, n)
    time_taken_data_radix.append(time_taken)

    time_taken = test_radix_sort_with_time(generate_random_integers5, n)
    time_taken_data_radix.append(time_taken)

    time_taken = test_radix_sort_with_time(generate_in_order_with_swaps, n)
    time_taken_data_radix.append(time_taken)

   
    input_sizes = ['scenario1','scenario2','scenario3','scenario4','scenario5','scenario6']

    # Plotting the graph
    plt.plot(input_sizes, time_taken_data_radix, label="Radix Sort")
    
    plt.xlabel("Input Scenario")
    plt.ylabel("Time Taken (seconds)")
    plt.legend()
    plt.title("Radix Sort Performance")
    plt.show()
