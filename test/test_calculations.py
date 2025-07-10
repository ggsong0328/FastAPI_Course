import pytest
from app.calculations import (
    add,
    subtract,
    multiply,
    divide,
    BankAccount,
    InsufficientFunds,
)


@pytest.fixture
def zero_bank_account():
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (5, 3, 8),
        (10, 2, 12),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 100, 200),
    ],
)
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected


@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (5, 3, 2),
        (10, 2, 8),
        (0, 0, 0),
        (-1, 1, -2),
        (100, 100, 0),
    ],
)
def test_subtract(num1, num2, expected):
    assert subtract(num1, num2) == expected


@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (5, 3, 15),
        (10, 2, 20),
        (0, 0, 0),
        (-1, 1, -1),
        (100, 100, 10000),
    ],
)
def test_multiply(num1, num2, expected):
    assert multiply(num1, num2) == expected


@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (5, 3, 1.6666666666666667),
        (10, 2, 5),
        (0, 1, 0),
        (-1, 1, -1),
        (100, 100, 1),
    ],
)
def test_divide(num1, num2, expected):
    assert divide(num1, num2) == expected


def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50.0


def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0.0


def test_bank_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30.0


def test_bank_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70.0


def test_bank_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 2) == 55


@pytest.mark.parametrize(
    "deposit, withdraw, expected",
    [
        (200, 100, 100),
        (50, 10, 40),
        (1000, 500, 500),
    ],
)
def test_bank_transaction(zero_bank_account, deposit, withdraw, expected):
    zero_bank_account.deposit(deposit)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == expected


def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(1000)
