from database import get_connection


class Employee:

    def __init__(self, name, email, department, salary):
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary


def add_employee(employee):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO employees (name, email, department, salary)
            VALUES (?, ?, ?, ?)
        """, (
            employee.name,
            employee.email,
            employee.department,
            employee.salary
        ))

        connection.commit()
        print("Employee added successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        connection.close()


def get_all_employees():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email, department, salary
        FROM employees
    """)

    employees = cursor.fetchall()

    connection.close()

    return employees


def search_employee(name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email, department, salary
        FROM employees
        WHERE name LIKE ?
    """, ("%" + name + "%",))

    employees = cursor.fetchall()

    connection.close()

    return employees


def update_employee(employee_id, name, email, department, salary):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE employees
        SET name = ?, email = ?, department = ?, salary = ?
        WHERE id = ?
    """, (
        name,
        email,
        department,
        salary,
        employee_id
    ))

    connection.commit()

    if cursor.rowcount > 0:
        print("Employee updated successfully!")
    else:
        print("Employee not found.")

    connection.close()


def delete_employee(employee_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM employees
        WHERE id = ?
    """, (employee_id,))

    connection.commit()

    if cursor.rowcount > 0:
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")

    connection.close()
