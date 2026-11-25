# Bianca Martinez
# CST560 Advanced Algorithm Design and Analysis
# Activity 6.2 - Backtracking Module

# Tasks requiring assignment
tasks = [
    "Personify_Defect",
    "Claims_Report",
    "Security_Update",
    "Dashboard_Enhancement"
]

# Available resources
domains = {
    "Personify_Defect": ["US_Developer"],
    "Claims_Report": ["US_Developer", "Data_Analyst"],
    "Security_Update": ["Security_Engineer"],
    "Dashboard_Enhancement": ["Data_Analyst", "Offshore_Developer"]
}

# Workload limits
capacity = {
    "US_Developer": 2,
    "Data_Analyst": 2,
    "Security_Engineer": 1,
    "Offshore_Developer": 1
}


def is_valid(task, resource, assignment):
    current_workload = list(assignment.values()).count(resource)
    return current_workload < capacity[resource]


# Updated MRV heuristic
def remaining_valid_resources(task, assignment):
    count = 0

    for resource in domains[task]:
        current_workload = list(assignment.values()).count(resource)

        if current_workload < capacity[resource]:
            count += 1

    return count


def select_unassigned_task(assignment):
    unassigned = [task for task in tasks if task not in assignment]

    return min(
        unassigned,
        key=lambda task: remaining_valid_resources(task, assignment)
    )


def backtrack(assignment):
    if len(assignment) == len(tasks):
        return assignment

    task = select_unassigned_task(assignment)

    for resource in domains[task]:

        if is_valid(task, resource, assignment):

            assignment[task] = resource

            result = backtrack(assignment)

            if result:
                return result

            del assignment[task]

    return None


if __name__ == "__main__":

    solution = backtrack({})

    print("\nTask Assignment Solution\n")

    if solution:
        for task, resource in solution.items():
            print(f"{task} -> {resource}")
    else:
        print("No valid solution found.")


# Runtime Analysis
# Time Complexity: O(d^n)
# Space Complexity: O(n)

# Design Statement
# This module uses a Constraint Satisfaction Problem (CSP)
# and backtracking algorithm to assign tasks to resources
# while respecting workload limits. I updated the MRV
# heuristic to select tasks based on resources that are
# still available rather than the original domain size.
# I developed and tested the solution using Python and
# Visual Studio Code.