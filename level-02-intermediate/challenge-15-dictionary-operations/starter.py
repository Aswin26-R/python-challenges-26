def get_value(d, key, default=None):
    """
    TODO:
    Return the value for the given key in dictionary d.
    If the key does not exist, return the default value (None if not specified).

    Examples:
        get_value({"a": 1, "b": 2}, "a")            should return 1
        get_value({"a": 1}, "z")                     should return None
        get_value({"a": 1}, "z", "not found")        should return "not found"
        get_value({}, "anything", 0)                  should return 0

    Hint: Use d.get(key, default) — Python dictionaries have this built in!
    """
    pass


def add_or_update(d, key, value):
    """
    TODO:
    Add a new key-value pair to the dictionary, or update the value if the key already exists.
    Return the updated dictionary.

    Examples:
        add_or_update({"a": 1}, "b", 2)   should return {"a": 1, "b": 2}
        add_or_update({"a": 1}, "a", 99)  should return {"a": 99}

    Hint: d[key] = value   sets or updates a key in a dictionary.
    """
    pass


def remove_key(d, key):
    """
    TODO:
    Remove the key from the dictionary if it exists.
    If the key does not exist, do nothing (do not raise an error).
    Return the updated dictionary.

    Examples:
        remove_key({"a": 1, "b": 2}, "a")  should return {"b": 2}
        remove_key({"a": 1}, "z")           should return {"a": 1}  (z not found, unchanged)
        remove_key({}, "anything")           should return {}

    Hint:
        if key in d:
            del d[key]
        return d
    """
    pass


def merge_dicts(d1, d2):
    """
    TODO:
    Merge two dictionaries into a new dictionary and return it.
    If both dictionaries have the same key, the value from d2 wins.
    Do NOT modify d1 or d2.

    Examples:
        merge_dicts({"a": 1, "b": 2}, {"b": 99, "c": 3})
        should return {"a": 1, "b": 99, "c": 3}

        merge_dicts({"x": 10}, {"y": 20})
        should return {"x": 10, "y": 20}

        merge_dicts({}, {"a": 1})
        should return {"a": 1}

    Hint:
        result = d1.copy()   # copy so we don't modify d1
        result.update(d2)    # add/overwrite with d2's values
        return result
    """
    pass


def invert_dict(d):
    """
    TODO:
    Return a new dictionary where keys and values are swapped.
    Original keys become values, original values become keys.

    Examples:
        invert_dict({"a": 1, "b": 2, "c": 3})
        should return {1: "a", 2: "b", 3: "c"}

        invert_dict({"x": "y"})
        should return {"y": "x"}

        invert_dict({})
        should return {}

    Hint: Use a dict comprehension:
          {v: k for k, v in d.items()}
    """
    pass


def get_all_keys(d):
    """
    TODO:
    Return a sorted list of all keys in the dictionary.

    Examples:
        get_all_keys({"banana": 1, "apple": 2, "cherry": 3})
        should return ["apple", "banana", "cherry"]

        get_all_keys({"z": 1, "a": 2, "m": 3})
        should return ["a", "m", "z"]

        get_all_keys({})
        should return []

    Hint: sorted(d.keys()) or sorted(d)
    """
    pass
