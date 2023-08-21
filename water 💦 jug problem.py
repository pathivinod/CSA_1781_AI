from collections import deque

class JugState:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

def water_jug_problem(x_capacity, y_capacity, target):
    visited = set()
    initial_state = JugState(0, 0)
    queue = deque([initial_state])

    while queue:
        current_state = queue.popleft()
        
        if current_state in visited:
            continue

        visited.add(current_state)

        if current_state.x == target or current_state.y == target:
            return current_state
        
        # Fill the jugs
        if current_state.x < x_capacity:
            queue.append(JugState(x_capacity, current_state.y))
        if current_state.y < y_capacity:
            queue.append(JugState(current_state.x, y_capacity))
        
        # Empty the jugs
        if current_state.x > 0:
            queue.append(JugState(0, current_state.y))
        if current_state.y > 0:
            queue.append(JugState(current_state.x, 0))
        
        # Pour water from one jug to another
        pour_amount = min(current_state.x, y_capacity - current_state.y)
        queue.append(JugState(current_state.x - pour_amount, current_state.y + pour_amount))
        
        pour_amount = min(x_capacity - current_state.x, current_state.y)
        queue.append(JugState(current_state.x + pour_amount, current_state.y - pour_amount))

    return None

def main():
    x_capacity = 4  # Capacity of the first jug
    y_capacity = 3  # Capacity of the second jug
    target = 2      # Target volume
    
    result = water_jug_problem(x_capacity, y_capacity, target)
    
    if result:
        print(f"Solution found: {result}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
