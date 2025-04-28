from account import Account
from user import User
from bankomat import Bankomat
import sys
import io

def test_deposit_positive_amount():
    acc = Account("123", 100)
    acc.deposit(50)
    assert acc.balance == 150
    print("test_deposit_positive_amount OK")

def test_deposit_zero():
    acc = Account("123", 100)
    acc.deposit(0)
    assert acc.balance == 100
    print("test_deposit_zero OK")

def test_deposit_negative_amount():
    acc = Account("123", 100)
    acc.deposit(-50)
    assert acc.balance == 50
    print("test_deposit_negative_amount OK")

def test_multiple_deposits():
    acc = Account("123", 0)
    acc.deposit(100)
    acc.deposit(200)
    assert acc.balance == 300
    print("test_multiple_deposits OK")

def test_withdraw_enough_funds():
    acc = Account("123", 200)
    result = acc.withdraw(150)
    assert result is True
    assert acc.balance == 50
    print("test_withdraw_enough_funds OK")

def test_withdraw_exact_balance():
    acc = Account("123", 100)
    result = acc.withdraw(100)
    assert result is True
    assert acc.balance == 0
    print("test_withdraw_exact_balance OK")

def test_withdraw_insufficient_funds():
    acc = Account("123", 100)
    result = acc.withdraw(150)
    assert result is False
    assert acc.balance == 100
    print("test_withdraw_insufficient_funds OK")

def test_withdraw_zero():
    acc = Account("123", 100)
    result = acc.withdraw(0)
    assert result is True
    assert acc.balance == 100
    print("test_withdraw_zero OK")

def test_check_balance_initial():
    acc = Account("123", 500)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    acc.check_balance()
    sys.stdout = sys.__stdout__
    assert "500" in captured_output.getvalue()
    print("test_check_balance_initial OK")

def test_check_balance_after_deposit():
    acc = Account("123", 100)
    acc.deposit(400)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    acc.check_balance()
    sys.stdout = sys.__stdout__
    assert "500" in captured_output.getvalue()
    print("test_check_balance_after_deposit OK")

def test_check_balance_after_withdraw():
    acc = Account("123", 300)
    acc.withdraw(100)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    acc.check_balance()
    sys.stdout = sys.__stdout__
    assert "200" in captured_output.getvalue()
    print("test_check_balance_after_withdraw OK")

def test_check_balance_zero():
    acc = Account("123", 0)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    acc.check_balance()
    sys.stdout = sys.__stdout__
    assert "0" in captured_output.getvalue()
    print("test_check_balance_zero OK")

# --------- TESTY BANKOMAT ---------

def test_login_correct_pin():
    user = User("Adam", "1234", Account("123"))
    atm = Bankomat()
    atm.log_in(user, "1234")
    assert atm.logged_user == user
    print("test_login_correct_pin OK")

def test_login_incorrect_pin():
    user = User("Ewa", "4321", Account("321"))
    atm = Bankomat()
    atm.log_in(user, "0000")
    assert atm.logged_user is None
    print("test_login_incorrect_pin OK")

def test_login_empty_pin():
    user = User("Karol", "1111", Account("555"))
    atm = Bankomat()
    atm.log_in(user, "")
    assert atm.logged_user is None
    print("test_login_empty_pin OK")

def test_login_none_user():
    atm = Bankomat()
    try:
        atm.log_in(None, "1234")
        print("test_login_none_user FAIL")
    except AttributeError:
        print("test_login_none_user OK")

def test_withdraw_money_logged_in_enough_funds():
    user = User("Anna", "1234", Account("111", 500))
    atm = Bankomat()
    atm.log_in(user, "1234")
    atm.withdraw_money(200)
    assert user.account.balance == 300
    print("test_withdraw_money_logged_in_enough_funds OK")

def test_withdraw_money_logged_in_insufficient_funds():
    user = User("Anna", "1234", Account("111", 100))
    atm = Bankomat()
    atm.log_in(user, "1234")
    atm.withdraw_money(200)
    assert user.account.balance == 100
    print("test_withdraw_money_logged_in_insufficient_funds OK")

def test_withdraw_money_not_logged_in():
    atm = Bankomat()
    captured_output = io.StringIO()
    sys.stdout = captured_output
    atm.withdraw_money(100)
    sys.stdout = sys.__stdout__
    assert "Musisz się zalogować" in captured_output.getvalue()
    print("test_withdraw_money_not_logged_in OK")

def test_withdraw_money_zero_amount():
    user = User("Anna", "1234", Account("111", 500))
    atm = Bankomat()
    atm.log_in(user, "1234")
    atm.withdraw_money(0)
    assert user.account.balance == 500
    print("test_withdraw_money_zero_amount OK")

# --------- MAIN ---------

def main():
    # Wywołanie wszystkich testów
    test_deposit_positive_amount()
    test_deposit_zero()
    test_deposit_negative_amount()
    test_multiple_deposits()
    test_withdraw_enough_funds()
    test_withdraw_exact_balance()
    test_withdraw_insufficient_funds()
    test_withdraw_zero()
    test_check_balance_initial()
    test_check_balance_after_deposit()
    test_check_balance_after_withdraw()
    test_check_balance_zero()
    test_login_correct_pin()
    test_login_incorrect_pin()
    test_login_empty_pin()
    test_login_none_user()
    test_withdraw_money_logged_in_enough_funds()
    test_withdraw_money_logged_in_insufficient_funds()
    test_withdraw_money_not_logged_in()
    test_withdraw_money_zero_amount()

if __name__ == "__main__":
    main()
