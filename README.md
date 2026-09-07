<div align="center">

# 🌟 Master Pattern Printing in DSA
### 🚀 The Ultimate 22-Pattern Collection for Coding Interviews & Loop Mastery

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![DSA Warmup](https://img.shields.io/badge/DSA-Pattern%20Mastery-FF6F00?style=for-the-badge&logo=codeforces&logoColor=white)](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)
[![Patterns Count](https://img.shields.io/badge/Completed-22%2F22%20Patterns-2ea44f?style=for-the-badge&logo=checkmarx&logoColor=white)](#-patterns-included)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

<br/>

> **"If you can control nested loops, you can conquer matrices, recursion, backtracking, and dynamic programming."**

</div>

---

## 📖 Why This Repository?

- 🔰 **Beginner-friendly** — no prior DSA experience required
- 🎯 **Striver's A2Z Sheet Compatible** — covers the 22 classic pattern problems from TakeUForward
- 💡 **Detailed Explanations** — each pattern includes **intuition, step-by-step approach, and complexity analysis**
- 🔁 **Loop Mastery** — helps build strong intuition for **nested loops, space calculations, and iteration control**
- 🚀 **Great DSA Warm-up** — ideal practice before diving into arrays, strings, recursion, and 2D matrices

---

## 📋 Patterns Included

| # | Pattern Name | Difficulty | Folder / Documentation | Solution Code |
|:---:|:---|:---:|:---|:---:|
| 01 | Rectangular Star Pattern | Easy | [01-rectangular-star-pattern](01-rectangular-star-pattern/) | [`one.py`](01-rectangular-star-pattern/one.py) |
| 02 | Right-Angled Triangle (Stars) | Easy | [02-right-angled-triangle-stars](02-right-angled-triangle-stars/) | [`two.py`](02-right-angled-triangle-stars/two.py) |
| 03 | Right-Angled Number Pyramid | Easy | [03-right-angled-number-pyramid](03-right-angled-number-pyramid/) | [`three.py`](03-right-angled-number-pyramid/three.py) |
| 04 | Right-Angled Number Pyramid - II | Easy | [04-right-angled-number-pyramid-ii](04-right-angled-number-pyramid-ii/) | [`four.py`](04-right-angled-number-pyramid-ii/four.py) |
| 05 | Inverted Right Pyramid (Stars) | Easy | [05-inverted-right-pyramid](05-inverted-right-pyramid/) | [`five.py`](05-inverted-right-pyramid/five.py) |
| 06 | Inverted Numbered Right Pyramid | Easy | [06-inverted-numbered-right-pyramid](06-inverted-numbered-right-pyramid/) | [`six.py`](06-inverted-numbered-right-pyramid/six.py) |
| 07 | Star Pyramid | Easy | [07-star-pyramid](07-star-pyramid/) | [`seven.py`](07-star-pyramid/seven.py) |
| 08 | Inverted Star Pyramid | Easy | [08-inverted-star-pyramid](08-inverted-star-pyramid/) | [`eight.py`](08-inverted-star-pyramid/eight.py) |
| 09 | Diamond Star Pattern | Medium | [09-diamond-star-pattern](09-diamond-star-pattern/) | [`nine.py`](09-diamond-star-pattern/nine.py) |
| 10 | Half Diamond Star Pattern | Easy | [10-half-diamond-star-pattern](10-half-diamond-star-pattern/) | [`ten.py`](10-half-diamond-star-pattern/ten.py) |
| 11 | Binary Number Triangle | Easy | [11-binary-number-triangle](11-binary-number-triangle/) | [`eleven.py`](11-binary-number-triangle/eleven.py) |
| 12 | Number Crown Pattern | Medium | [12-number-crown-pattern](12-number-crown-pattern/) | [`twelve.py`](12-number-crown-pattern/twelve.py) |
| 13 | Increasing Number Triangle (Floyd's Triangle) | Easy | [13-increasing-number-triangle](13-increasing-number-triangle/) | [`thirteen.py`](13-increasing-number-triangle/thirteen.py) |
| 14 | Increasing Letter Triangle | Easy | [14-increasing-letter-triangle](14-increasing-letter-triangle/) | [`fourteen.py`](14-increasing-letter-triangle/fourteen.py) |
| 15 | Reverse Letter Triangle | Easy | [15-reverse-letter-triangle](15-reverse-letter-triangle/) | [`fifteen.py`](15-reverse-letter-triangle/fifteen.py) |
| 16 | Alpha-Ramp Pattern | Easy | [16-alpha-ramp-pattern](16-alpha-ramp-pattern/) | [`sixteen.py`](16-alpha-ramp-pattern/sixteen.py) |
| 17 | Alpha-Hill Pattern | Medium | [17-alpha-hill-pattern](17-alpha-hill-pattern/) | [`seventeen.py`](17-alpha-hill-pattern/seventeen.py) |
| 18 | Alpha-Triangle Pattern | Medium | [18-alpha-triangle-pattern](18-alpha-triangle-pattern/) | [`eighteen.py`](18-alpha-triangle-pattern/eighteen.py) |
| 19 | Symmetric Void Pattern | Medium | [19-symmetric-void-pattern](19-symmetric-void-pattern/) | [`nineteen.py`](19-symmetric-void-pattern/nineteen.py) |
| 20 | Symmetric Butterfly Pattern | Medium | [20-symmetric-butterfly-pattern](20-symmetric-butterfly-pattern/) | [`twenty.py`](20-symmetric-butterfly-pattern/twenty.py) |
| 21 | Hollow Rectangle / Square Pattern | Medium | [21-hollow-rectangle-pattern](21-hollow-rectangle-pattern/) | [`twentyone.py`](21-hollow-rectangle-pattern/twentyone.py) |
| 22 | The Number Pattern (Concentric Square) | Hard | [22-the-number-pattern](22-the-number-pattern/) | [`twentytwo.py`](22-the-number-pattern/twentytwo.py) |

---

## 🧠 The 4-Step Pattern Solving Blueprint

Every pattern problem can be solved systematically by asking four questions:

1. **Outer Loop (Rows):** How many rows are there?
   - Run outer loop `i` from `0` to `rows - 1` (or `1` to `N`).
2. **Inner Loop 1 (Leading Spaces / Left Section):** Does this row need indentation spaces?
   - Identify formula connecting `i` and `N` (e.g., `N - i - 1`).
3. **Inner Loop 2 (Symbols / Numbers):** What characters or numbers are printed, and how many?
   - Connect count and value to `i` (e.g., `2*i + 1` stars or `j` from `1` to `i`).
4. **Newline:** Move to the next row after the inner loops complete (`print()`).

---

## 🚀 Getting Started

### Clone & Navigate
```bash
# Clone the repository
git clone <your-repo-url>

# Navigate into the project
cd patterns
```

### Run Any Pattern File
```bash
# Example: Run Pattern 01 (Rectangular Star Pattern)
python 01-rectangular-star-pattern/one.py

# Example: Run Pattern 07 (Star Pyramid)
python 07-star-pyramid/seven.py

# Example: Run Pattern 22 (Concentric Number Pattern)
python 22-the-number-pattern/twentytwo.py
```

---

## 🎯 Who Is This For?

- 🎓 Students starting their **DSA / Coding Interview preparation**
- 💻 Beginners mastering **nested loops and iteration control**
- 🔁 Anyone wanting structured daily warmup practice before tackling 2D arrays, recursion, and DP

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add visual diagrams, translations in other languages (C++, Java), or alternative approaches:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/pattern-improvements`)
3. Commit your changes (`git commit -m 'Add C++ solution for patterns'`)
4. Push to the branch (`git push origin feature/pattern-improvements`)
5. Open a Pull Request

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

<div align="center">
⭐ <i>If you found this repository helpful for your DSA journey, please consider giving it a star!</i> ⭐
</div>
