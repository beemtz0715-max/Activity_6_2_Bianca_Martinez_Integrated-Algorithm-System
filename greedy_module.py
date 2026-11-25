# Bianca Martinez
# CST560 Advanced Algorithm Design and Analysis
# Activity 6.2 - Greedy Module
# Iris & Friends Care Tracker


def interval_scheduling(intervals):

    # Sort appointments by finish time
    sorted_intervals = sorted(
        intervals,
        key=lambda x: x[1]
    )

    selected = []
    current_end = None

    for start, end in sorted_intervals:

        if current_end is None or start >= current_end:

            selected.append((start, end))
            current_end = end

    return selected


def run_greedy_demo():

    print("\n" + "=" * 50)
    print("GREEDY ALGORITHM MODULE")
    print("=" * 50)

    # Test Case 1 - Normal Schedule
    appointments = [
        (9, 11),
        (9, 10),
        (10, 12),
        (11, 12),
        (12, 13),
        (9, 13)
    ]

    result = interval_scheduling(appointments)

    print("\nTest Case 1 - Normal Schedule")
    print("Final schedule:", result)
    print("Appointments selected:", len(result))

    # Test Case 2 - Empty Schedule
    result = interval_scheduling([])

    print("\nTest Case 2 - Empty Schedule")
    print("Final schedule:", result)
    print("Appointments selected:", len(result))

    # Test Case 3 - One Appointment
    result = interval_scheduling([
        (10, 11)
    ])

    print("\nTest Case 3 - One Appointment")
    print("Final schedule:", result)
    print("Appointments selected:", len(result))

    # Test Case 4 - Overlapping Appointments
    result = interval_scheduling([
        (9, 12),
        (10, 13),
        (11, 14)
    ])

    print("\nTest Case 4 - Overlapping Appointments")
    print("Final schedule:", result)
    print("Appointments selected:", len(result))

    # Test Case 5 - Greedy Choice Example
    result = interval_scheduling([
        (9, 12),
        (9, 10),
        (10, 11),
        (11, 12)
    ])

    print("\nTest Case 5 - Greedy Choice")
    print("Final schedule:", result)
    print("Appointments selected:", len(result))

    return result


if __name__ == "__main__":
    run_greedy_demo()


# --------------------------------------------------
# Runtime Analysis
# --------------------------------------------------
#
# Time Complexity: O(n log n)
# Sorting appointments is the most expensive step.
#
# Space Complexity: O(n)


# --------------------------------------------------
# Design Statement
# --------------------------------------------------
#
# This module uses a Greedy Algorithm to solve the
# interval scheduling problem. I connected the
# assignment to my Iris & Friends Care Tracker
# project by treating appointments as cat-care
# activities that need to be scheduled without
# conflicts.
#
# The algorithm always selects the appointment
# that finishes first, which leaves the most room
# for future appointments. This demonstrates the
# greedy-choice property and optimal substructure.
#
# I tested normal schedules, empty schedules,
# single appointments, overlapping appointments,
# and a greedy-choice example. I developed and
# tested the solution using Python and Visual
# Studio Code.