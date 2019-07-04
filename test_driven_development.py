""" Test Driven Development Example
    David Bland """

# Functions

def is_even(number):
    return number % 2 == 0

def even_number_of_evens(numbers):
    evens = 0
    for number in numbers:
        if is_even(number):
            evens += 1
    if evens > 0 and is_even(evens):
        return True
    else:
        return False

# Tests
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All Tests Pass :)")