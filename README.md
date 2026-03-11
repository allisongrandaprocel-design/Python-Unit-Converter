# Python-Unit-Converter
A basic unit converter built with Python. It allows users to convert different measurements like distance and temperature through a simple command-line interface.
# 🔄 Unit Converter — Python

A command-line unit converter built with **pure Python** (no external libraries).  
Great first project for a Software Engineering student's GitHub portfolio.

---

## 📋 Available Categories

| # | Category | Example Units |
| 1 | 📏 Length | meter, kilometer, mile, foot, inch |
| 2 | ⚖️ Weight / Mass | kilogram, pound, ounce, ton |
| 3 | 🌡️ Temperature | Celsius, Fahrenheit, Kelvin |
| 4 | 💨 Speed | km/h, m/s, mph, knots |
| 5 | 🟦 Area | m², km², hectare, acre |
| 6 | 🧪 Volume | liter, gallon, fluid ounce, cup |
| 7 | ⏱️ Time | second, minute, hour, day, week, year |

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/unit-converter.git
cd unit-converter

# Run the program (requires Python 3.9+)
python unit_converter.py
```

No external libraries needed. Just Python!

---

## 🖥️ Example Usage

```
══════════════════════════════════════════════════════
         🔄  UNIT CONVERTER  🔄
══════════════════════════════════════════════════════
  [1]  📏 Length
  [2]  ⚖️  Weight / Mass
  [3]  🌡️  Temperature
  ...
  [0]  🚪 Exit

  Choose a category: 3

  → 🌡️  Temperature

  FROM unit (number): 1
  TO   unit (number): 2
  Value in [celsius]: 100

  ✅  100 celsius
      =  212 fahrenheit
```

---

## 🗂️ Project Structure

```
unit-converter/
├── unit_converter.py   # Main program
└── README.md           # This file
```

---

## 🧠 Python Concepts Applied

- **Functions** with type hints (`def convert(value: float, ...) -> float`)
- **Dictionaries** as conversion factor tables
- **Error handling** with `try / except`
- **`while True` loops** for the interactive menu
- **f-strings** for formatted output
- **`__main__` entry point** as Python best practice

---

## 📌 How to Push to GitHub

```bash
git init
git add .
git commit -m "feat: unit converter in Python"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/unit-converter.git
git push -u origin main
```

---

## 💡 Ideas to Expand This Project

- Add **automated tests** with `pytest`
- Build a **graphical interface** with `tkinter`
- Turn it into a **web app** with `Flask` or `FastAPI`
- Add a **history log** of past conversions

---

## 👤 Author

**Your Name** · Software Engineering Student  
GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

---

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/) — free to use and modify.
