import pytest
import time
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import Timer, managed_list, suppress_errors


class TestTimer:
    def test_elapsed_is_set(self):
        with Timer() as t:
            pass
        assert t.elapsed is not None
        assert t.elapsed >= 0

    def test_elapsed_reasonable_value(self):
        with Timer() as t:
            time.sleep(0.05)
        assert t.elapsed >= 0.04, "Elapsed should be at least ~0.05 seconds"
        assert t.elapsed < 1.0, "Elapsed should not be more than 1 second for a short sleep"

    def test_returns_self(self):
        with Timer() as t:
            pass
        assert isinstance(t, Timer)

    def test_does_not_suppress_exceptions(self):
        with pytest.raises(ValueError):
            with Timer():
                raise ValueError("test error")

    def test_elapsed_zero_for_instant_code(self):
        with Timer() as t:
            x = 2 + 2
        assert t.elapsed >= 0


class TestManagedList:
    def test_yields_empty_list(self):
        with managed_list() as items:
            assert items == []

    def test_items_can_be_appended(self):
        with managed_list() as items:
            items.append(1)
            items.append(2)
        assert items == [1, 2]

    def test_yields_list_type(self):
        with managed_list() as items:
            assert isinstance(items, list)

    def test_multiple_items(self):
        with managed_list() as items:
            for i in range(5):
                items.append(i)
        assert items == [0, 1, 2, 3, 4]


class TestSuppressErrors:
    def test_suppresses_specified_exception(self):
        with suppress_errors(ValueError):
            raise ValueError("should be suppressed")
        # if we get here, exception was suppressed successfully

    def test_does_not_suppress_other_exceptions(self):
        with pytest.raises(TypeError):
            with suppress_errors(ValueError):
                raise TypeError("not suppressed")

    def test_no_exception_works_normally(self):
        result = []
        with suppress_errors(ValueError):
            result.append(42)
        assert result == [42]

    def test_multiple_exception_types(self):
        with suppress_errors(ValueError, TypeError):
            raise TypeError("suppressed")

    def test_int_conversion_suppressed(self):
        with suppress_errors(ValueError):
            int("not_a_number")
