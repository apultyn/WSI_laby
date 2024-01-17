# README

## Usage

```shell
python3 main.py -map_file -close_bonus -slippery_rate -epochs -learning_rate -discount_factor -epsilon --test_name
```

## Args

- map_file - string - path to map file
- close_bonus - bool - whether use bonus for getting closer to targer
- slippery_rate - float [0, 1] - chance of slipping (doing additional random move)
- epochs - int - amount of training walks (until reaching end or falling into hole)
- learning_rate - float (0, 1) - how new step affects previous qvalue in table
- discount_factor - float (0, 1) - how previous best move from one field affects new qvalue
- epsilon - float (0, 1) - chance of taking random step in training instead of best one
- test_name - optional string - name of the test to create plots and save params