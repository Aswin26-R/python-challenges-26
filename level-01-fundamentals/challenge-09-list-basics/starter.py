def get_first(lst):
    """
    TODO:
    Return the first item in the list.
    If the list is empty, return None.

    Examples:
        get_first([10, 20, 30])  should return 10
        get_first(["a", "b"])    should return "a"
        get_first([])            should return None

    Hint: Check if the list is empty first:
        if len(lst) == 0:
            return None
        return lst[0]
    """
    pass


def get_last(lst):
    """
    TODO:
    Return the last item in the list.
    If the list is empty, return None.

    Examples:
        get_last([10, 20, 30])  should return 30
        get_last(["a", "b"])    should return "b"
        get_last([])            should return None

    Hint: Use a negative index: lst[-1] gives you the last item.
    """
    pass


def get_length(lst):
    """
    TODO:
    Return the number of items in the list.

    Examples:
        get_length([1, 2, 3, 4])  should return 4
        get_length([])            should return 0
        get_length(["hello"])     should return 1

    Hint: Use the len() function: len(lst)
    """
    pass


def add_item(lst, item):
    """
    TODO:
    Add the item to the END of the list and return the updated list.

    Examples:
        add_item([1, 2, 3], 4)        should return [1, 2, 3, 4]
        add_item([], "hello")          should return ["hello"]
        add_item(["a", "b"], "c")     should return ["a", "b", "c"]

    Hint: Use lst.append(item) to add to the end.
          append() modifies the list IN PLACE and returns None,
          so you need to append first, then return the list.
    """
    pass


def remove_item(lst, item):
    """
    TODO:
    Remove the FIRST occurrence of item from the list and return the updated list.
    If the item is not in the list, return the list unchanged (do not raise an error).

    Examples:
        remove_item([1, 2, 3, 2], 2)  should return [1, 3, 2]  (removes FIRST 2 only)
        remove_item([1, 2, 3], 2)     should return [1, 3]
        remove_item([1, 2, 3], 99)    should return [1, 2, 3]  (99 not found, unchanged)

    Hint:
        Check if item is in the list before removing:
        if item in lst:
            lst.remove(item)
        return lst
    """
    pass


def sort_list(lst):
    """
    TODO:
    Return a new list with the items sorted in ascending order.
    Do NOT modify the original list.

    Examples:
        sort_list([3, 1, 2])        should return [1, 2, 3]
        sort_list([5, 3, 8, 1])     should return [1, 3, 5, 8]
        sort_list(["c", "a", "b"])  should return ["a", "b", "c"]
        sort_list([])               should return []

    Hint: Use sorted(lst) — this returns a NEW sorted list without modifying the original.
          Do NOT use lst.sort() for this — it modifies the original list in place.
    """
    pass


def sum_list(lst):
    """
    TODO:
    Return the sum of all numbers in the list.
    If the list is empty, return 0.

    Examples:
        sum_list([1, 2, 3, 4])  should return 10
        sum_list([10, -5, 5])   should return 10
        sum_list([])            should return 0
        sum_list([7])           should return 7

    Hint: Use Python's built-in sum() function: sum(lst)
    """
    pass
