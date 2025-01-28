field = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '@', '#'],
    ['#', '#', '#', '#', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', 'x', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

player_pos = (-1, -1)
exit_pos = (-1, -1)

for row in enumerate(field):
    for cell in enumerate(row[1]):
        if cell[1] == '@':
            player_pos = (row[0], cell[0])  # y, x
            print("player pos:", player_pos)
        if cell[1] == "x" or cell[1] == "X":
            exit_pos = (row[0], cell[0])  # y, x
            print("exit pos:", exit_pos)

for row in field:
    print(' '.join(row))

nodes = [player_pos]  # the main queue
paths = [[player_pos]]  # [[1, 2, 4], [1, 3, 5], ... ]
visited = set()

while exit_pos not in nodes:
    nodes_added = []
    row = nodes[0][0]
    col = nodes[0][1]
    if field[row - 1][col] != '#' and (row - 1, col) not in visited:  # up
        nodes.append((row - 1, col))
        nodes_added.append((row - 1, col))
    if field[row + 1][col] != '#' and (row + 1, col) not in visited:  # down
        nodes.append((row + 1, col))
        nodes_added.append((row + 1, col))
    if field[row][col - 1] != '#' and (row, col - 1) not in visited:  # left
        nodes.append((row, col - 1))
        nodes_added.append((row, col - 1))
    if field[row][col + 1] != '#' and (row, col + 1) not in visited:  # right
        nodes.append((row, col + 1))
        nodes_added.append((row, col + 1))

    for path in paths:
        if nodes[0] == path[-1]:
            if nodes_added:  # extend path only if it's not a dead-end
                if len(nodes_added) > 1:  # handle forks in the path
                    paths.append(path[:])
                path.append(nodes_added.pop(0))

    visited.add(nodes.pop(0))

shortest_path = []
for path in paths:
    if path[-1] == exit_pos:
        shortest_path = path

for node in shortest_path[1:-1]:
    field[node[0]][node[1]] = "."

print("shortest path: ")
for row in field:
    print(' '.join(row))
