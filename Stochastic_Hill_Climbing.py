import random

# Bigger tree example
tree = {
    "A": (5, ["B", "C", "E"]),
    "B": (6, ["D", "F"]),
    "C": (4, ["G"]),
    "D": (7, []),
    "F": (9, []),
    "E": (3, ["H", "I"]),
    "G": (5, []),
    "H": (4, []),
    "I": (8, [])
}

current = "A"
path = [current]

while tree[current][1]:  # while current node has children
    children = tree[current][1]
    better_children = []

    # Loop to find all better children
    for child in children:
        if tree[child][0] > tree[current][0]:
            better_children.append(child)
      

    if not better_children:  # no better child → stop
        print(f"No better children for {current} ({tree[current][0]}), stopping.")
        break

    # Randomly choose one of the better children
    current = random.choice(better_children)
    path.append(current)
    print(f"Moved to {current}, path so far: {path}")  # debug

print("Stochastic Hill Climbing Path:", path)
