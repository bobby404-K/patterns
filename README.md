# Pattern Programs in Python

A collection of 22 foundational pattern printing algorithms implemented in Python, designed to build loop mastery, nested iteration control, and spatial logic for technical interviews.

---

## Overview

Pattern printing problems serve as a fundamental building block in computer science education. Mastering these exercises develops:
- Precise control over multi-dimensional loops and loop bounds
- Mathematical mapping between indices and printable output
- Spatial visualization essential for matrix operations, dynamic programming tables, and recursion trees
- Time and space complexity awareness in nested iterations

---

## Pattern Catalog

| # | Pattern Name | Difficulty | Folder | Source Code |
|:---:|:---|:---:|:---|:---:|
| 01 | Rectangular Star Pattern | Easy | [01/](01/) | [`one.py`](01/one.py) |
| 02 | Right-Angled Triangle (Stars) | Easy | [02/](02/) | [`two.py`](02/two.py) |
| 03 | Right-Angled Number Pyramid | Easy | [03/](03/) | [`three.py`](03/three.py) |
| 04 | Right-Angled Number Pyramid - II | Easy | [04/](04/) | [`four.py`](04/four.py) |
| 05 | Inverted Right Pyramid (Stars) | Easy | [05/](05/) | [`five.py`](05/five.py) |
| 06 | Inverted Numbered Right Pyramid | Easy | [06/](06/) | [`six.py`](06/six.py) |
| 07 | Star Pyramid | Easy | [07/](07/) | [`seven.py`](07/seven.py) |
| 08 | Inverted Star Pyramid | Easy | [08/](08/) | [`eight.py`](08/eight.py) |
| 09 | Diamond Star Pattern | Medium | [09/](09/) | [`nine.py`](09/nine.py) |
| 10 | Half Diamond Star Pattern | Easy | [10/](10/) | [`ten.py`](10/ten.py) |
| 11 | Binary Number Triangle | Easy | [11/](11/) | [`eleven.py`](11/eleven.py) |
| 12 | Number Crown Pattern | Medium | [12/](12/) | [`twelve.py`](12/twelve.py) |
| 13 | Increasing Number Triangle (Floyd's Triangle) | Easy | [13/](13/) | [`thirteen.py`](13/thirteen.py) |
| 14 | Increasing Letter Triangle | Easy | [14/](14/) | [`fourteen.py`](14/fourteen.py) |
| 15 | Reverse Letter Triangle | Easy | [15/](15/) | [`fifteen.py`](15/fifteen.py) |
| 16 | Alpha-Ramp Pattern | Easy | [16/](16/) | [`sixteen.py`](16/sixteen.py) |
| 17 | Alpha-Hill Pattern | Medium | [17/](17/) | [`seventeen.py`](17/seventeen.py) |
| 18 | Alpha-Triangle Pattern | Medium | [18/](18/) | [`eighteen.py`](18/eighteen.py) |
| 19 | Symmetric Void Pattern | Medium | [19/](19/) | [`nineteen.py`](19/nineteen.py) |
| 20 | Symmetric Butterfly Pattern | Medium | [20/](20/) | [`twenty.py`](20/twenty.py) |
| 21 | Hollow Rectangle Pattern | Medium | [21/](21/) | [`twentyone.py`](21/twentyone.py) |
| 22 | The Number Pattern (Concentric Square) | Hard | [22/](22/) | [`twentytwo.py`](22/twentytwo.py) |

---

## Pattern Solving Framework

Every pattern problem can be decomposed into four standard algorithmic steps:

1. **Row Count Determination (Outer Loop):** Identify the total number of lines to print, establishing the outer loop range (`i` from `0` to `rows - 1`).
2. **Horizontal Offsets / Spacing (Inner Loop 1):** Calculate leading whitespace or central gap formulas as a function of row index `i` and input dimension `N`.
3. **Symbol / Value Mapping (Inner Loop 2):** Determine the number of printed characters, numbers, or alphabetic values per row, along with any increment/decrement rules.
4. **Row Termination:** Print a newline after all row elements are emitted to advance the cursor.

---

## Execution

### Requirements
- Python 3.8 or higher

### Running Solutions
Execute any pattern by navigating to the repository root and running the corresponding script:

```bash
# Pattern 01: Rectangular Star Pattern
python 01/one.py

# Pattern 07: Star Pyramid
python 07/seven.py

# Pattern 12: Number Crown Pattern
python 12/twelve.py

# Pattern 22: Concentric Number Pattern
python 22/twentytwo.py
```

---

## Repository Structure

```
patterns/
├── 01/
│   ├── README.md
│   ├── one.png
│   └── one.py
├── 02/
│   ├── README.md
│   ├── two.png
│   └── two.py
...#all folders==all patterns
├── 22/
│   ├── README.md
│   ├── twentytwo.png
│   └── twentytwo.py
└── README.md
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

