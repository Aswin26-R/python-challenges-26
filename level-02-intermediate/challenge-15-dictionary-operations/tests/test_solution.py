import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import get_value, add_or_update, remove_key, merge_dicts, invert_dict, get_all_keys


class TestGetValue:
    def test_existing_key(self):
        assert get_value({"a": 1, "b": 2}, "a") == 1

    def test_missing_key_default_none(self):
        assert get_value({"a": 1}, "z") is None

    def test_custom_default(self):
        assert get_value({"a": 1}, "z", "not found") == "not found"

    def test_empty_dict(self):
        assert get_value({}, "key", 0) == 0

    def test_zero_value_exists(self):
        assert get_value({"a": 0}, "a") == 0


class TestAddOrUpdate:
    def test_add_new_key(self):
        result = add_or_update({"a": 1}, "b", 2)
        assert result == {"a": 1, "b": 2}

    def test_update_existing_key(self):
        result = add_or_update({"a": 1}, "a", 99)
        assert result == {"a": 99}

    def test_returns_dict(self):
        result = add_or_update({}, "x", 1)
        assert isinstance(result, dict)

    def test_add_to_empty(self):
        result = add_or_update({}, "key", "value")
        assert result == {"key": "value"}


class TestRemoveKey:
    def test_remove_existing(self):
        result = remove_key({"a": 1, "b": 2}, "a")
        assert result == {"b": 2}

    def test_remove_missing_key(self):
        result = remove_key({"a": 1}, "z")
        assert result == {"a": 1}

    def test_remove_from_empty(self):
        result = remove_key({}, "anything")
        assert result == {}

    def test_returns_dict(self):
        result = remove_key({"a": 1}, "a")
        assert isinstance(result, dict)


class TestMergeDicts:
    def test_basic_merge(self):
        result = merge_dicts({"a": 1, "b": 2}, {"c": 3})
        assert result == {"a": 1, "b": 2, "c": 3}

    def test_d2_wins_conflict(self):
        result = merge_dicts({"a": 1, "b": 2}, {"b": 99, "c": 3})
        assert result == {"a": 1, "b": 99, "c": 3}

    def test_empty_d1(self):
        result = merge_dicts({}, {"a": 1})
        assert result == {"a": 1}

    def test_empty_d2(self):
        result = merge_dicts({"a": 1}, {})
        assert result == {"a": 1}

    def test_does_not_modify_d1(self):
        d1 = {"a": 1}
        d2 = {"b": 2}
        merge_dicts(d1, d2)
        assert d1 == {"a": 1}, "merge_dicts() should not modify d1"

    def test_returns_new_dict(self):
        d1 = {"a": 1}
        result = merge_dicts(d1, {"b": 2})
        assert result is not d1


class TestInvertDict:
    def test_basic_invert(self):
        result = invert_dict({"a": 1, "b": 2, "c": 3})
        assert result == {1: "a", 2: "b", 3: "c"}

    def test_string_values(self):
        result = invert_dict({"x": "y"})
        assert result == {"y": "x"}

    def test_empty(self):
        result = invert_dict({})
        assert result == {}

    def test_returns_dict(self):
        result = invert_dict({"a": 1})
        assert isinstance(result, dict)


class TestGetAllKeys:
    def test_sorted_keys(self):
        result = get_all_keys({"banana": 1, "apple": 2, "cherry": 3})
        assert result == ["apple", "banana", "cherry"]

    def test_empty(self):
        result = get_all_keys({})
        assert result == []

    def test_returns_list(self):
        result = get_all_keys({"a": 1})
        assert isinstance(result, list)

    def test_alphabetical_order(self):
        result = get_all_keys({"z": 1, "a": 2, "m": 3})
        assert result == ["a", "m", "z"]
