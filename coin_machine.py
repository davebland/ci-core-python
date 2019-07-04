from byotest import *

eur_coins = {
    100 : 20,
    50 : 20,
    20 : 20,
    10 : 20,
    5 : 20,
    2 : 20,
    1 : 20
}

usd_coins = {
    100 : 20,
    50 : 20,
    25 : 1,
    10 : 1,
    5 : 1,
    1 : 3
}

def get_change(amount, denominations = eur_coins):
    change = []
    for coin in denominations:
        while coin <= amount:
            if denominations[coin] > 0:
                change.append(coin)
                denominations[coin] -= 1
                amount -= coin
            else:
                break
    if amount == 0:
        return change
    else:
        raise Exception("Insufficient change available")

# Test coin denominations
test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])

# Test non denomination results
test_are_equal(get_change(3), [2,1])
test_are_equal(get_change(7), [5,2])
test_are_equal(get_change(301), [100,100, 100, 1])
test_are_equal(get_change(393), [100,100, 100, 50, 20, 20, 2, 1])

# Test for specific requested coins with limited number
test_are_equal(get_change(35, usd_coins), [25,10])
try:
    test_are_equal(get_change(9, usd_coins), [5,1,1,1,1])
except Exception as E:
    print(E)
    
print ("All tests pass!")