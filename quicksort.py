import random
import math
import time
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(150000)

# Function for partition position
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

# Function to generate n randomly chosen integers in the range [0...n]
def generate_random_integers1(n):
    return random.sample(range(n+1), n)

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
    for _ in range(int(math.log(n)/2)):
        idx1, idx2 = random.sample(range(n), 2)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr
  

# Function to test the quicksort function on different types of inputs and measure time
def test_quicksort_with_time(input_generator, *args):
    print("Input:", input_generator.__name__)
    if args:
        array = input_generator(*args)
    else:
        array = input_generator(10000) 

    #print("Original array:", array)

    # Measure the time taken to run quicksort
    start_time = time.time()
    quicksort(array, 0, len(array) - 1)
    end_time = time.time()

    #print('Sorted array:')
    #for x in array:
        #print(x, end=" ")
    #print("\n")

    # Print the time taken
    time_taken_data = end_time - start_time
    print(f"Time taken: {end_time - start_time:.6f} seconds\n")
    return time_taken_data


# Driver code
if __name__ == '__main__':
    time_taken_data = []
    
    n = int(input("Enter an inputsize: "))
    time_taken=test_quicksort_with_time(generate_random_integers1, n) 
    time_taken_data.append(time_taken)
       
    time_taken=test_quicksort_with_time(generate_random_integers2, n, 999)
    time_taken_data.append(time_taken)
    time_taken=test_quicksort_with_time(generate_random_integers3, n)
    time_taken_data.append(time_taken)
    time_taken=test_quicksort_with_time(generate_random_integers4, n)
    time_taken_data.append(time_taken)
    time_taken=test_quicksort_with_time(generate_random_integers5, n)
    time_taken_data.append(time_taken)
    time_taken=test_quicksort_with_time(generate_in_order_with_swaps, n)
    time_taken_data.append(time_taken)

    input_sizes = ['scenario1','scenario2','scenario3','scenario4','scenario5','scenario6']
    # Plotting the graph
    print(input_sizes)
    print(time_taken_data)
    plt.plot(input_sizes,time_taken_data, label="Random Integers sizes")
  
    plt.xlabel("Input Size")
    plt.ylabel("Time Taken (seconds)")
    plt.legend()
    plt.title("Quicksort Performance")
    plt.show()


