# Bianca Martinez
# CST560 - Activity 6.2 Integrated Algorithm System
# Graph Module
# Iris & Friends Care Tracker
# Algorithm: Dijkstra's Shortest Path

import heapq

# This graph represents pet-care locations around Rio Hondo.
# Each connection includes a sample travel time in minutes.
# I used an adjacency list because it makes the connections
# between locations easy to organize and update.

graph = {
    "Rio Hondo": [
        ("San Benito Animal Hospital", 18),
        ("Harlingen Pets", 30)
    ],
    "San Benito Animal Hospital": [
        ("Rio Hondo", 18),
        ("Pet Care Veterinary Clinic", 20),
        ("Harlingen Pets", 22)
    ],
    "Pet Care Veterinary Clinic": [
        ("San Benito Animal Hospital", 20),
        ("Harlingen Pets", 8)
    ],
    "Harlingen Pets": [
        ("Rio Hondo", 30),
        ("San Benito Animal Hospital", 22),
        ("Pet Care Veterinary Clinic", 8)
    ]
}


def find_shortest_route(graph, start, goal):

    # Check that both locations exist in the graph.
    if start not in graph or goal not in graph:
        return None, []

    # Set every location's distance to infinity.
    distances = {
        location: float("inf")
        for location in graph
    }

    distances[start] = 0

    # Store previous locations for path reconstruction.
    previous = {
        location: None
        for location in graph
    }

    # Priority queue stores the next shortest location.
    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_location = heapq.heappop(
            priority_queue
        )

        if current_distance > distances[current_location]:
            continue

        if current_location == goal:
            break

        # Explore neighboring locations.
        for neighbor, travel_time in graph[current_location]:

            new_distance = current_distance + travel_time

            # Edge relaxation occurs here.
            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                previous[neighbor] = current_location

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    if distances[goal] == float("inf"):
        return None, []

    # Rebuild shortest path.
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return distances[goal], path


def display_shortest_route(graph, start, destination):

    distance, path = find_shortest_route(
        graph,
        start,
        destination
    )

    print(f"\nRoute to {destination}:")

    if path:
        print("Shortest route:", " -> ".join(path))
        print("Total travel time:", distance, "minutes")
    else:
        print("No route found.")


def run_graph_demo():

    print("\n" + "=" * 50)
    print("GRAPH ALGORITHM MODULE")
    print("=" * 50)

    # Test Case 1
    display_shortest_route(
        graph,
        "Rio Hondo",
        "Pet Care Veterinary Clinic"
    )

    # Test Case 2
    display_shortest_route(
        graph,
        "Rio Hondo",
        "Harlingen Pets"
    )

    # Test Case 3
    display_shortest_route(
        graph,
        "Rio Hondo",
        "Rio Hondo"
    )

    # Test Case 4
    display_shortest_route(
        graph,
        "Rio Hondo",
        "Unknown Location"
    )

    # Test Case 5
    disconnected_graph = {
        "Rio Hondo": [],
        "Pet Store": []
    }

    display_shortest_route(
        disconnected_graph,
        "Rio Hondo",
        "Pet Store"
    )

    # Test Case 6
    # Demonstrates edge relaxation based on professor feedback.
    print("\nEdge Relaxation Example")

    relaxation_graph = {
        "Home": [
            ("Clinic", 20),
            ("Shelter", 5)
        ],
        "Shelter": [
            ("Clinic", 10)
        ],
        "Clinic": []
    }

    display_shortest_route(
        relaxation_graph,
        "Home",
        "Clinic"
    )


if __name__ == "__main__":
    run_graph_demo()


# --------------------------------------------------
# WHY I CHOSE DIJKSTRA'S ALGORITHM
# --------------------------------------------------
#
# I chose Dijkstra's algorithm because my graph uses
# weighted connections to represent different travel
# times between locations. It helps find the route
# with the lowest total travel time.


# --------------------------------------------------
# WEIGHTED VS. UNWEIGHTED GRAPHS
# --------------------------------------------------
#
# I used a weighted graph because each connection
# has a different travel time. BFS is useful for
# finding the shortest path in an unweighted graph,
# where every connection has the same cost.
#
# Dijkstra's algorithm is a better choice because
# it considers the different weights when finding
# a route.


# --------------------------------------------------
# RUNTIME ANALYSIS
# --------------------------------------------------
#
# Time Complexity:
# O((V + E) log V)
#
# V represents locations.
# E represents connections.
#
# Space Complexity:
# O(V + E)


# --------------------------------------------------
# DESIGN STATEMENT
# --------------------------------------------------
#
# I
# --------------------------------------------------
# DESIGN STATEMENT
# --------------------------------------------------
#
# I used Dijkstra's algorithm for my Iris & Friends
# Care Tracker project because I wanted to find the
# shortest travel route between pet-care locations
# around Rio Hondo. I created a weighted adjacency
# list and used Python's heapq priority queue to
# compare travel times.
#
# I tested regular routes, the same starting and
# ending location, an unknown destination, a
# disconnected graph, and an example showing how
# the algorithm updates a route when a shorter
# path is found.
#
# These travel times are sample estimates, not
# verified driving times. Real travel times can
# differ by direction because of traffic or
# one-way streets. I can update the edge weights
# and run the algorithm again when conditions change.
#
# I used Python and Visual Studio Code to develop
# and test this project.
