# Curcio National Bank (CNB) - Python Banking App

## Overview
Curcio National Bank (CNB) is a **Python-based banking application** that simulates basic banking operations such as deposits, withdrawals, transfers, and viewing transaction history. This project is designed as a **demo for learning purposes**, allowing users to interact with financial transactions in a structured environment.

## Features
- **User Authentication**: Login system with demo accounts.
- **Account Management**:
  - Checking and Savings accounts.
  - View account balances.
- **Transaction Capabilities**:
  - Deposit and withdraw funds.
  - Transfer money between accounts.
  - Transaction history logging.
- **Graphical User Interface (GUI)** built with **Tkinter**.

## How to Run the Application
There are two ways to run the CNB application:

### **Option 1: Run via Python (Recommended for Developers)**
#### **Prerequisites**
- Install **Python 3.10+** (https://www.python.org/downloads/)
- Install required dependencies:
  ```bash
  pip install pillow
  ```

#### **Steps to Run**
1. **Download or clone the repository:**
   ```bash
   git clone https://github.com/yourusername/cnb-python-banking.git
   cd cnb-python-banking
   ```
2. **Run the application**
   ```bash
   python main.py
   ```
   
### **Option 2: Run as a Standalone Executable (.exe)**
If you don’t want to install Python, you can use the standalone executable `.exe` version.

## Demo Accounts
Use the following login credentials to test the application:
| Name              | Username      | Password         |
|------------------|--------------|-----------------|
| Chris Curcio    | curcio_admin | SecureBank123!  |
| Richard Caldwell | richardC89   | CNB$avings321   |
| Sarah West      | sarah_west    | DepositNow789!  |
| Mark Thompson   | markT_CNB     | TrustBank654@   |

## Project Structure
```
├── main.py                  # Entry point for the application
├── auth.py                   # Handles user authentication
├── database.py               # Manages account data storage (JSON-based)
├── transactions.py           # Handles deposits, withdrawals, and transfers
├── ui_login.py               # Login screen UI
├── ui_account.py             # Account overview UI
├── ui_transactions.py        # Deposit, withdrawal, and transfer UI
├── ui_transaction_history.py # Transaction history UI
├── README.md                 # Project documentation (this file)
└── accounts.json             # Account data (auto-generated if missing)
```

## License
This project is for educational purposes and does not include a real banking backend.
