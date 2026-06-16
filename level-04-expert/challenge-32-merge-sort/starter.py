def merge(left, right):
    """
    TODO:
    Merge two sorted lists into a single sorted list.
    Both 'left' and 'right' are already sorted in ascending order.

    Examples:
        merge([1, 3, 5], [2, 4, 6])    → [1, 2, 3, 4, 5, 6]
        merge([1, 2, 3], [])            → [1, 2, 3]
        merge([], [4, 5])               → [4, 5]
        merge([1], [2])                 → [1, 2]

    Algorithm:
        result = []
        i = 0  (index into left)
        j = 0  (index into right)

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # One list may still have items — add them all
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    """
    pass


def merge_sort(arr):
    """
    TODO:
    Sort the list using the Merge Sort algorithm.
    Return a NEW sorted list — do not modify the original.

    Examples:
        merge_sort([38, 27, 43, 3, 9, 82, 10])  → [3, 9, 10, 27, 38, 43, 82]
        merge_sort([5, 2, 4, 1, 3])              → [1, 2, 3, 4, 5]
        merge_sort([])                            → []
        merge_sort([1])                           → [1]
        merge_sort([2, 1])                        → [1, 2]

    Algorithm:
        Base case: if len(arr) <= 1, return arr  (already sorted)

        Otherwise:
            1. Find the midpoint: mid = len(arr) // 2
            2. Recursively sort each half:
               left = merge_sort(arr[:mid])
               right = merge_sort(arr[mid:])
            3. Merge and return:
               return merge(left, right)
    """
    pass


def merge_sort_inplace(arr):
    """
    TODO:
    Sort the list IN PLACE using merge sort.
    Modify arr directly instead of returning a new list.

    This version should produce the same sorted result, but by modifying
    the original list object.

    Example:
        data = [3, 1, 4, 1, 5, 9]
        merge_sort_inplace(data)
        data  → [1, 1, 3, 4, 5, 9]

    Hint:
        sorted_arr = merge_sort(arr)  ← use your existing function
        arr.clear()
        arr.extend(sorted_arr)
        (This modifies the original list)
    """
    pass
