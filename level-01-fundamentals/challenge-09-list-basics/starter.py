def get_first(lst):
    if len(lst) == 0:
        return None
    return lst[0]
    pass
print(get_first([30,20,30]))

def get_last(lst):
    if len(lst) == 0:
        return None
    return lst[-1]
    pass
print(get_last([20,40,60]))

def get_length(lst):
    return len(lst)
    pass
print(get_length([1,2,3,4,5,6]))

def add_item(lst, item):
    lst.append(item)
    return lst
    pass
print(add_item([1,2,3,34],44))

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
    pass
print(remove_item([1,2,3,4],5))

def sort_list(lst):
    return sorted(lst)
    pass
print(sort_list([3,2,4,5]))

def sum_list(lst):
    return sum(lst)
    pass
print(sum_list({1,2,3,4}))