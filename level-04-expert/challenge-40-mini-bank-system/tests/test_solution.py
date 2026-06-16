import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import (
    Account, SavingsAccount, CheckingAccount, Bank,
    InsufficientFundsError, AccountNotFoundError, InvalidAmountError
)


class TestExceptions:
    def test_insufficient_funds_is_exception(self):
        assert issubclass(InsufficientFundsError, Exception)

    def test_account_not_found_is_exception(self):
        assert issubclass(AccountNotFoundError, Exception)

    def test_invalid_amount_is_exception(self):
        assert issubclass(InvalidAmountError, Exception)


class TestAccount:
    def test_initial_balance(self):
        acc = Account("Alice")
        assert acc.get_balance() == 0.0

    def test_initial_balance_nonzero(self):
        acc = Account("Alice", balance=500.0)
        assert acc.get_balance() == 500.0

    def test_has_account_id(self):
        acc = Account("Alice")
        assert hasattr(acc, "account_id")
        assert acc.account_id is not None

    def test_unique_ids(self):
        acc1 = Account("Alice")
        acc2 = Account("Bob")
        assert acc1.account_id != acc2.account_id

    def test_deposit_increases_balance(self):
        acc = Account("Alice")
        acc.deposit(500)
        assert acc.get_balance() == 500.0

    def test_deposit_returns_balance(self):
        acc = Account("Alice")
        result = acc.deposit(500)
        assert result == 500.0

    def test_deposit_negative_raises(self):
        acc = Account("Alice")
        with pytest.raises(InvalidAmountError):
            acc.deposit(-100)

    def test_deposit_zero_raises(self):
        acc = Account("Alice")
        with pytest.raises(InvalidAmountError):
            acc.deposit(0)

    def test_withdraw_decreases_balance(self):
        acc = Account("Alice", balance=1000.0)
        acc.withdraw(300)
        assert acc.get_balance() == 700.0

    def test_withdraw_returns_balance(self):
        acc = Account("Alice", balance=1000.0)
        result = acc.withdraw(300)
        assert result == 700.0

    def test_withdraw_insufficient_raises(self):
        acc = Account("Alice", balance=100.0)
        with pytest.raises(InsufficientFundsError):
            acc.withdraw(200)

    def test_withdraw_negative_raises(self):
        acc = Account("Alice", balance=100.0)
        with pytest.raises(InvalidAmountError):
            acc.withdraw(-50)

    def test_history_records_deposit(self):
        acc = Account("Alice")
        acc.deposit(500)
        history = acc.get_history()
        assert len(history) == 1
        assert history[0]["type"] == "deposit"
        assert history[0]["amount"] == 500.0

    def test_history_records_withdrawal(self):
        acc = Account("Alice", balance=1000.0)
        acc.withdraw(200)
        history = acc.get_history()
        assert history[-1]["type"] == "withdrawal"
        assert history[-1]["amount"] == 200.0
        assert history[-1]["balance_after"] == 800.0

    def test_str_representation(self):
        acc = Account("Alice")
        result = str(acc)
        assert "Alice" in result


class TestSavingsAccount:
    def test_is_account_subclass(self):
        assert issubclass(SavingsAccount, Account)

    def test_default_interest_rate(self):
        acc = SavingsAccount("Alice")
        assert acc.interest_rate == 0.05

    def test_custom_interest_rate(self):
        acc = SavingsAccount("Alice", interest_rate=0.1)
        assert acc.interest_rate == 0.1

    def test_apply_interest_increases_balance(self):
        acc = SavingsAccount("Alice", interest_rate=0.1)
        acc.deposit(1000)
        acc.apply_interest()
        assert acc.get_balance() == 1100.0

    def test_apply_interest_returns_balance(self):
        acc = SavingsAccount("Alice", interest_rate=0.1)
        acc.deposit(1000)
        result = acc.apply_interest()
        assert result == 1100.0

    def test_apply_interest_recorded_in_history(self):
        acc = SavingsAccount("Alice", interest_rate=0.05)
        acc.deposit(1000)
        acc.apply_interest()
        types = [h["type"] for h in acc.get_history()]
        assert "interest" in types


class TestCheckingAccount:
    def test_is_account_subclass(self):
        assert issubclass(CheckingAccount, Account)

    def test_default_overdraft_limit(self):
        acc = CheckingAccount("Bob")
        assert acc.overdraft_limit == 100.0

    def test_overdraft_allowed(self):
        acc = CheckingAccount("Bob", overdraft_limit=100.0)
        acc.deposit(50)
        acc.withdraw(100)  # balance = -50 — within overdraft
        assert acc.get_balance() == -50.0

    def test_overdraft_exceeded_raises(self):
        acc = CheckingAccount("Bob", overdraft_limit=100.0)
        acc.deposit(50)
        with pytest.raises(InsufficientFundsError):
            acc.withdraw(200)  # would be -150, exceeds -100 limit

    def test_withdraw_zero_raises(self):
        acc = CheckingAccount("Bob")
        with pytest.raises(InvalidAmountError):
            acc.withdraw(0)


class TestBank:
    def test_create_checking_account(self):
        bank = Bank()
        acc = bank.create_account("Alice", "checking")
        assert isinstance(acc, CheckingAccount)

    def test_create_savings_account(self):
        bank = Bank()
        acc = bank.create_account("Bob", "savings")
        assert isinstance(acc, SavingsAccount)

    def test_get_account(self):
        bank = Bank()
        acc = bank.create_account("Alice")
        found = bank.get_account(acc.account_id)
        assert found is acc

    def test_get_missing_account_raises(self):
        bank = Bank()
        with pytest.raises(AccountNotFoundError):
            bank.get_account("fake-id")

    def test_deposit(self):
        bank = Bank()
        acc = bank.create_account("Alice")
        bank.deposit(acc.account_id, 500)
        assert bank.get_balance(acc.account_id) == 500.0

    def test_withdraw(self):
        bank = Bank()
        acc = bank.create_account("Alice")
        bank.deposit(acc.account_id, 1000)
        bank.withdraw(acc.account_id, 300)
        assert bank.get_balance(acc.account_id) == 700.0

    def test_transfer(self):
        bank = Bank()
        acc1 = bank.create_account("Alice")
        acc2 = bank.create_account("Bob")
        bank.deposit(acc1.account_id, 1000)
        bank.transfer(acc1.account_id, acc2.account_id, 400)
        assert bank.get_balance(acc1.account_id) == 600.0
        assert bank.get_balance(acc2.account_id) == 400.0

    def test_transfer_insufficient_funds(self):
        bank = Bank()
        acc1 = bank.create_account("Alice")
        acc2 = bank.create_account("Bob")
        bank.deposit(acc1.account_id, 100)
        with pytest.raises(InsufficientFundsError):
            bank.transfer(acc1.account_id, acc2.account_id, 500)
        assert bank.get_balance(acc2.account_id) == 0.0

    def test_total_assets(self):
        bank = Bank()
        acc1 = bank.create_account("Alice")
        acc2 = bank.create_account("Bob")
        bank.deposit(acc1.account_id, 500)
        bank.deposit(acc2.account_id, 300)
        assert bank.total_assets() == 800.0

    def test_create_savings_with_interest_rate(self):
        bank = Bank()
        acc = bank.create_account("Alice", "savings", interest_rate=0.1)
        assert acc.interest_rate == 0.1
