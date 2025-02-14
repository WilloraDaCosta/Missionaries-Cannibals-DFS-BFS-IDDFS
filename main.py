from collections import deque

class State:
    def __init__(self, m, c, b):
        self.missionaries = m
        self.cannibals = c
        self.boat = b
        self.parent = None

    def is_valid(self):
        if self.missionaries < 0 or self.missionaries > total_missionaries:
            return False
        if self.cannibals < 0 or self.cannibals > total_cannibals:
            return False
        if (self.missionaries < self.cannibals) and self.missionaries > 0:
            return False
        if (total_missionaries - self.missionaries < total_cannibals - self.cannibals) and total_missionaries - self.missionaries > 0:
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def successors(self):
        children = []
        if self.boat == 0:
            new_state = State(self.missionaries, self.cannibals + 1, 1)
            if new_state.is_valid():
                new_state.parent = self
                children.append(new_state)
            new_state = State(self.missionaries + 1, self.cannibals, 1)
            if new_state.is_valid():
                new_state.parent = self
                children.append(new_state)
            new_state = State(self.missionaries + 1, self.cannibals + 1, 1)
            if new_state.is_valid():
                new_state.parent = self
                children.append(new_state)
            new_state = State(self.missionaries + 2, self.cannibals, 1)
            if new_state.is_valid():
                new_state.parent = self
                children.append(new_state)
            new_state = State(self.missionaries, self.cannibals + 2, 1)
            if new_state.is_valid():
                new_state.parent = self
                children.append(new_state)
        else:
            new_state = State(self.missionaries, self.cannibals - 1, 0)
            if new_state.is_valid():
                new_state.parent = self
                children.append(new_state)
            new_state = State(self.missionaries - 1, self.cannibals, 0)
            if new_state.is_valid():
                new_state.parent = self
                children.append(new_state)
            new_state = State(self.missionaries - 1, self.cannibals - 1, 0)
            if new_state.is_valid():
                new_state.parent = self
                children.append(new_state)
            new_state = State(self.missionaries - 2, self.cannibals, 0)
            if new_state.is_valid():
                new_state.parent = self
                children.append(new_state)
            new_state = State(self.missionaries, self.cannibals - 2, 0)
            if new_state.is_valid():
                new_state.parent = self
                children.append(new_state)
        return children

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

def bfs(initial_state):
    visited = set()
    queue = deque([initial_state])

    while queue:
        state = queue.popleft()
        if state.is_goal():
            return state
        visited.add(state)
        for child in state.successors():
            if child not in visited:
                queue.append(child)

    return None

def dfs(initial_state):
    visited = set()
    stack = [initial_state]

    while stack:
        state = stack.pop()
        if state.is_goal():
            return state
        visited.add(state)
        for child in reversed(state.successors()):
            if child not in visited:
                stack.append(child)

    return None

def iddfs(initial_state):
    depth_limit = 0
    while True:
        result = dls(initial_state, depth_limit)
        if result:
            return result
        depth_limit += 1

def dls(node, depth_limit):
    return recursive_dls(node, depth_limit)

def recursive_dls(node, depth_limit):
    if node.is_goal():
        return node
    elif depth_limit == 0:
        return None
    elif depth_limit > 0:
        cutoff_occurred = False
        for child in node.successors():
            result = recursive_dls(child, depth_limit - 1)
            if result:
                return result
            elif result == None:
                cutoff_occurred = True
        if cutoff_occurred:
            return None

total_missionaries = 3  # Set total number of missionaries
total_cannibals = 3  # Set total number of cannibals

initial_state = State(total_missionaries, total_cannibals, 1)

print("BFS:")
result_bfs = bfs(initial_state)
if result_bfs:
    print("Solution found.")
    print("Steps:")
    steps = []
    while result_bfs:
        steps.append(result_bfs)
        result_bfs = result_bfs.parent
    for step in reversed(steps):
        print(step.missionaries, step.cannibals, step.boat)
else:
    print("No solution found.")

print("\nDFS:")
result_dfs = dfs(initial_state)
if result_dfs:
    print("Solution found.")
    print("Steps:")
    steps = []
    while result_dfs:
        steps.append(result_dfs)
        result_dfs = result_dfs.parent
    for step in reversed(steps):
        print(step.missionaries, step.cannibals, step.boat)
else:
    print("No solution found.")

print("\nIDDFS:")
result_iddfs = iddfs(initial_state)
if result_iddfs:
    print("Solution found.")
    print("Steps:")
    steps = []
    while result_iddfs:
        steps.append(result_iddfs)
        result_iddfs = result_iddfs.parent
    for step in reversed(steps):
        print(step.missionaries, step.cannibals, step.boat)
else:
    print("No solution found.")
