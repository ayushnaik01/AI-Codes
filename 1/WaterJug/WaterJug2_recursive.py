# Function to find all possible states for next move
def next_states(state, capacities):
    a, b = state
    ca, cb = capacities
    next_moves = []
    # fill jug a
    next_moves.append((ca, b))
    # fill jug b
    next_moves.append((a, cb))
    # empty jug a
    next_moves.append((0, b))
    # empty jug b
    next_moves.append((a, 0))
    # pour a to b until b is full or a is empty
    amt = min(a, cb-b)
    next_moves.append((a-amt, b+amt))
    # pour b to a until a is full or b is empty
    amt = min(ca-a, b)
    next_moves.append((a+amt, b-amt))
    return next_moves

# Recursive function to find the solution using BFS
def bfs_water_jug(start, goal, capacities, visited):
    if start == goal:
        print(start)
        return True
    q = []
    q.append(start)
    visited.add(start)
    while q:
        curr_state = q.pop(0)
        print(curr_state)
        for next_state in next_states(curr_state, capacities):
            if next_state not in visited:
                q.append(next_state)
                visited.add(next_state)
                if next_state == goal:
                    print(next_state)
                    print("Solution found!")
                    return True
    return False

# Taking input from the user
capacities = tuple(map(int, input("Enter the capacities of the jugs separated by a space (e.g. 3 5): ").split()))
start_state = tuple(map(int, input("Enter the initial state of the jugs separated by a space (e.g. 0 0): ").split()))
goal_state = tuple(map(int, input("Enter the goal state of the jugs separated by a space (e.g. 4 2): ").split()))

# Finding the solution using BFS
visited = set()
found_solution = bfs_water_jug(start_state, goal_state, capacities, visited)

if not found_solution:
    print("Solution not found!")

