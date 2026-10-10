# 💰 Expense Tracker

A command-line Expense Tracker built with Python to manage daily expenses and store data permanently using JSON.

## ✨ Features

- ➕ **Add Expense:** Record an expense with its category, name, and amount.
- 📋 **View Expenses:** Display all saved expenses.
- 💵 **Total Spending:** Calculate the total amount spent.
- 🔍 **Search Expenses:** Find expenses by name, ignoring letter case.
- 💾 **Persistent Storage:** Save expenses in a JSON file so data remains available after restarting the program.
- ✅ **Input Validation:** Handle invalid menu choices, empty names, and invalid or non-positive amounts.

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON for data storage
- `pathlib` for file handling

## 📁 Project Structure

```text
Expense-Tracker/
│
├── main.py
├── tracker.py
├── Expense.json
└── README.md
```

`Expense.json` is created when expenses are saved, and it stores the expense records.

## 🚀 How to Run

1. Make sure Python 3 is installed.
2. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/Expense-Tracker.git
   ```

3. Open the project directory:

   ```bash
   cd Expense-Tracker
   ```

4. Run the program:

   ```bash
   python main.py
   ```

## 📚 What I Learned

- Creating classes and objects in Python
- Using methods to organize program functionality
- Working with lists and dictionaries
- Reading and writing JSON data
- Handling exceptions and validating user input
- Saving data between program executions
- Using `pathlib` to manage file paths

## 🔮 Future Improvements

- Delete or edit existing expenses
- Filter expenses by category
- Add monthly expense summaries
- Display spending statistics
- Build a graphical user interface

## 👨‍💻 Author

Chewang Tamang

GitHub: ChewangDEV (https://github.com/ChewangDEV)

---

Built as part of my journey to improve my Python programming skills.
