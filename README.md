# Data Analyzer and Transformer

A menu-driven Python program that analyzes and transforms numeric data stored in **1D lists** and **2D lists (matrices)**. Every feature is written as a function, and the same functions work for both kinds of data.

## Features

| Option | What it does |
|---|---|
| 1. Input data | Enter a 1D list or a 2D list (2D data is shown row by row) |
| 2. Display data summary | Total elements, minimum, maximum, sum and average |
| 3. Calculate factorial | Factorial of a number, using recursion |
| 4. Filter data | Keeps only the values greater than a threshold, using `lambda` and `filter()` |
| 5. Sort data | Sorts all values in ascending or descending order |
| 6. Display statistics | Minimum, maximum, sum and average, returned together as multiple values |
| 7. Exit | Closes the program |

## Requirements

- Python 3.6 or newer (the program uses f-strings)
- No external libraries

## How to run

```bash
python main.py
```

## How to use

1. Choose **1** to enter data, then choose **1** for 1D data or **2** for 2D data.
2. Type numbers separated by **commas**, for example `1,2,3`.
   - For 2D data, first enter the number of rows, then type each row on its own line.
3. Choose any option from **2 to 6** to work on the data you entered.
4. Choose **7** to exit.

Options 2, 4, 5 and 6 need data, so always use option 1 first.

## Example run (2D data)

Input:

```
enter your choice: 1
press 1 for 1D data, 2 for 2D data
enter your choice: 2
enter number of rows: 2
enter 1 row data separated by commas: 1,2,3
enter 2 row data separated by commas: 40,5,60
```

Option 2 output:

```
total elements:  6
minimum:  1
maximum:  60
sum:  111
average:  18.5
```

Option 4 with threshold `5`:

```
filtered data:  [40, 60]
```

Option 5 with descending order:

```
[60, 40, 5, 3, 2, 1]
```

## How 1D and 2D data are handled

A 2D list is a list of lists, for example `[[1, 2, 3], [40, 5, 60]]`. Functions like `min()`, `sum()` and `sorted()` need plain numbers, so each function first checks the data with `isinstance()` and flattens a 2D list into one list:

```python
if len(number) > 0 and isinstance(number[0], list):
    m = [x for row in number for x in row]
else:
    m = number
```

After this step, the same code works for both 1D and 2D data.

## Functions

| Function | Purpose |
|---|---|
| `get_1d()` | Reads comma-separated numbers and returns a 1D list |
| `get_2d()` | Reads a number of rows, then each row, and returns a 2D list |
| `flatten(number)` | Prints the summary (total, min, max, sum, average) for 1D or 2D data |
| `fact(n)` | Returns the factorial of `n` using recursion |
| `filt(number, threshold)` | Returns the values greater than the threshold, using `lambda` |
| `srt(number)` | Returns the data sorted in ascending or descending order |
| `stats(number)` | Returns four values: minimum, maximum, sum and average |

## Python concepts used

- Functions with parameters and return values
- Returning and unpacking multiple values
- Recursion (factorial)
- `lambda` with `filter()`
- Built-in functions: `min()`, `max()`, `sum()`, `len()`, `sorted()`
- List comprehension
- `isinstance()` for type checking
- 1D and 2D lists
- `while` loop with an `if / elif / else` menu

## Notes and limitations

- Only whole numbers are supported. Typing text or decimals makes the program stop with an error.
- The filter option asks for a threshold that exists in the data. Otherwise it prints `invalid threshold` and asks again.
- Option 5 sorts a 2D list as one combined list, not row by row.

## Author

Ahmed Bhesania