from typing import List
from contextlib import suppress
import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

bomb_grid = []
game_grid = []
is_over = False


@app.post("/bomb-grid")
async def load_bomb_grid(grid: List[List[int]]):
    reset_game()
    bomb_grid.extend(grid)
    grid_size = len(grid)
    game_grid.extend([["_" for _ in range(grid_size)] for _ in range(grid_size)])
    return game_grid


@app.get("/game-grid")
async def get_game_grid():
    return game_grid


@app.post("/check-cell")
async def check_cell(col: int, row: int):
    global is_over
    if is_over:
        raise HTTPException(422, "Game is over.")
    if not bomb_grid:
        raise HTTPException(422, "Bomb grid not loaded yet.")
    if col > len(bomb_grid) or row > len(bomb_grid):
        raise HTTPException(422, "Invalid position")
    if is_bomb(col, row):
        game_grid[col][row] = "*"
        is_over = True
        raise HTTPException(422, "Game over you landed on a mine")

    count_neighbors(col, row)

    return game_grid


def is_bomb(col, row) -> bool:
    with suppress(IndexError):
        return bomb_grid[col][row] == 1


def get_neighbors_positions(col, row):
    return [
        (col - 1, row - 1),
        (col - 1, row),
        (col - 1, row + 1),
        (col, row - 1),
        (col, row + 1),
        (col + 1, row - 1),
        (col + 1, row),
        (col + 1, row + 1),
    ]


def count_neighbors(col, row):
    try:
        if game_grid[col][row] != "_" or col < 0 or row < 0:
            raise IndexError
    except IndexError:
        return
    counter = 0
    for x, y in get_neighbors_positions(col, row):
        if x >= 0 and y >= 0:
            with suppress(IndexError):
                counter += bomb_grid[x][y] == 1
    game_grid[col][row] = counter

    if game_grid[col][row] == 0:
        for col, row in get_neighbors_positions(col, row):
            count_neighbors(col, row)


def reset_game():
    global is_over
    is_over = False
    bomb_grid.clear()
    game_grid.clear()


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
