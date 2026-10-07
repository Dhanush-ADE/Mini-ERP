from database import get_connection


class Product:

    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity


def add_product(product):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO products (name, category, price, quantity)
            VALUES (?, ?, ?, ?)
        """, (
            product.name,
            product.category,
            product.price,
            product.quantity
        ))

        connection.commit()
        print("Product added successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        connection.close()


def get_all_products():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, category, price, quantity
        FROM products
    """)

    products = cursor.fetchall()

    connection.close()

    return products


def search_product(name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, category, price, quantity
        FROM products
        WHERE name LIKE ?
    """, ("%" + name + "%",))

    products = cursor.fetchall()

    connection.close()

    return products


def update_product(product_id, name, category, price, quantity):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE products
        SET name = ?, category = ?, price = ?, quantity = ?
        WHERE id = ?
    """, (
        name,
        category,
        price,
        quantity,
        product_id
    ))

    connection.commit()

    if cursor.rowcount > 0:
        print("Product updated successfully!")
    else:
        print("Product not found.")

    connection.close()


def update_stock(product_id, quantity_change):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT quantity
        FROM products
        WHERE id = ?
    """, (product_id,))

    product = cursor.fetchone()

    if product is None:
        print("Product not found.")
        connection.close()
        return

    current_quantity = product[0]
    new_quantity = current_quantity + quantity_change

    if new_quantity < 0:
        print("Insufficient stock.")
        connection.close()
        return

    cursor.execute("""
        UPDATE products
        SET quantity = ?
        WHERE id = ?
    """, (new_quantity, product_id))

    connection.commit()

    print("Stock updated successfully!")
    print("New stock:", new_quantity)

    connection.close()


def get_low_stock_products(threshold=5):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, category, price, quantity
        FROM products
        WHERE quantity <= ?
        ORDER BY quantity ASC
    """, (threshold,))

    products = cursor.fetchall()

    connection.close()

    return products


def delete_product(product_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM products
        WHERE id = ?
    """, (product_id,))

    connection.commit()

    if cursor.rowcount > 0:
        print("Product deleted successfully!")
    else:
        print("Product not found.")

    connection.close()
