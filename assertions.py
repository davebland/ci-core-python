def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count
    
def count_upper_case2(message):
    return sum([1 for c in message if c.isupper()])

assert count_upper_case2("") == 0, "Empty string"
assert count_upper_case2("A") == 1, "One upper case"
assert count_upper_case2("AbC") == 2, "Two upper case"
assert count_upper_case2("a") == 0, "One lower case"
assert count_upper_case2("£$%%^") == 0, "Special characters"
assert count_upper_case2("874454") == 0, "Numbers"

print("All the tests passed")