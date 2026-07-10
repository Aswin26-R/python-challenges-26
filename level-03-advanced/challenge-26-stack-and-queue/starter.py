def binary_search_iterative(arr, target):
    """
    TODO:
    Find target in the sorted list arr using an iterative (loop-based) binary search.
    Return the INDEX of target if found.
    Return -1 if target is not in the list.

    The list is SORTED in ascending order.

    Examples:
        binary_search_iterative([1, 3, 5, 7, 9, 11], 7)  → 3
        binary_search_iterative([1, 3, 5, 7, 9, 11], 4)  → -1
        binary_search_iterative([1, 3, 5, 7, 9, 11], 1)  → 0
        binary_search_iterative([1, 3, 5, 7, 9, 11], 11) → 5
        binary_search_iterative([], 5)                     → -1

    Algorithm:
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid        ← found it!
            elif arr[mid] < target:
                low = mid + 1     ← search right half
            else:
                high = mid - 1    ← search left half

        return -1  ← not found
    """
    
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
    pass

print(binary_search_iterative([], 5))


def binary_search_recursive(arr, target, low=0, high=None):
    """
    TODO:
    Find target using RECURSIVE binary search.
    Return the index of target, or -1 if not found.

    Examples:
        binary_search_recursive([1, 3, 5, 7, 9, 11], 7)  → 3
        binary_search_recursive([1, 3, 5, 7, 9, 11], 4)  → -1

    Algorithm (recursive):
        Base case 1: if low > high, return -1  (not found)

        mid = (low + high) // 2

        if arr[mid] == target: return mid
        elif arr[mid] < target: recurse right half
            return binary_search_recursive(arr, target, mid + 1, high)
        else: recurse left half
            return binary_search_recursive(arr, target, low, mid - 1)

    Note: Handle the case where high is None at the start:
        if high is None:
            high = len(arr) - 1
    """
    if  high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = ( low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr,target,mid + 1,high)
    else:
        return binary_search_recursive(arr,target,low,mid - 1)
    pass

print(binary_search_recursive([1, 3, 5, 7, 9, 11], 4))


def find_insert_position(arr, target):
    """
    TODO:
    Return the index where target SHOULD be inserted in arr to keep it sorted.
    If target is already in the list, return the index of its first occurrence.

    Examples:
        find_insert_position([1, 3, 5, 7, 9], 4)   → 2  (between 3 and 5)
        find_insert_position([1, 3, 5, 7, 9], 0)   → 0  (before everything)
        find_insert_position([1, 3, 5, 7, 9], 10)  → 5  (after everything)
        find_insert_position([1, 3, 5, 7, 9], 5)   → 2  (exactly at index 2)
        find_insert_position([], 5)                  → 0

    This is similar to binary search, but instead of returning -1 when not found,
    return the value of 'low' — that's where the target would be inserted.

    Algorithm:
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

        return low  ← insertion point
    """
    low = 0
    high = len(arr) -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid +1
        else:
            high = mid - 1
    return low
    pass

print(find_insert_position([1, 3, 5, 7, 9], 10))
