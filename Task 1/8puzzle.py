from collections import deque

goal_state = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8)
)

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def get_initial_state():
    initial_state = []
    print("Enter the initial state of the 8-puzzle (3x3 grid, use 0 to represent the empty space):")
    for i in range(3):
        row = input(f"Enter row {i + 1} (3 numbers separated by spaces): ").split()
        row = [int(x) for x in row]
        initial_state.append(tuple(row))
    return tuple(initial_state)

def print_state(state):
    for row in state:
        print("(" + ",".join(map(str, row)) + ")")
    print()

def solve_8_puzzle_bfs(initial_state):
    queue = deque([(initial_state, [])])  # (current_state, path)
    closed_set = set()
    parent_map = {initial_state: None}

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            print("Solution found!")
            print(f"Number of steps: {len(path)}")
            print("Solution path:")
            for step, state in enumerate(path):
                print(f"Step {step}:")
                print_state(state)
            print(f"Step {len(path)}:")
            print_state(goal_state)
            return True

        if current_state in closed_set:
            continue
        closed_set.add(current_state)

        for dx, dy in moves:
            i, j = None, None
            for x in range(3):
                for y in range(3):
                    if current_state[x][y] == 0:
                        i, j = x, y
                        break
                if i is not None:
                    break

            new_i, new_j = i + dx, j + dy
            if is_valid_move(new_i, new_j):
                new_state = [list(row) for row in current_state]
                new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                new_state = tuple(tuple(row) for row in new_state)

                if new_state not in closed_set:
                    queue.append((new_state, path + [current_state]))
                    parent_map[new_state] = current_state

    print("No solution found.")
    return False

# Example usage:
initial_state = get_initial_state()
solve_8_puzzle_bfs(initial_state)