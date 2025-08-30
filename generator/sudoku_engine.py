from __future__ import annotations
import random
from typing import List, Tuple, Optional

Grid = List[List[int]]
SIZE = 9
DIGITS = list(range(1, 10))

def find_empty(grid: Grid) -> Optional[Tuple[int, int]]:
    for r in range(SIZE):
        for c in range(SIZE):
            if grid[r][c] == 0:
                return r, c
    return None

def valid(grid: Grid, r: int, c: int, v: int) -> bool:
    br, bc = (r // 3) * 3, (c // 3) * 3
    row_ok = all(grid[r][x] != v for x in range(SIZE))
    col_ok = all(grid[y][c] != v for y in range(SIZE))
    box_ok = all(grid[br + y][bc + x] != v for y in range(3) for x in range(3))
    return row_ok and col_ok and box_ok

def solve_count(grid: Grid, limit: int = 2) -> int:
    spot = find_empty(grid)
    if not spot:
        return 1
    r, c = spot
    count = 0
    for v in DIGITS:
        if valid(grid, r, c, v):
            grid[r][c] = v
            count += solve_count(grid, limit)
            grid[r][c] = 0
            if count >= limit:
                break
    return count

def generate_full() -> Grid:
    grid = [[0]*SIZE for _ in range(SIZE)]
    def backtrack() -> bool:
        spot = find_empty(grid)
        if not spot:
            return True
        r, c = spot
        random.shuffle(DIGITS)
        for v in DIGITS:
            if valid(grid, r, c, v):
                grid[r][c] = v
                if backtrack():
                    return True
                grid[r][c] = 0
        return False
    backtrack()
    return [row[:] for row in grid]

def make_puzzle(difficulty: str = "easy"):
    solution = generate_full()
    puzzle = [row[:] for row in solution]
    cells = [(r, c) for r in range(SIZE) for c in range(SIZE)]
    random.shuffle(cells)
    targets = {"easy": 36, "medium": 30, "hard": 24}
    target = targets.get(difficulty, 30)
    for r, c in cells:
        if sum(1 for rr in range(SIZE) for cc in range(SIZE) if puzzle[rr][cc] != 0) <= target:
            break
        val = puzzle[r][c]
        if val == 0:
            continue
        puzzle[r][c] = 0
        temp = [row[:] for row in puzzle]
        if solve_count(temp, limit=2) != 1:
            puzzle[r][c] = val
    return puzzle, solution

def generate(difficulty: str):
    p, s = make_puzzle(difficulty)
    return {"difficulty": difficulty, "grid": p, "solution": s}
