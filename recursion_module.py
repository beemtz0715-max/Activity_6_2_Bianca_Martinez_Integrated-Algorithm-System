"""
Name: Bianca Martinez
Course: CST560 Advanced Algorithm Design and Analysis
Instructor: Dr. Jamal Alhiyafi
Assignment: Activity 6.2 - Integrated Algorithm System
Module: Recursion Module

Description:
This module demonstrates recursion by counting the number
of cats in a list. The list contains my cats: Cali, Iris,
Jasper, and Raja.

This module represents the first step of the Iris & Friends
Care Tracker system. Before appointments, scheduling, or
routing can occur, the system must first determine how many
cats require care.
"""

# Why recursion is appropriate:
# This problem can be broken into smaller versions of itself.
# Counting all cats is the same as counting one cat and then
# counting the remaining cats.
#
# The same process repeats at each level until the tasks become
# small enough that no further breakdown is needed. Eventually,
# the list becomes empty and the recursion stops.


def count_cats_recursive(cat_list):
    """
    Base Case:
    If the list is empty, return 0 because there are no
    cats left to count.

    Recursive Step:
    Count one cat and then recursively count the remaining
    cats in the list.
    """

    # Base Case
    # When the list is empty, recursion stops.
    # This prevents an infinite loop.
    if len(cat_list) == 0:
        return 0

    # Recursive Case
    # Count the first cat and recursively count the rest.
    # The list becomes smaller with each recursive call,
    # eventually reaching the base case.
    return 1 + count_cats_recursive(cat_list[1:])


def run_recursion_demo():
    """
    Demonstrates and tests the recursion module.
    """

    print("\n" + "=" * 50)
    print("RECURSION MODULE - CAT COUNTING")
    print("=" * 50)

    # Test Case 1: Multiple Cats
    cats1 = ["Cali", "Iris", "Jasper", "Raja"]

    print("\nTest Case 1 - Multiple Cats")
    print("My cats:", cats1)
    print("Total cats:", count_cats_recursive(cats1))

    # Test Case 2: Single Cat
    cats2 = ["Iris"]

    print("\nTest Case 2 - Single Cat")
    print("My cats:", cats2)
    print("Total cats:", count_cats_recursive(cats2))

    # Test Case 3: Empty List
    cats3 = []

    print("\nTest Case 3 - Empty List")
    print("My cats:", cats3)
    print("Total cats:", count_cats_recursive(cats3))

    # Return value used by the integrated system
    return count_cats_recursive(cats1)


if __name__ == "__main__":
    run_recursion_demo()


# ------------------------------------------------------------------
# Runtime Analysis
# ------------------------------------------------------------------
#
# Time Complexity: O(n)
# The function visits each cat exactly once.
#
# Space Complexity: O(n)
# A recursive call is added to the call stack for each cat.
#
# ------------------------------------------------------------------
# Design Statement
# ------------------------------------------------------------------
#
# For this module, I selected a simple cat-counting example
# because it helped me focus on understanding recursion instead
# of complex logic. The function counts one cat at a time and
# then calls itself with the remaining cats in the list.
#
# The base case occurs when the list becomes empty, causing the
# recursion to stop. Each recursive call solves a smaller version
# of the same problem until a final result is reached.
#
# For the final integrated system, this module serves as the
# starting point of the Iris & Friends Care Tracker. The system
# first determines how many cats require care before moving on
# to caregiver assignment, appointment selection, scheduling,
# and route planning.
#
# I tested the function using multiple cats, a single cat, and
# an empty list to verify that the recursion behaves correctly
# under different conditions. I developed and tested the code
# using Python 3 and Visual Studio Code.