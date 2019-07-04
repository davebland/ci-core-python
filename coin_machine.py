from byotest import *

eur_coins = [100,50,20,10,5,2,1]
usd_coins = [100,50,25,10,5,1]

def get_change(amount, denominations = eur_coins):
    change = []
    for coin in denominations:
        while coin <= amount: 
            change.append(coin)
            amount -= coin
    return change

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

# Test for specific requested coins
test_are_equal(get_change(35, usd_coins), [25,10])

print ("All tests pass!")