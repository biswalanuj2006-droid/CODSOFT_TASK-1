# 🔐 Random Password Generator

A simple Python program that generates strong random passwords using letters, numbers, and special symbols.

## 📌 Features

- Generate passwords of any length
- Includes:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special symbols (!, @, #, $, etc.)
- Easy to use
- Beginner-friendly Python project

---

## 📂 Project Structure

```
RandomPasswordGenerator/
│
├── password_generator.py
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/RandomPasswordGenerator.git
```

### 2. Open the Project Folder

```bash
cd RandomPasswordGenerator
```

### 3. Run the Program

```bash
python password_generator.py
```

---

## 🖥 Example Output

```text
==============================================

           RANDOM PASSWORD GENERATOR

==============================================

Enter password length: 12

Generated Password : K@8q!zP#4Lm$

Thanks for using the password generator
```

---

## 🛠 Technologies Used

- Python 3
- Random Module
- String Module

---

## 📖 Code Explanation

### Import Required Modules

```python
import random
import string
```

### Character Sets

```python
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
```

### Combine All Characters

```python
all_characters = letters + numbers + symbols
```

### Generate Password

```python
for i in range(length):
    password += random.choice(all_characters)
```

---

## ⚠ Limitations

- Does not guarantee at least one letter, one number, and one symbol.
- Password strength depends on the chosen length.

---

## 🔮 Future Improvements

- Password strength checker
- Copy password to clipboard
- Save generated passwords
- Custom character selection
- GUI version using Tkinter
- Dark-themed UI version

---

## 👨‍💻 Author

ANUJ

---

## 📜 License

This project is open-source and available under the MIT License.
