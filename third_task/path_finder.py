import random
import queue
import time


# Generating map with given size and land percentage
def generate_map(M, N, land_percentage):
    total_cells = M * N
    land_cells = int(total_cells * land_percentage)
    cell_types = ['water'] * (total_cells - land_cells) + ['land'] * land_cells
    random.shuffle(cell_types)
    map_grid = [cell_types[i:i + N] for i in range(0, total_cells, N)]
    # print('Your map looks like: ')
    # visualize_map(map_grid)
    return map_grid

# printing map in terminal
def visualize_map(map_grid):
    symbol_mapping = {'water': '◻', 'land': '■'}
    for row in map_grid:
        row_str = " ".join([symbol_mapping[cell] for cell in row])
        print(row_str)


# print map in terminal
def visualize_map_with_markers(map_grid, start, end):
    symbol_mapping = {'water': '◻', 'land': '■'}
    for i, row in enumerate(map_grid):
        row_str = ""
        for j, cell in enumerate(row):
            if (i, j) == start:
                row_str += "🛥"
            elif (i, j) == end:
                row_str += "🏁"
            else:
                row_str += symbol_mapping[cell] + " "
        print(row_str)

# Check that cell is on the map
def is_valid_cell(x, y, M, N):
    return 0 <= x < M and 0 <= y < N


# Check cell type
def get_cell_type(map_grid, x, y):
    if is_valid_cell(x, y, len(map_grid), len(map_grid[0])):
        return map_grid[x][y]
    else:
        return None


# Looking for shortest path using BFS
# https://en.wikipedia.org/wiki/Breadth-first_search
def shortest_path(map_grid, start, end):
    M = len(map_grid)
    N = len(map_grid[0])
    visited = [[False] * N for _ in range(M)]
    q = queue.Queue()
    q.put(start)
    visited[start[0]][start[1]] = True

    while not q.empty():
        x, y = q.get()
        if (x, y) == end:
            break

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid_cell(new_x, new_y, M, N) and not visited[new_x][new_y] and map_grid[new_x][new_y] == 'water':
                q.put((new_x, new_y))
                visited[new_x][new_y] = True

    if visited[end[0]][end[1]]:
        return True
    else:
        return False


# User input parameters
M = int(input('Enter number of lines (M): '))
N = int(input('Enter number of columns (N): '))
# land_percentage = float(input('Enter percent of land on your map: ')) / 100
# if land_percentage > 100 or land_percentage < 0:
#     print('The percent is too big or too small, please retry with correct value')
land_percentage = 0.3
start_x = int(input('Enter X coordinate of the start point A(x): '))
start_y = int(input('Enter Y coordinate of the start point A(y): '))
end_x = int(input('Enter X coordinate of the end point B(x): '))
end_y = int(input('Enter Y coordinate of the end point B(y): '))


map_grid = generate_map(M, N, land_percentage)

start = (start_x, start_y)
end = (end_x, end_y)

# print map with start and end point
print('Look, this is your map! Try to find path faster than me?')
visualize_map_with_markers(map_grid, start, end)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('GOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!')


if get_cell_type(map_grid, start_x, start_y) == 'land':
    print('Sorry, start point must be not land Try again -_-')
if is_valid_cell(start_x, start_y, M, N) and is_valid_cell(end_x, end_y, M, N):
    if shortest_path(map_grid, start, end):
        print('Path is exist. I swear. And also I won again')
    else:
        print('Path is not exist  Sorry for disappointing. Try again')
else:
    print('Wrong coordinates of A or B points. You can do better. Try again ^_^')
