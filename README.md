🕹️ Tic-Tac-Toe Game with AI (C)
📌 Project Overview
This project is a command-line Tic-Tac-Toe game written in C that supports both Single Player (Human vs Computer) and Two Player (Human vs Human) modes.
In single-player mode, the computer uses the Minimax algorithm to make optimal moves, making the AI unbeatable.
✨ Features
Single Player mode with AI opponent (Minimax)
Two Player mode (Human vs Human)
Intelligent win, loss, and draw detection
Turn-based gameplay
Input validation and error handling
Clean and modular C code
Handles all edge cases (invalid input, repeated moves, early termination)
🧠 Algorithm Used
Minimax Algorithm
Recursively evaluates all possible future game states
Chooses the optimal move by minimizing the opponent’s chances of winning
Guarantees the best possible outcome for the AI (win or draw)
🛠️ Technologies Used
Language: C
Concepts:
Arrays
Recursion
Conditional logic
Game state evaluation
Algorithmic problem solving
▶️ How to Run
Clone the repository
Compile the program:
gcc tic_tac_toe.c -o tic_tac_toe
Run the executable:
./tic_tac_toe
📚 Learning Outcomes
Strong understanding of recursion and backtracking
Practical use of Minimax in game AI
Improved debugging and control flow handling
Experience in building logic-driven applications in C
📌 Future Enhancements
Difficulty levels (Easy/Medium/Hard)
Graphical User Interface (GUI)
Score tracking system

🏦 Bank Management System (Python + MySQL)
📌 Project Overview
This project is a menu-driven Bank Management System built using Python and MySQL.
It simulates real-world banking operations with persistent database storage using mysql.connector.
✨ Features
Open and manage bank accounts
Cash deposit and withdrawal
Fund transfer between accounts
Account statement generation
Update and delete account details
Loan management
Interest calculation
Account merging
Display total number of accounts
🗄️ Database Design
Uses MySQL relational database
Stores:
Account details
Customer information
Balance and transactions
Ensures data integrity using commits and rollbacks
🛠️ Technologies Used
Language: Python
Database: MySQL
Connector: mysql.connector
Concepts:
SQL (CRUD operations)
Transactions
Modular programming
Input validation
Error handling
▶️ How to Run
Prerequisites
Python 3.x
MySQL Server
mysql-connector-python
Install the connector:
pip install mysql-connector-python
Steps
Create the required database and tables in MySQL
Update database credentials in the Python file
Run the program:
python bank_management_program.py
📚 Learning Outcomes
Python–MySQL integration
Database schema design
SQL query execution
Transaction management
Real-world financial system simulation
📌 Future Enhancements
User authentication system
Transaction history logs
GUI using Tkinter
Encryption for sensitive data
👤 Author
Divyanshu Goyal
