#Michael Hernandez
#IS211 Assignment 1 Part 1
"""IS211 Assigment 1 part 1 - listDivide and tests"""

def listDivide(numbers, divide=2):
    """ This function takes a list of numbers and tests if the elements are divisible
    by the divide argument

    Args:
        numbers (list) A list of integers
        divide (int) The number we will be dividing the list by

    Returns:
        isdivisible (int) Number of elements that are divisible by divide variable

    """
    isdivisible = 0
    for number in numbers:
        if number % divide == 0:
            isdivisible += 1
    return isdivisible

class listDivideException(Exception):
    """Custom exception class for assignment 1"""
    pass

def testListDivide():
    """ Unit tests """
    if listDivide([1, 2, 3, 4, 5]) != 2:
        raise listDivideException
    if listDivide([2, 4, 6, 8, 10]) != 5:
        raise listDivideException
    if listDivide([30, 54, 63, 98, 100], divide=10) != 2:
        raise listDivideException
    if listDivide([]) != 0:
        raise listDivideException
    if listDivide([1, 2, 3, 4, 5], 1) != 5:
        raise listDivideException

if __name__ == '__main__':
    testListDivide()
