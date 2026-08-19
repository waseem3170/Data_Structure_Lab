import random
import time

def linear_search(arr, target):
    """O(n) Linear Search"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """O(log n) Binary Search"""
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def demonstrate_quadratic_time(arr):
    """O(n^2) Nested Loop Operation"""
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i] < arr[j]:
                count += 1
    return count

def run_lab_assignment():
    sizes = [10000, 50000, 100000]
    
    print("=" * 70)
    print("LAB ASSIGNMENT 1: TIME COMPLEXITY ANALYSIS (PYTHON)")
    print("=" * 70 + "\n")

    # -------------------------------------------------------------------------
    # TASK 1: Linear Search - O(n)
    # -------------------------------------------------------------------------
    print("--- Task 1: Linear Search [O(n)] ---")
    for n in sizes:
        arr = [random.randint(1, 1000000) for _ in range(n)]
        target = -1  # Force worst-case scenario (item not present)

        start_time = time.perf_counter_ns()
        linear_search(arr, target)
        end_time = time.perf_counter_ns()

        duration_micros = (end_time - start_time) // 1000
        print(f"Array Size (n = {n:>7,}) | Execution Time: {duration_micros:>8,} µs")

    # -------------------------------------------------------------------------
    # TASK 2: Binary Search - O(log n)
    # -------------------------------------------------------------------------
    print("\n--- Task 2: Binary Search [O(log n)] ---")
    for n in sizes:
        arr = sorted([random.randint(1, 1000000) for _ in range(n)])  # Pre-sorted
        target = -1  # Worst-case search target

        start_time = time.perf_counter_ns()
        binary_search(arr, target)
        end_time = time.perf_counter_ns()

        duration_micros = (end_time - start_time) // 1000
        print(f"Array Size (n = {n:>7,}) | Execution Time: {duration_micros:>8,} µs")

    # -------------------------------------------------------------------------
    # TASK 3: Nested Loops Demonstration - O(n^2)
    # -------------------------------------------------------------------------
    print("\n--- Task 3: Nested Loops Demonstration [O(n^2)] ---")
    for n in sizes:
        arr = [random.randint(1, 1000000) for _ in range(n)]

        start_time = time.perf_counter_ns()
        demonstrate_quadratic_time(arr)
        end_time = time.perf_counter_ns()

        duration_micros = (end_time - start_time) // 1000
        duration_sec = duration_micros / 1000000.0
        print(f"Array Size (n = {n:>7,}) | Execution Time: {duration_micros:>12,} µs ({duration_sec:.3f} sec)")

if __name__ == "__main__":
    run_lab_assignment()
