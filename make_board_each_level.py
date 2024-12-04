def add_border_walls(grid, grid_size):
    """
    Add border walls to a grid.

    :param grid: a list representing the grid
    :param grid_size: the size of the grid
    :preconditions: grid is a 2D square list of size
    :preconditions: grid_size is a positive integer
    :postconditions: the last row and the last columns of the grid are filled with the '#'
    :return: the modified grid with border walls added

    >>> grid1 = [[' ' for _ in range(1)] for _ in range(1)]
    >>> add_border_walls(grid1, 1)
    [['#']]
    >>> grid2 = [[' ' for _ in range(3)] for _ in range(3)]
    >>> add_border_walls(grid2, 3)
    [['#', '#', '#'], ['#', ' ', '#'], ['#', '#', '#']]
    """
    for i in range(grid_size):
        grid[0][i] = '#'
        grid[grid_size-1][i] = '#'
        grid[i][0] = '#'
        grid[i][grid_size-1] = '#'
    return grid


def fill_spaces(grid, grid_size):
    """
    Fill empty spaces in a grid with dots.

    :param grid: a list representing the grid
    :param grid_size: the size of the grid
    :preconditions: grid is a 2D square list of size
    :preconditions: grid_size is a positive integer
    :postconditions: the grid is filled (' ') with dots ('.')
    
     >>> grid_1 = [[' ' for _ in range(1)] for _ in range(1)]
     >>> fill_spaces(grid_1, 1)
     >>> grid_1
     [['.']]
     >>> grid_3 = [[' ' for _ in range(3)] for _ in range(3)]
     >>> fill_spaces(grid_3, 3)
     >>> grid_3
     [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    """
    for row in range(grid_size):
        for col in range(grid_size):
            if grid[row][col] == ' ':
                grid[row][col] = '.'


def make_board_lv3():
    """
    Build a 10x10 grid and add specific walls with the '#' and special mark '!'.

    :preconditions: initialize grid size as 10
    :preconditions: initialize the grid as a 2D list of size 10x10
    :postconditions: fill the grid with dots('.'), walls('#'), and a mark('!')
    :return: the grid with dots, walls, and a mark

    >>> grid_mark = make_board_lv3()
    >>> '!' == grid_mark[4][4]
    True
    """
    grid_size = 10
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    add_border_walls(grid, grid_size)
    # for i in range(grid_size):
    #     grid[0][i] = '#'
    #     grid[grid_size-1][i] = '#'
    #     grid[i][0] = '#'
    #     grid[i][grid_size-1] = '#'
    walls = [
        (3, 1), (3, 5),
        (3, 2), (3, 3), (3, 4),
        (4, 5), (5, 5), (6, 5),
        (7, 3), (7, 4), (7, 5)
    ]
    for (row, col) in walls:
        grid[row][col] = '#'
    grid[4][4] = "!"
    fill_spaces(grid, grid_size)
    # for row in range(grid_size):
    #     for col in range(grid_size):
    #         if grid[row][col] == ' ':
    #             grid[row][col] = '.'

    return grid


def make_board_lv2():
    """
    Build a 10x10 grid and add specific walls with the '#' and special mark '!'.

    :preconditions: initialize grid size as 10
    :preconditions: initialize the grid as a 2D list of size 10x10
    :postconditions: fill the grid with dots('.'), walls('#'), and a mark('!')
    :return: the grid with dots, walls, and a mark
    """
    grid_size = 10
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    add_border_walls(grid, grid_size)
    # for i in range(grid_size):
    #     grid[0][i] = '#'
    #     grid[grid_size-1][i] = '#'
    #     grid[i][0] = '#'
    #     grid[i][grid_size-1] = '#'
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
    fill_spaces(grid, grid_size)
    # for row in range(grid_size):
    #     for col in range(grid_size):
    #         if grid[row][col] == ' ':
    #             grid[row][col] = '.'

    return grid


def make_board_lv1():
    """
    Build a 10x10 grid and add specific walls with the '#' and special mark '!'.

    :preconditions: initialize grid size as 10
    :preconditions: initialize the grid as a 2D list of size 10x10
    :postconditions: fill the grid with dots('.'), walls('#'), and a mark('!')
    :return: the grid with dots, walls, and a mark
    """
    grid_size = 10
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    add_border_walls(grid, grid_size)
    # for i in range(grid_size):
    #     grid[0][i] = '#'
    #     grid[grid_size-1][i] = '#'
    #     grid[i][0] = '#'
    #     grid[i][grid_size-1] = '#'
    walls = [
        (1, 8), (3, 7), (4, 7), (5, 7), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (8, 8),
        (7, 8), (8, 7), (7, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (6, 5), (6, 4),
        (7, 5), (7, 4), (6, 1), (6, 2), (6, 3), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
        (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)
    ]
    for (row, col) in walls:
        grid[row][col] = '#'
    grid[7][1] = "!"
    fill_spaces(grid, grid_size)
    # for row in range(grid_size):
    #     for col in range(grid_size):
    #         if grid[row][col] == ' ':
    #             grid[row][col] = '.'

    return grid


def display_grid(grid):
    for row in grid:
        print(' '.join(row))
