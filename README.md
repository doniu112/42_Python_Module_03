*This project was created as part of the 42 curriculum by dswietoc.*

# Python Module 03 — Data Quest

Python collections through game analytics.

## Description

Game-themed exercises covering command-line arguments, lists, tuples, sets, dictionaries, generators, and comprehensions.

## Requirements

- Python 3.10 or later.
- No third-party packages are needed to run the exercises.
- `flake8` and `mypy` are optional development tools for linting and type checking.

## Setup

```bash
git clone https://github.com/doniu112/42_Python_Module_03.git
cd 42_Python_Module_03
```

The commands below use a Linux, macOS, or WSL shell and `python3`.

## Exercises

| Exercise | File | Purpose |
| --- | --- | --- |
| ex0 | [ft_command_quest.py](ex0/ft_command_quest.py) | Inspect and display command-line arguments. |
| ex1 | [ft_score_analytics.py](ex1/ft_score_analytics.py) | Parse integer scores and calculate summary statistics. |
| ex2 | [ft_coordinate_system.py](ex2/ft_coordinate_system.py) | Read 3D coordinates and calculate Euclidean distances. |
| ex3 | [ft_achievement_tracker.py](ex3/ft_achievement_tracker.py) | Compare randomized achievement sets for four players. |
| ex4 | [ft_inventory_system.py](ex4/ft_inventory_system.py) | Parse an inventory and calculate quantities and percentages. |
| ex5 | [ft_data_stream.py](ex5/ft_data_stream.py) | Generate events lazily and consume a list with a generator. |
| ex6 | [ft_data_alchemist.py](ex6/ft_data_alchemist.py) | Transform and filter player data with comprehensions. |

## Usage

Run these commands from the repository root:

```bash
python3 ex0/ft_command_quest.py hello world 42
python3 ex1/ft_score_analytics.py 1500 2300 invalid 1800
python3 ex2/ft_coordinate_system.py
python3 ex3/ft_achievement_tracker.py
python3 ex4/ft_inventory_system.py sword:1 potion:5 shield:2 sword:3 bad
python3 ex5/ft_data_stream.py
python3 ex6/ft_data_alchemist.py
```

For exercise 2, enter coordinates as `x,y,z`, for example `1,2,3`, followed by a second point such as `4,5,6`. Invalid input prompts another attempt; EOF ends the program cleanly.

## Implementation notes

- Score analysis discards invalid arguments and processes the remaining valid integers.
- Coordinates are stored as tuples. Distances are calculated from the origin and between two points.
- Achievement analysis uses union, intersection, and difference. Randomized results vary between runs.
- Inventory arguments use `item:quantity`. Invalid syntax, duplicate names, and negative quantities are rejected. Ties retain the first item encountered.
- A zero total quantity produces a message instead of dividing by zero.
- Exercise 5 prints 1,000 generated events, then randomly removes and yields all ten events from a separate list.
- Exercise 6 capitalizes all names, separately filters originally capitalized names, assigns random scores, and selects scores above the calculated average.

## Code quality

Create a virtual environment and install the development tools:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install flake8 mypy
```

From the repository root:

```bash
python3 -m flake8 ex*/*.py
python3 -m mypy --strict --explicit-package-bases ex*/*.py
```

The runtime uses only the Python standard library; randomness means the output of exercises 3, 5, and 6 is not fixed.

## Related modules

- [Module 00 — Growing Code](https://github.com/doniu112/42_Python_Module_00)
- [Module 01 — Code Cultivation](https://github.com/doniu112/42_Python_Module_01)
- [Module 02 — Garden Guardian](https://github.com/doniu112/42_Python_Module_02)
- [Module 04 — Data Archivist](https://github.com/doniu112/42_Python_Module_04)

