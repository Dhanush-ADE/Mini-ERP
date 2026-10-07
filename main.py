from database import create_tables

from employee import (
    Employee,
    add_employee,
    get_all_employees,
    search_employee,
    update_employee,
    delete_employee
)

from inventory import (
    Product,
    add_product,
    get_all_products,
    search_product,
    update_product,
    update_stock,
    get_low_stock_products,
    delete_product
)

from orders import (
    create_order,
    get_all_orders,
    get_order_details,
    cancel_order
)


def employee_menu():
    while True:
        print("\n========== EMPLOYEE MANAGEMENT ==========")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            department = input("Department: ")
            salary = float(input("Salary: "))

            employee = Employee(
                name,
                email,
                department,
                salary
            )

            add_employee(employee)

        elif choice == "2":
            employees = get_all_employees()

            print("\nEmployees:")
            for employee in employees:
                print(employee)

        elif choice == "3":
            name = input("Enter employee name to search: ")

            employees = search_employee(name)

            for employee in employees:
                print(employee)

        elif choice == "4":
            employee_id = int(input("Employee ID: "))
            name = input("New name: ")
            email = input("New email: ")
            department = input("New department: ")
            salary = float(input("New salary: "))

            update_employee(
                employee_id,
                name,
                email,
                department,
                salary
            )

        elif choice == "5":
            employee_id = int(input("Employee ID: "))
            delete_employee(employee_id)

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


def inventory_menu():
    while True:
        print("\n========== INVENTORY MANAGEMENT ==========")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Update Stock")
        print("6. Low Stock Report")
        print("7. Delete Product")
        print("8. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Product name: ")
            category = input("Category: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))

            product = Product(
                name,
                category,
                price,
                quantity
            )

            add_product(product)

        elif choice == "2":
            products = get_all_products()

            print("\nProducts:")
            for product in products:
                print(product)

        elif choice == "3":
            name = input("Enter product name to search: ")

            products = search_product(name)

            for product in products:
                print(product)

        elif choice == "4":
            product_id = int(input("Product ID: "))
            name = input("New product name: ")
            category = input("New category: ")
            price = float(input("New price: "))
            quantity = int(input("New quantity: "))

            update_product(
                product_id,
                name,
                category,
                price,
                quantity
            )

        elif choice == "5":
            product_id = int(input("Product ID: "))
            quantity_change = int(
                input("Quantity change (+add / -remove): ")
            )

            update_stock(
                product_id,
                quantity_change
            )

        elif choice == "6":
            threshold = int(
                input("Low stock threshold: ")
            )

            products = get_low_stock_products(threshold)

            print("\nLow Stock Products:")

            if not products:
                print("No low-stock products.")

            for product in products:
                print(product)

        elif choice == "7":
            product_id = int(input("Product ID: "))
            delete_product(product_id)

        elif choice == "8":
            break

        else:
            print("Invalid choice.")


def order_menu():
    while True:
        print("\n========== ORDER MANAGEMENT ==========")
        print("1. Create Order")
        print("2. View All Orders")
        print("3. View Order Details")
        print("4. Cancel Order")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            customer_name = input("Customer name: ")
            product_id = int(input("Product ID: "))
            quantity = int(input("Quantity: "))

            create_order(
                customer_name,
                product_id,
                quantity
            )

        elif choice == "2":
            orders = get_all_orders()

            print("\nOrders:")

            for order in orders:
                print(order)

        elif choice == "3":
            order_id = int(input("Order ID: "))

            details = get_order_details(order_id)

            print("\nOrder Details:")

            for detail in details:
                print(detail)

        elif choice == "4":
            order_id = int(input("Order ID: "))

            cancel_order(order_id)

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def main():
    create_tables()

    while True:
        print("\n")
        print("==========================================")
        print("              MINI ERP SYSTEM")
        print("==========================================")
        print("1. Employee Management")
        print("2. Inventory Management")
        print("3. Order Management")
        print("4. Exit")
        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            employee_menu()

        elif choice == "2":
            inventory_menu()

        elif choice == "3":
            order_menu()

        elif choice == "4":
            print("Thank you for using Mini ERP.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
