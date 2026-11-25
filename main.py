# Bianca Martinez
# CST560 Advanced Algorithm Design and Analysis
# Activity 6.2 Integrated Algorithm System
# Main Orchestration File

from recursion_module import run_recursion_demo
from backtracking_module import backtrack
from dp_module import run_dp_demo
from greedy_module import run_greedy_demo
from graph_module import run_graph_demo


def main():

    print("=" * 60)
    print("IRIS & FRIENDS CARE TRACKER")
    print("INTEGRATED ALGORITHM SYSTEM")
    print("=" * 60)

    print("\nSystem Workflow:")
    print("1. Count cats requiring care")
    print("2. Assign resources")
    print("3. Select priority tasks")
    print("4. Schedule appointments")
    print("5. Find shortest travel routes")

    print("\n" + "=" * 60)
    print("STEP 1: RECURSION")
    print("=" * 60)

    run_recursion_demo()

    print("\n" + "=" * 60)
    print("STEP 2: BACKTRACKING")
    print("=" * 60)

    assignment = backtrack({})

    if assignment:
        for task, resource in assignment.items():
            print(f"{task} -> {resource}")
    else:
        print("No valid solution found.")

    print("\n" + "=" * 60)
    print("STEP 3: DYNAMIC PROGRAMMING")
    print("=" * 60)

    run_dp_demo()

    print("\n" + "=" * 60)
    print("STEP 4: GREEDY ALGORITHM")
    print("=" * 60)

    run_greedy_demo()

    print("\n" + "=" * 60)
    print("STEP 5: GRAPH ALGORITHM")
    print("=" * 60)

    run_graph_demo()

    print("\n" + "=" * 60)
    print("FINAL CARE PLAN COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()