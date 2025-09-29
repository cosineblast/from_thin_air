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


# Part 1: list-related exercises


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
    return 0 if len(stuff) == 0 else stuff[0] + solve(stuff[1:])


def list_max(stuff):
    return stuff[0] if len(stuff) == 1 else max(stuff[0], solve(stuff[1:]))


def list_element(x, stuff):
    return False if len(stuff) == 0 else x == stuff[0] or solve(x, stuff[1:])


def list_multiply_10(stuff):
    pass


def list_remove_odds(stuff):
    pass


def list_reverse(stuff):
    pass


def list_concatenate(stuff):
    pass


def list_flatten(stuff):
    pass


def list_replicate(stuff):
    pass


def list_take_while(stuff):
    pass


def list_drop_while(stuff):
    pass


def list_zip(stuff):
    pass


def list_sort(stuff):
    pass
