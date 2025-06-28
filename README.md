# 💰 Bank Account Management System (OOP in Python)

This is a Python-based Object-Oriented Programming (OOP) project that simulates a **simple banking system**. It supports different account types, deposit/withdrawal operations, interest calculation, and overdraft handling.

---

## 🚀 Features

- Create **Savings** and **Current** accounts  
- Deposit and withdraw money with validations  
- Calculate interest for savings accounts  
- Handle overdrafts with interest in current accounts  
- Transfer funds between accounts  
- Display account balance and holder information  

---

## 🏦 Class Structure

### `Account` (Base Class)
- **Attributes**: `account_number`, `holder_name`, `balance`
- **Methods**:
  - `deposit(amount)`
  - `withdraw(amount)`
  - `disp_balance()`
  - `transfer(amount, target_account)`

### `Savings_Acc` (Inherits from `Account`)
- **Attributes**: `interest_rate` (default 5%)
- **Method**: 
  - `calculate_interest()`

### `Current_Acc` (Inherits from `Account`)
- **Attributes**: `overdraft_limit`, `overdraft_interest_rate`
- **Methods**:
  - `withdraw(amount)` (supports overdraft)
  - `apply_overdraft_interest_rate()`

---

## 🧪 Example Usage

```python
if __name__ == "__main__":
    acc1 = Savings_Acc("S001", "Vaishnavi", 10000)
    acc2 = Current_Acc("C001", "Nandini", 5000)

    acc1.disp_balance()
    acc1.deposit(5000)

    acc2.withdraw(10000)  # triggers overdraft
    acc2.withdraw(8000)   # should fail

    acc1.transfer(300, acc2)

    acc2.deposit(10000)
```

---

## ✅ Sample Output

```
account Hoder:Vaishnavi | Balance:10000
Rs5000 deposited.New balance:Rs15000.0
10000 withdrawn.Remaining Balance is:-5000
 Overdraft Interest of ₹500.00 applied on ₹5000.
Updated balance after interest: ₹-5500.00
Cannot Withdraw money.Amount exceeded Balance
300 transferred to <__main__.Current_Acc object at 0x...>
Rs10000 deposited to Current Account. New balance: Rs4500.0
```

---

## 💡 How to Run

1. Make sure you have Python installed (Python 3.x)
2. Save the code in a file, e.g., `bank_system.py`
3. Open terminal and run:

```bash
python bank_system.py
```

---

## 📌 Future Enhancements

- Add transaction history tracking  
- Build a user login system  
- Use a database (e.g., SQLite/PostgreSQL) for persistent data  
- Add GUI using Tkinter or a web frontend using Flask/Django  
