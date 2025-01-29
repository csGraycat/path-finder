from queue import Queue


def draw_path(field_arr, path):
    for node in path[1:-1]:
        field_arr[node[0]][node[1]] = "."
    return field_arr


field = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '@', '#'],
    ['#', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', '#', '#', '#', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', 'x', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
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

nodes = Queue()  # the main queue
nodes.put((player_pos, [player_pos]))  # the queue stores the node for consideration as well as the path towards it
visited = set()

while not nodes.empty():
    current_node, current_path = nodes.get()
    if current_node == exit_pos:
        shortest_path = current_path
        field = draw_path(field, shortest_path)
        break
    row = current_node[0]
    col = current_node[1]
    neighbours = []
    if row - 1 != 0:  # up
        neighbours.append((row - 1, col))
    if row + 1 != len(field) - 1:  # down
        neighbours.append((row + 1, col))
    if col - 1 != 0:  # left
        neighbours.append((row, col - 1))
    if col + 1 != len(field[0]) - 1:  # right
        neighbours.append((row, col + 1))

    for neighbour in neighbours:
        r = neighbour[0]
        c = neighbour[1]
        if field[r][c] != '#' and neighbour not in visited:
            nodes.put((neighbour, current_path + [neighbour]))

    visited.add(current_node)

print("shortest path: ")
for row in field:
    print(' '.join(row))
