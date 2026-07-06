def get_value(d, key, default=None):
    return d.get(key,default)
    pass
print(get_value({"a": 1, "b": 2}, "a"))

def add_or_update(d, key, value):
    d[key] = value
    return d
    pass
print(add_or_update({"a": 1}, "a", 99))

def remove_key(d, key):
    if key in d:
        del d[key]
    return d
    pass
print(remove_key({"a": 1, "b": 2}, "a"))

def merge_dicts(d1, d2):
    result = d1.copy()
    result.update(d2)
    return result
    pass
print(merge_dicts({"x": 10}, {"y": 20}))

def invert_dict(d):
    return {v: k for k, v in d.items()}
    pass
print(invert_dict({"a": 1, "b": 2, "c": 3}))

def get_all_keys(d):
    return sorted(d.keys())
    pass
print(get_all_keys({"banana": 1, "apple": 2, "cherry": 3}))