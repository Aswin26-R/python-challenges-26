import pytest # type: ignore
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import BankAccount


class TestBankAccountInit:
    def test_creates_with_owner(self):
        account = BankAccount("Alice")
        assert account.owner == "Alice"

    def test_default_balance_zero(self):
        account = BankAccount("Alice")
        assert account.get_balance() == 0

    def test_custom_starting_balance(self):
        account = BankAccount("Bob", 500)
        assert account.get_balance() == 500


class TestDeposit:
    def test_basic_deposit(self):
        account = BankAccount("Alice", 100)
        account.deposit(50)
        assert account.get_balance() == 150

    def test_deposit_to_empty(self):
        account = BankAccount("Alice")
        account.deposit(200)
        assert account.get_balance() == 200

    def test_multiple_deposits(self):
        account = BankAccount("Alice", 0)
        account.deposit(100)
        account.deposit(50)
        assert account.get_balance() == 150

    def test_deposit_zero_raises(self):
        account = BankAccount("Alice", 100)
        with pytest.raises(ValueError):
            account.deposit(0)

    def test_deposit_negative_raises(self):
        account = BankAccount("Alice", 100)
        with pytest.raises(ValueError):
            account.deposit(-10)

    def test_deposit_error_message(self):
        account = BankAccount("Alice", 100)
        with pytest.raises(ValueError, match="positive"):
            account.deposit(-1)


class TestWithdraw:
    def test_basic_withdrawal(self):
        account = BankAccount("Alice", 100)
        account.withdraw(30)
        assert account.get_balance() == 70

    def test_withdraw_all(self):
        account = BankAccount("Alice", 100)
        account.withdraw(100)
        assert account.get_balance() == 0

    def test_insufficient_funds_raises(self):
        account = BankAccount("Alice", 100)
        with pytest.raises(ValueError):
            account.withdraw(200)

    def test_withdraw_zero_raises(self):
        account = BankAccount("Alice", 100)
        with pytest.raises(ValueError):
            account.withdraw(0)

    def test_withdraw_negative_raises(self):
        account = BankAccount("Alice", 100)
        with pytest.raises(ValueError):
            account.withdraw(-10)

    def test_insufficient_funds_message(self):
        account = BankAccount("Alice", 100)
        with pytest.raises(ValueError, match="Insufficient funds"):
            account.withdraw(200)


class TestGetBalance:
    def test_initial_balance(self):
        account = BankAccount("Alice", 250)
        assert account.get_balance() == 250


class TestStr:
    def test_str_representation(self):
        account = BankAccount("Alice", 100)
        result = str(account)
        assert "Alice" in result
        assert "100" in result

    def test_str_format(self):
        account = BankAccount("Alice", 150)
        assert str(account) == "BankAccount(owner='Alice', balance=150.00)"

    def test_str_with_decimals(self):
        account = BankAccount("Bob", 99)
        assert "99.00" in str(account)
