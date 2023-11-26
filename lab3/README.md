# Tic-Tac-Toe

## Playing

### Usage

```shell
python3 play.py -min_max_as_x -depth
```

### Args

* min_max_as_x - bool - whether min-max algorithm plays as x and therefore starts
* depth - int - how many moves ahead min-max should look into

### How to play

When it's your turn, enter your move by entering row and column, seperated by space. Rows and columns are counted from 0.

## Testing

### Usage

```shell
python3 testing.py -iter -min_max_as_x -depth -print_results --test_name
```

### Args

* iter - int - amount of games to play
* min_max_as_x - bool - whether min-max algorithm plays as x and therefore starts
* depth - int - how many moves ahead min-max should look into
* print_results - bool - whether to show the ending board for each game
* test_name - string - if provided, plots and results of current test would be saved