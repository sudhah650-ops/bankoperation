from bank import bankOper

def test_deposite():
    totalBalance, updateBalance = bankOper(200000, 30000, 0)

    assert totalBalance == 230000
    assert updateBalance == 230000

def test_withdraw():
    totalBalance, updateBalance = bankOper(100000, 40000, 10000)

    assert totalBalance == 1400000
    assert updateBalance == 1300000

def test_anyamount():
    totalBalance, updateBalance = bankOper(1500000, 0, 15000)

    assert totalBalance == 1600000
    assert updateBalance == 1800000