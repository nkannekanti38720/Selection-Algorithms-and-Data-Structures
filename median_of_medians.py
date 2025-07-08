# I am implementing the Deterministic Median of Medians algorithm here.
# This will allow me to find the k-th smallest element in an array in worst-case linear time.

def median_of_medians(arr, k):
    # The partition function arranges the array around a pivot and returns its index.
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # I use this helper function to find the median of medians in the array
    def median_of_medians_helper(arr, low, high):
        if high - low + 1 <= 5:
            # If there are fewer than 5 elements, I can sort and return the middle element
            return sorted(arr[low:high + 1])[len(arr[low:high + 1]) // 2]

        # I group elements into sets of 5 and calculate the median of each group
        medians = []
        for i in range(low, high + 1, 5):
            group = arr[i:min(i + 5, high + 1)]
            medians.append(sorted(group)[len(group) // 2])

        # Now I recursively apply the algorithm to the medians
        return median_of_medians_helper(medians, 0, len(medians) - 1)

    # This is the main recursive selection function
    def select(arr, low, high, k):
        if low == high:
            return arr[low]

        pivot_index = median_of_medians_helper(arr, low, high)
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
result = median_of_medians(arr, k)
print(f"The {k+1}-th smallest element is {result}")
