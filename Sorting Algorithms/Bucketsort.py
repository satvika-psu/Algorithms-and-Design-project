import time
import random
import math
import matplotlib.pyplot as plt

# Function to perform bucket sort
def bucket_sort(arr):
    # Find the maximum and minimum values to determine the range of buckets
    max_val = max(arr)
    min_val = min(arr)
    bucket_size = (max_val - min_val) / len(arr)

    # Create empty buckets
    buckets = [[] for _ in range(len(arr))]

    # Place each element into its respective bucket
    for i in range(len(arr)):
        bucket_index = min(int((arr[i] - min_val) / bucket_size), len(arr) - 1)  # Ensure bucket index is within range
        buckets[bucket_index].append(arr[i])

    # Sort each bucket individually (using another sorting algorithm or recursion)
    for bucket in buckets:
        insertion_sort(bucket)

    # Concatenate the sorted buckets to get the final sorted array
    arr.clear()
    for bucket in buckets:
        arr.extend(bucket)


# Function to perform insertion sort on a bucket
def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

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

# Function to test the bucket_sort function on different input scenarios and measure time
def test_bucket_sort_with_time(input_generator, *args):
    print("Input:", input_generator.__name__)
    if args:
        array = input_generator(*args)
    else:
        array = input_generator(10000)  

    # Measure the time taken to run bucket_sort
    start_time = time.time()
    bucket_sort(array)
    end_time = time.time()

    # Print the time taken
    time_taken_data = end_time - start_time
    print(f"Time taken: {end_time - start_time:.6f} seconds\n")

    return time_taken_data

# Driver code
if __name__ == '__main__':
    time_taken_data_bucket = []

    n = int(input("Enter an input size: "))

    time_taken = test_bucket_sort_with_time(generate_random_integers1, n)
    time_taken_data_bucket.append(time_taken)

    time_taken = test_bucket_sort_with_time(generate_random_integers2, n, 999)
    time_taken_data_bucket.append(time_taken)

    time_taken = test_bucket_sort_with_time(generate_random_integers3, n)
    time_taken_data_bucket.append(time_taken)

    time_taken = test_bucket_sort_with_time(generate_random_integers4, n)
    time_taken_data_bucket.append(time_taken)

    time_taken = test_bucket_sort_with_time(generate_random_integers5, n)
    time_taken_data_bucket.append(time_taken)

    time_taken = test_bucket_sort_with_time(generate_in_order_with_swaps, n)
    time_taken_data_bucket.append(time_taken)

    input_sizes = ['scenario1','scenario2','scenario3','scenario4','scenario5','scenario6']

    # Plotting the graph
    plt.plot(input_sizes, time_taken_data_bucket, label="Bucket Sort")
    
    plt.xlabel("Input Scenario")
    plt.ylabel("Time Taken (seconds)")
    plt.legend()
    plt.title("Bucket Sort Performance")
    plt.show()
