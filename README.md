# PyCalc

A simple calculator with a REPL interface built in Python

## Features

- **Basic arithmetic operations**(`+`, `-`, `*`, `/`)
- **Parentheses for grouping**
- **Unary operators**(`+x`, `-x`)
- **Built-in constants**(`pi`, `e`)
- **Built-in math functions**

## Usage

```bash
python main.py
```

### Available Functions

| Function      | Description                 | Example                    |
| ------------- | --------------------------- | -------------------------- |
| `abs(x)`      | Absolute value              | `abs(-5) → 5`              |
| `sqrt(x)`     | Square root                 | `sqrt(16) → 4`             |
| `pow(x, y)`   | Power                       | `pow(2, 8) → 256`          |
| `min(...)`    | Minimum value               | `min(1, 2, 3) → 1`         |
| `max(...)`    | Maximum value               | `max(1, 2, 3) → 3`         |
| `round(x, n)` | Round to `n` decimal places | `round(3.14159, 2) → 3.14` |
| `sin(x)`      | Sine (radians)              | `sin(π/2) → 1`             |
| `cos(x)`      | Cosine (radians)            | `cos(0) → 1`               |
| `tan(x)`      | Tangent (radians)           | `tan(π/4) → 1`             |

### Constants

| Constant | Approximate Value |
| -------- | ----------------- |
| pi       | 3.14159…          |
| e        | 2.71828…          |

### Commands

| Command         | Description              |
| --------------- | ------------------------ |
| `history`       | View calculation history |
| `clear`         | Clear history            |
| `help`          | Show help message        |
| `exit` / `quit` | Exit the calculator      |
