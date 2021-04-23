# Minesweeper

- Implement a class `Minesweeper` (preferably in Python or JavaScript) which accepts a `bombGrid` upon initialization.
	- bombGrid is 2d matrix (0 = safe space, 1 = bomb)

- An instance of this Minesweeper class will have a `gameGrid` property which will essentially
be the game UI within the terminal. It will be the same height and width as the bombGrid
and each cell's value should be something like "_" to represent that it has not been
checked yet.

- An instance will also have a `checkCell` method which accepts 2 arguments `col` and `row`
to represent the coordinates of the cell being checked. Calling this function will:
  1. If the cell being checked corresponds to a bomb in the bombGrid, then end the game
  2. Check all neighboring cells surrounding the checked cell and count the number of them
  that are bombs according to the bombGrid. Replace the value of the cell on the gameGrid
  with that bomb count.
  3. If none of the neighbors are bombs and the gameGrid cell is replaced with '0', then
  all of the neighbors of the checked cell should also be checked (ad infinitum) (see
  `game.checkCell(0, 0)` below).
  4. Print the gameGrid

In order of importance, we score on...
  1. Getting through all the specs
  2. Variable naming / code separation
  3. Playability of the game

Feel free to keep your submission in 1 file.

## Examples
```javascript
bombGrid = [
  [ 0, 0, 1, 0, 0, 1 ],
  [ 0, 0, 1, 1, 1, 0 ],
  [ 0, 0, 1, 1, 0, 0 ],
  [ 0, 0, 1, 0, 0, 0 ],
  [ 0, 1, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 1, 0 ]
]

const game = new Minesweeper(bombGrid)

console.log(game.gameGrid)
/*
  Terminal prints something like this...
	[
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '_' ]
	]
*/

game.checkCell(5, 5)
/*
	[
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '1' ]
	]
*/

game.checkCell(0, 3)
/*
	[
	  [ '_', '_', '_', '4', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '1' ]
	]
*/

game.checkCell(0, 0)
/*
	[
	  [ '0', '2', '_', '4', '_', '_' ],
	  [ '0', '3', '_', '_', '_', '_' ],
	  [ '0', '3', '_', '_', '_', '_' ],
	  [ '1', '3', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '1' ]
	]
*/



game.checkCell(0, 2)
/*
	'Game over you landed on a mine'

	[
	  [ '0', '2', '*', '4', '_', '_' ],
	  [ '0', '3', '_', '_', '_', '_' ],
	  [ '0', '3', '_', '_', '_', '_' ],
	  [ '1', '3', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '_' ],
	  [ '_', '_', '_', '_', '_', '1' ]
	]
*/
```


## Requirements
- Python >= 3.9
- Poetry (or virtualenv with pip)

## Installation
```shell
poetry install
```
or

```shell
python -m pip install -r requirements.txt
```

## How to run?
```shell
python main.py
```


## Why FastAPI?
- Swagger documentation
- Async/await support
- Serialization using Type annotations

## Where is the Docs?
```shell
http://localhost:8000/docs
```
