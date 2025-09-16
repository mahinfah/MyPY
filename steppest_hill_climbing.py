tree = {
    "A": (3, ["B", "C"]),
    "B": (4, ["D"]),
    "C": (4, []),
    "D": (5, ["E"]),
    "E": (55, ["F"]),
    "F": (3, [])
}

current = "A"
path = [current]

while tree[current][1]:
    moved = False
    children = tree[current][1]

    # Find the best child (highest value among children)
    best_child = None
    best_value = tree[current][0]

    for child in children:
        if tree[child][0] > best_value:
            best_child = child
            best_value = tree[child][0]

    if best_child:  # if we found a better move
        current = best_child
        path.append(current)
        moved = True

    if not moved:
        break  # no better child found → stop

print("Steepest Hill Climbing Path:", path)
