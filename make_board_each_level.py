def make_board_lv3():
    grid_size = 10
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    for i in range(grid_size):
        grid[0][i] = '#'
        grid[grid_size-1][i] = '#'
        grid[i][0] = '#'
        grid[i][grid_size-1] = '#'
    walls = [
        (3, 1), (3, 5),
        (3, 2), (3, 3), (3, 4),
        (4, 5), (5, 5), (6, 5),
        (7, 3), (7, 4), (7, 5)
    ]
    for (row, col) in walls:
        grid[row][col] = '#'
    grid[4][4] = "!"
    for row in range(grid_size):
        for col in range(grid_size):
            if grid[row][col] == ' ':
                grid[row][col] = '.'

    return grid


def make_board_lv2():
    grid_size = 10
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    for i in range(grid_size):
        grid[0][i] = '#'
        grid[grid_size-1][i] = '#'
        grid[i][0] = '#'
        grid[i][grid_size-1] = '#'
    walls = [
        (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
        (2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4), (4, 3),
        (4, 4), (5, 3), (5, 4), (8, 1), (8, 2), (8, 3), (8, 4),
        (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8), (7, 7),
        (6, 7), (6, 8), (6, 9), (5, 8), (5, 7), (4, 7)
    ]
    for (row, col) in walls:
        grid[row][col] = '#'
    grid[4][8] = "!"
    for row in range(grid_size):
        for col in range(grid_size):
            if grid[row][col] == ' ':
                grid[row][col] = '.'

    return grid


def make_board_lv1():
    grid_size = 10
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    for i in range(grid_size):
        grid[0][i] = '#'
        grid[grid_size-1][i] = '#'
        grid[i][0] = '#'
        grid[i][grid_size-1] = '#'
    walls = [
        (1, 8), (3, 7), (4, 7), (5, 7), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (8, 8),
        (7, 8), (8, 7), (7, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 5), (6, 4),
        (7, 5), (7, 4), (6, 1), (6, 2), (6, 3), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
        (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)
    ]
    for (row, col) in walls:
        grid[row][col] = '#'
    grid[7][1] = "!"
    for row in range(grid_size):
        for col in range(grid_size):
            if grid[row][col] == ' ':
                grid[row][col] = '.'

    return grid
