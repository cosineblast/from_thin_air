"""
=== from thin air challenge

This is a small challenge intended to teach you on how to
adapt existing algorithms into new ones.

The main goal is to exercise the programmer's ability to answer the following question:

"How would I solve this problem if someone had already solved part of it for me"

In this challenge, you will be solving a variety of exercises, which consist of
implementing functions to solve simple tasks, such as sorting lists, or computing
list sums.

However, there's a catch! To pass this challenge, your solutions must use the aid of a
an existing helper function `solve` that can solve this same problem for you:

"""

from thin_air import solve

"""
This function is a bit special, it always behaves like a correct
implementation of the function the exercise currently asks you to implement.
So, for instance, while inside of an exercise function that asks you to implement a function that
sorts a list, `solve` behaves like a function that does exactly that.
 
These exercise functions have documentation comments explaining their intended beheavior,
but their bodies are intially just `pass` (i.e they do nothing, and fail the tests).
Your goal is to fill in the bodies of these functions, to make so that they match the behavior
described by their respective comments.

Here are the main rules:
1. The general implementation of these functions must necessarily call the function `solve`
2. Whenever your implementation calls `solve`, the arguments to `solve` must be
   less than the arguments your function received.

   Don't think too much about this, but in general, if no argument of your call to `solve`
   is greater than what your function received originally, and at least
   one argument is smaller then the original input, everything will work well.
   Examples:
    your_function(3,8) may call solve(3,7)
    your_function(3,8) may call solve(2,8)
    your_function(3,8) may call solve(2,7)
    your_function(3,8) must NOT call solve(4,8) (first argument is greater )
    your_function(3,8) must NOT call solve(3,9) (second argument is greater)
    your_function(3,8) must NOT call solve(3,8) (no argument is smaller    )
   
You can verify your solutions by running `python3 thin_air.py`,
which will load all the exercise functions of the current module (`problems.py`)
and check their correctness.

This challenge develops skills can be really useful for developing algorithms to
solve problems, when combined with other programming techniques.

Give it a try!

Tips:

If you feel tempted to use a builtin python function that does what an exercise
asks you to implement, why not just use `solve`?
"""

# Part 0: numeric exercises

# Note: The following exercise is already completed. It is an example solution.
def pow(b, n):
    """
    Given two non-negative integers, b and n the function `pow` must compute b raised to the n-th
    power. (i.e b ** n).

    Examples:
    >>> pow(10, 0)
    1

    >>> pow(0, 0)
    1

    >>> pow(2, 6)
    64

    >>> pow(10, 4)
    10000

    >>> pow(7, 5)
    16807
    """

    # technically, we could just do
    #   return b ** n
    # and it would match the behavior described above.

    # However, we need to use the existing implementation (the `solve` function) in
    # our solution to this problem in order to respect Rule 1.
    # so, we may feel tempted to just do
    #   return solve(b, n)
    # which would technically work, since `solve` always behaves as intended,
    # but we would then be violating rule 2, which forces
    # us to use the existing solution only with a case smaller than our current one.

    # So, we are going to have to use a different strategy to pass this challenge.
    # The idea of this solution, is to use solve(b, n-1), and then multiply it by b.
    # Since solve(b, n-1) returns b**(n-1), multiplying it by b gives us b**n, giving
    # us a correct solution.

    if n == 0:
        return 1

    return b * solve(b, n - 1)

def largest_digit(n):
    """
    Given a non-negative integer n, finds what is the biggest digit of n
    in its base 10 representation
    Tip: %

    Examples:
    >>> largest_digit(123)
    3

    >>> largest_digit(1997)
    9

    >>> largest_digit(2005)
    5

    >>> largest_digit(0)
    0

    >>> largest_digit(101)
    1
    """
    return 0 if n == 0 else max(n % 10, solve(n // 10))

def count_bits(n):
    """
    Given a non-negative integer n, determinse how many ones there are in the
    binary representation of n.

    Tip: The last bit of a number depends on whether it is even or odd.

    Examples:
    >>> count_bits(10) # 10 == 0B1010
    2

    >>> count_bits(7) # 7 == 0B0111
    3

    >>> count_bits(8) # 8 == 0B1000
    1

    >>> count_bits(3) # 3 == 0B11
    11

    >>> count_bits(0)
    0
    """
    return 0 if n == 0 else n % 2 + solve(n//2)

def reverse_digits(n):
    """
    Given a non-negative integer n, returns a pair containing
    the number of digits of n, and a number with the reversed digits of n.

    Examples:
    >>> reverse_digits(123)
    (3, 321)

    >>> reverse_digits(7)
    (1, 7)

    >>> reverse_digit(1992)
    (4, 2991)

    >>> count_bits(0)
    (0, 0)
    """
    if n == 0:
        return (0, 0)
    
    (count, rev) = solve(n // 10)

    return (count + 1, (n % 10) * (10 ** count) + rev) 
# Part 1: list-related exercises


# The following exercise is already solved for you.
def list_sum(stuff):
    """
    Given a list of integers, the list_sum function computes the sum of the numbers of this list.

    Examples:
    >>> list_sum([])
    0

    >>> list_sum([42])
    42

    >>> list_sum([9, 10])
    19

    >>> list_sum(list(range(10)))
    45
    """
    return 0 if stuff == [] else stuff[0] + solve(stuff[1:])

# The following exercise is already solved for you.
def list_product(stuff):
    """
    Given a list of integers, the list_product function computes the product of the numbers of this list.

    Examples:
    >>> list_product([42])
    42

    >>> list_product([])
    1

    >>> list_product([9, 10])
    90

    >>> list_sum(list(range(1, 6)))
    720
    """
    return 1 if stuff == [] else stuff[0] * solve(stuff[1:])

def list_max(stuff):
    """
    Given a non-empty list of integers, list_max returns its largest element.

    Examples:
    >>> list_max([7])
    7

    >>> list_max([2, 3])
    3

    >>> list_max(list(range(10)))
    10

    >>> list_max([2, 77, 2, 42])
    77
    """
    return stuff[0] if len(stuff) == 1 else max(stuff[0], solve(stuff[1:]))


def list_element(x, stuff):
    """
    Given an integer x and a list of integers stuff, list_element returns True
    if x occurs in stuff, False otherwise.
    
    Examples:
    >>> list_element(3, [])
    False
    
    >>> list_element(3, [1,2])
    False

    >>> list_element(3, [1,2,3,4,5])
    True

    >>> list_element(77, [2, 77, 2, 42])
    True
    """
    return False if len(stuff) == 0 else x == stuff[0] or solve(x, stuff[1:])

def list_frequencies(stuff):
    """
    Given a list of values, list_frequencies returns a dictionary
    that contains the occurence count of each element in the list.
    
    Examples:
    >>> list_frequencies([])
    {}
    
    >>> list_frequencies(['beep'])
    {'beep': 1}

    >>> list_frequencieslement(['beep', 'boop'])
    {'beep': 1, 'boop':  1}

    >>> list_frequencieslement(['beep', 'boop', 'beep'])
    {'beep': 2, 'boop': 1}
    """

    if stuff == []:
        return {}
    else:
        next = solve(stuff[1:])

        if stuff[0] in next:
            next[stuff[0]] += 1
        else:
            next[stuff[0]] = 1

        return next

def list_mul_10(stuff):
    """
    Given a list of integers, returns another list of same size, in which
    each element of the old list is multiplied by 10.
    
    Examples:
    >>> list_mul_10([1, 2, 3])
    [10, 20, 30]
    
    >>> list_mul_10([])
    []

    >>> list_mul_10([4])
    [40]

    >>> list_mul_10([7, 80, 42])
    [70, 800, 420]
    """
    return [] if stuff == [] else [10 * stuff[0]] + solve(stuff[1:])


def list_reverse(stuff):
    """
    Returns the elements of the original list in reverse order.
    
    Examples:
    >>> list_reverse([])
    []
    
    >>> list_reverse([42])
    [42]

    >>> list_reverse([1, 2])
    [2, 1]

    >>> list_reverse([2, 5, 7])
    [7, 5, 2]
    """
    return [] if stuff == [] else solve(stuff[1:]) + [stuff[0]]


def list_remove_odds(stuff):
    """
    Given a list of integers, returns a new list without the odd elements of the original one.
    
    Examples:
    >>> list_remove_odds([2, 3, 4, 5, 6])
    [2, 4, 6]
    
    >>> list_remove_odds([0, 1, 1, 2, 3, 5, 8, 13, 21])
    [0, 2, 8]

    >>> list_remove_odds([])
    []

    >>> list_remove_odds([2])
    [2]

    >>> list_remove_odds([1])
    [1]
    """
    if stuff == []:
        return []
    x = stuff[0]
    return ([x] if x % 2 == 0 else []) + solve(stuff[1:])

def list_replicate(n, x):
    """
    Returns is a list of length n with x as the value of every element.

    Examples:
    >>> list_replicate(5, 'ora)
    ['ora', 'ora', 'ora', 'ora', 'ora']

    >>> list_replicate(3, 7)
    [7, 7, 7]

    >>> list_replicate(0, 'bomb')
    []

    >>> list_replicate(1, 'beep')
    ['beep']
    """
    return [] if n == 0 else [x] + solve(n-1, x)

def list_sort(stuff):
    """
    Given a list of integers, returns a list with the same elements, but
    in ascending order.

    Examples:
    >>> sort([4, 2, 6, 1, 3, 5, 7])
    [1, 2, 3, 4, 5, 6, 7]

    >>> sort([42])
    [42]

    >>> sort([])
    []

    >>> sort([1, 2, 3])
    [1, 2, 3]
    """

    if stuff == []:
        return []

    least = min(stuff)
    least_index = stuff.index(least)

    without_least = stuff[:least_index] + stuff[least_index+1:]

    return [least] + solve(without_least)
