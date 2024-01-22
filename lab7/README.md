# README

## Usage

```shell
python3 BurglarAlarmSystem.py <test_file>
```

## Args

* test_file - plik json zawierający listę testów w formacie:
```json
{
    "name": "False alarm chance",   // nazwa testu
    "variable": ["CallAnswered"],   // jaką zmienną chcemy poznać
    "evidence": {   // co wiemy?
        "Burglary": 0
    },
    "which": 1  // chcemy wiedzieć, czy interesujące nas zdarzenie wystąpi (1), czy nie (0)
}
```