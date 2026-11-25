# Bianca Martinez
# CST560 Advanced Algorithm Design and Analysis
# Activity 6.2 - Dynamic Programming Module
# Iris & Friends Care Tracker

# Each task has a name, time requirement, and priority score.
tasks = [
    {"name": "Feed the cats", "time": 10, "priority": 10},
    {"name": "Clean litter boxes", "time": 15, "priority": 9},
    {"name": "Give scheduled medication", "time": 5, "priority": 10},
    {"name": "Grooming", "time": 10, "priority": 5},
    {"name": "Playtime", "time": 15, "priority": 6}
]

time_limit = 30


# Top-Down Dynamic Programming (Memoization)
def dp_memoized(tasks, time_limit):

    n = len(tasks)
    memo = {}

    def solve(i, remaining_time):

        if i == n or remaining_time == 0:
            return 0

        if (i, remaining_time) in memo:
            return memo[(i, remaining_time)]

        skip = solve(i + 1, remaining_time)

        take = 0

        if tasks[i]["time"] <= remaining_time:
            take = (
                tasks[i]["priority"]
                + solve(i + 1,
                        remaining_time - tasks[i]["time"])
            )

        memo[(i, remaining_time)] = max(skip, take)

        return memo[(i, remaining_time)]

    best_score = solve(0, time_limit)

    selected_tasks = []
    remaining_time = time_limit

    for i in range(n):

        if remaining_time == 0:
            break

        skip = solve(i + 1, remaining_time)

        if tasks[i]["time"] <= remaining_time:

            take = (
                tasks[i]["priority"]
                + solve(i + 1,
                        remaining_time - tasks[i]["time"])
            )

            if take > skip:
                selected_tasks.append(tasks[i]["name"])
                remaining_time -= tasks[i]["time"]

    return best_score, selected_tasks


# Bottom-Up Dynamic Programming (Tabulation)
def dp_tabulated(tasks, time_limit):

    n = len(tasks)

    dp = [
        [0 for _ in range(time_limit + 1)]
        for _ in range(n + 1)
    ]

    for i in range(n - 1, -1, -1):

        for remaining_time in range(time_limit + 1):

            skip = dp[i + 1][remaining_time]

            take = 0

            if tasks[i]["time"] <= remaining_time:

                take = (
                    tasks[i]["priority"]
                    + dp[i + 1][
                        remaining_time - tasks[i]["time"]
                    ]
                )

            dp[i][remaining_time] = max(skip, take)

    best_score = dp[0][time_limit]

    selected_tasks = []
    remaining_time = time_limit

    for i in range(n):

        if remaining_time == 0:
            break

        skip = dp[i + 1][remaining_time]

        if tasks[i]["time"] <= remaining_time:

            take = (
                tasks[i]["priority"]
                + dp[i + 1][
                    remaining_time - tasks[i]["time"]
                ]
            )

            if take > skip:
                selected_tasks.append(tasks[i]["name"])
                remaining_time -= tasks[i]["time"]

    return best_score, selected_tasks


def run_dp_demo():

    print("\n" + "=" * 50)
    print("DYNAMIC PROGRAMMING MODULE")
    print("=" * 50)

    memo_score, memo_tasks = dp_memoized(
        tasks,
        time_limit
    )

    table_score, table_tasks = dp_tabulated(
        tasks,
        time_limit
    )

    print("\nTop-Down (Memoization)")
    print("Best priority score:", memo_score)
    print("Selected tasks:", memo_tasks)

    print("\nBottom-Up (Tabulation)")
    print("Best priority score:", table_score)
    print("Selected tasks:", table_tasks)

    print("\nDo both methods agree?")
    print(memo_score == table_score)

    print("\nTask Selection Comparison")
    print("Memoized Tasks:", memo_tasks)
    print("Tabulated Tasks:", table_tasks)

    print(
        "Do both methods select the same tasks?",
        memo_tasks == table_tasks
    )

    print("\nAdditional Test Case 1 - Zero Time")

    zero_score, zero_tasks = dp_tabulated(
        tasks,
        0
    )

    print("Best priority score:", zero_score)
    print("Selected tasks:", zero_tasks)

    print("\nAdditional Test Case 2 - Limited Time")

    short_score, short_tasks = dp_tabulated(
        tasks,
        2
    )

    print("Best priority score:", short_score)
    print("Selected tasks:", short_tasks)


if __name__ == "__main__":
    run_dp_demo()


# Runtime Analysis
#
# Time Complexity:
# O(n * W)
#
# Space Complexity:
# O(n * W)
#
# n = number of tasks
# W = available time


# Design Statement
#
# This module uses the 0/1 Knapsack problem to
# select cat-care tasks with the highest priority
# while staying within a time limit. I implemented
# both memoization and tabulation approaches and
# verified that they return the same results.
# Additional test cases were added to verify
# behavior when no time or very limited time is
# available. I developed and tested the solution
# using Python and Visual Studio Code.