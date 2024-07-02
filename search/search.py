import matplotlib.pyplot as plt
import time
import random

# Function to generate a random array
def generate_random_array(size, lower_bound=1, upper_bound=100000):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

# Function for linear search
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Function for binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Function to plot execution times
def graph_time():
    input_sizes = list(range(1, 5000, 4))
    linear_times_best = []
    linear_times_worst = []
    binary_times_best = []
    binary_times_worst = []

    for size in input_sizes:
        array = generate_random_array(size)
        sorted_array = sorted(array)
        target_best_case_linear = array[0]  # Best case for linear search (first element)
        target_worst_case = -1  # Worst case for both (not in the list)
        target_best_case_binary = sorted_array[size // 2]  # Best case for binary search (middle element)


        # Measure linear search times
        start_time = time.perf_counter()
        linear_search(array, target_best_case_linear)
        end_time = time.perf_counter()
        linear_times_best.append(end_time - start_time)

        start_time = time.perf_counter()
        linear_search(array, target_worst_case)
        end_time = time.perf_counter()
        linear_times_worst.append(end_time - start_time)
        
        # Measure binary search times
        start_time = time.perf_counter()
        binary_search(sorted_array, target_best_case_binary)
        end_time = time.perf_counter()
        binary_times_best.append(end_time - start_time)

        start_time = time.perf_counter()
        binary_search(sorted_array, target_worst_case)
        end_time = time.perf_counter()
        binary_times_worst.append(end_time - start_time)
    
    # Debug print statements to check the measured times
    print("Linear Search Best Case Times:", linear_times_best)
    print("Linear Search Worst Case Times:", linear_times_worst)
    print("Binary Search Best Case Times:", binary_times_best)
    print("Binary Search Worst Case Times:", binary_times_worst)
    
    # Plot the results
    fig, ax = plt.subplots()
    ax.plot(input_sizes, linear_times_best, color='green', linewidth=2.0, label="Linear Search Best Case")
    ax.plot(input_sizes, linear_times_worst, color='blue', linewidth=2.0, label="Linear Search Worst Case")
    # ax.plot(input_sizes, binary_times_best, color='red', linewidth=2.0, label="Binary Search Best Case")
    # ax.plot(input_sizes, binary_times_worst, color='orange', linewidth=2.0, label="Binary Search Worst Case")
    
    plt.xlabel("Size of Array")
    plt.ylabel("Time (seconds)")
    plt.title("Search Algorithm Performance")
    plt.legend()
    plt.grid(True)
    plt.savefig("binary _search_libenaralgo_worst.png", dpi=300, bbox_inches='tight')
    # plt.show()
    print("Graph plotted and saved as search_algorithms.png")

# Run the graphing function
if __name__ == "__main__":
    graph_time()
    # print(binary_search([1,2,3,4,5,5,6,7,8,8,10],5))