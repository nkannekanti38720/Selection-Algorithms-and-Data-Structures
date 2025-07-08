# Here, I am implementing the Randomized Quickselect algorithm.
# This algorithm finds the k-th smallest element in expected linear time.

import random

def randomized_quickselect(arr, k):
    # The partition function arranges the array around a randomly chosen pivot.
    def partition(arr, low, high):
        pivot_index = random.randint(low, high)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # This is the recursive function to select the k-th smallest element.
    def select(arr, low, high, k):
        if low == high:
            return arr[low]

        pivot_index = partition(arr, low, high)

        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return select(arr, low, pivot_index - 1, k)
        else:
            return select(arr, pivot_index + 1, high, k)

    return select(arr, 0, len(arr) - 1, k)

# Example usage
arr = [12, 3, 5, 7, 19, 4, 11]
k = 3  # I want to find the 3rd smallest element
result = randomized_quickselect(arr, k)
print(f"The {k+1}-th smallest element is {result}")
