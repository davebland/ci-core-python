def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)

def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(collection, item):
    assert item not in collection, "{0} does contain {1}".format(collection, item)

def test_between(value, lower, upper):
    assert lower <= value <= upper, "{0} does not fall between {1} and {2}".format(value, lower, upper)

# test_are_equal(1, 2)
# test_not_equal("teststring","teststring")
# test_is_in([1,"wrongteststring",3,4], "teststring")
# test_not_in([1,"teststring",3,4], "teststring")
# test_between(21, 5, 20)