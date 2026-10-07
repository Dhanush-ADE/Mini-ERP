MiniERP — Business Management System

A simple command-line Enterprise Resource Planning (ERP) application built with Python and SQLite.

MiniERP demonstrates how core business operations such as employee management, inventory management, and order processing can be organized into a modular software system.

Features

Employee Management
- Add employees
- View all employees
- Search employees
- Update employee information
- Delete employees

Inventory Management
- Add products
- View products
- Search products
- Update product information
- Update stock levels
- Identify low-stock products
- Delete products

Order Management
- Create customer orders
- Validate product availability
- Automatically calculate order totals
- Automatically reduce inventory after an order
- View all orders
- View detailed order information
- Cancel orders
- Restore inventory when an order is cancelled

Technologies Used

- Python 3
- SQLite
- SQL
- Object-Oriented Programming
- Git & GitHub

Project Structure

text
mini-erp/
│
├── main.py
├── database.py
├── employee.py
├── inventory.py
├── orders.py
├── requirements.txt
├── .gitignore
└── README.md


Database Design

The application uses SQLite with four main tables:

- employees — stores employee information
- products — stores inventory information
- orders — stores customer orders
- order_items — stores products belonging to each order

The application uses primary keys and foreign keys to establish relationships between orders, order items, and products.

How to Run

1. Clone the repository

bash
git clone <your-github-repository-url>


2. Open the project directory

bash
cd mini-erp


3. Run the application

bash
python main.py


The database tables are created automatically when the application starts.

Concepts Demonstrated

This project was built to practice and demonstrate:

- Python programming
- Object-oriented programming
- Functions and modular programming
- CRUD operations
- SQL queries
- SQLite database management
- Database relationships
- Input validation
- Transaction handling
- Inventory and order business logic
- Basic software project structure

Future Improvements

Possible future improvements include:

- User authentication and role-based access
- Multiple products per order through the application interface
- Sales and revenue reports
- Graphical or web-based interface
- REST API
- Improved input validation
- Automated unit tests

Author

DHANUSH H

B.Sc. Computer Science — 2027