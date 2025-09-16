tree = {
    "A": (5, ["B", "C","E"]),
    "E": (22, []),
    "B": (6, ["D"]),
    "C": (4, []),
    "D": (8, [])
}

current = "A"
path = [current]

while tree[current][1]:  # while current node has children
    moved = False
    children = tree[current][1]

    # Check children one by one
    for child in children:
        if tree[child][0] > tree[current][0]:  
            # Move immediately when a better child is found
            current = child
            path.append(current)
            moved = True
            break   # stop checking further children
    
    if not moved:  # no better child found → stop
        break

print("Path:", path)
