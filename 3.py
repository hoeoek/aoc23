test_case = r"""467..114..
                ...*......
                ..35..633.
                ......\...
                617*......
                .....+.58.
                ..592.....
                ......755.
                ...$.*....
                .664.598.."""

def create_grid(test_case):
    grid = []
    for line in test_case.split('\n'):
        if line:
            grid.append(list(line))
    return grid

def get_adjacent_cells(cell: tuple, grid):
    x, y = cell
    adjacent_cells = []
    if x > 0:
        adjacent_cells.append((x-1, y))
    if y > 0:
        adjacent_cells.append((x, y-1))
    if x < len(grid[0])-1:
        adjacent_cells.append((x+1, y))
    if y < len(grid)-1: 
        adjacent_cells.append((x, y+1))
    if x > 0 and y > 0:
        adjacent_cells.append((x-1, y-1))
    if x < len(grid[0])-1 and y > 0:
        adjacent_cells.append((x+1, y-1))
    if x > 0 and y < len(grid)-1:
        adjacent_cells.append((x-1, y+1))
    if x < len(grid[0])-1 and y < len(grid)-1:
        adjacent_cells.append((x+1, y+1))
    return adjacent_cells

def find_digit_coords(grid: list) -> list:
    coords = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell.isdigit():
                coords.append((x, y))
    return coords

def check_adjecent_cells_for_symbols(adjacent_cells: list, grid) -> bool:
    for adjacent_cell in adjacent_cells:
        x, y = adjacent_cell
        cell_char = grid[y][x]
        if not cell_char.isdigit() and not cell_char == '.': 
            #print(f"Found symbol {cell_char} at {adjacent_cells}")
            return True
    #print(f"No symbols found at {adjacent_cells}")
    return False

def expand_num(coord, grid):
    x, y = coord
    if not grid[y][x].isdigit():
        print(f"No digit at starting coordinate ({x}, {y})")
        return 0  # Return 0 if the starting coordinate is not a digit

    number = ""

    # Move left to the start of the number
    while x > 0 and grid[y][x-1].isdigit():
        x -= 1

    # Expand the number
    while x < len(grid[0]) and grid[y][x].isdigit():
        number += grid[y][x]
        print(f"Expanding number at ({x}, {y}): {number}")
        x += 1

    return int(number) if number else 0


def process_grid(input_grid: str) -> int:
    tot_sum = 0
    grid = create_grid(input_grid)
    num_coords = find_digit_coords(grid)
    processed = set()

    for num_coord in num_coords:
        if num_coord not in processed:
            adjacent_cells = get_adjacent_cells(num_coord, grid)
            if check_adjecent_cells_for_symbols(adjacent_cells, grid):
                number = expand_num(num_coord, grid)
                tot_sum += number
                x, y = num_coord
                while x >= 0 and y >= 0 and y < len(grid) and x < len(grid[0]) and grid[y][x].isdigit():
                    processed.add((x, y))
                    x += 1
    return tot_sum

#print(process_grid(test_case))
# >>> 4361 (its working!)

with open("input_3.txt", 'r') as f:
    input_grid = f.read()

#print(process_grid(input_grid))

def calculate_gear_ratios(grid: list) -> int:
    total_ratio = 0

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '*':
                print(f"Checking * at ({x}, {y})")
                adjacent_numbers = []
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                        print(f"Checking adjacent cell at ({nx}, {ny}), character: '{grid[ny][nx]}'")
                        if grid[ny][nx].isdigit():
                            num = expand_num((nx, ny), grid)
                            adjacent_numbers.append(num)
                            print(f"Adjacent number at ({nx}, {ny}): {num}")
                if len(adjacent_numbers) == 2:
                    print(f"Gear at ({x}, {y}) with numbers {adjacent_numbers}")
                    total_ratio += adjacent_numbers[0] * adjacent_numbers[1]

    return total_ratio





print(calculate_gear_ratios(create_grid(test_case)))