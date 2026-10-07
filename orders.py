from database import get_connection


def create_order(customer_name, product_id, quantity):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Step 1: Find the product
        cursor.execute("""
            SELECT name, price, quantity
            FROM products
            WHERE id = ?
        """, (product_id,))

        product = cursor.fetchone()

        if product is None:
            print("Product not found.")
            return

        product_name, price, available_quantity = product

        # Step 2: Check stock
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if quantity > available_quantity:
            print("Insufficient stock.")
            print("Available stock:", available_quantity)
            return

        # Step 3: Calculate total
        total_amount = price * quantity

        # Step 4: Create order
        cursor.execute("""
            INSERT INTO orders (customer_name, total_amount)
            VALUES (?, ?)
        """, (customer_name, total_amount))

        order_id = cursor.lastrowid

        # Step 5: Create order item
        subtotal = price * quantity

        cursor.execute("""
            INSERT INTO order_items
            (order_id, product_id, quantity, price, subtotal)
            VALUES (?, ?, ?, ?, ?)
        """, (
            order_id,
            product_id,
            quantity,
            price,
            subtotal
        ))

        # Step 6: Reduce inventory
        new_quantity = available_quantity - quantity

        cursor.execute("""
            UPDATE products
            SET quantity = ?
            WHERE id = ?
        """, (new_quantity, product_id))

        # Step 7: Save everything
        connection.commit()

        print("\nOrder created successfully!")
        print("--------------------------------")
        print("Order ID:", order_id)
        print("Customer:", customer_name)
        print("Product:", product_name)
        print("Quantity:", quantity)
        print("Price:", price)
        print("Total:", total_amount)
        print("Remaining stock:", new_quantity)
        print("--------------------------------")

    except Exception as e:
        connection.rollback()
        print("Order failed.")
        print("Error:", e)

    finally:
        connection.close()


def get_all_orders():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, customer_name, total_amount, status, created_at
        FROM orders
        ORDER BY id DESC
    """)

    orders = cursor.fetchall()

    connection.close()

    return orders


def get_order_details(order_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            orders.id,
            orders.customer_name,
            products.name,
            order_items.quantity,
            order_items.price,
            order_items.subtotal,
            orders.total_amount,
            orders.status,
            orders.created_at
        FROM orders
        JOIN order_items
            ON orders.id = order_items.order_id
        JOIN products
            ON order_items.product_id = products.id
        WHERE orders.id = ?
    """, (order_id,))

    order = cursor.fetchall()

    connection.close()

    return order


def cancel_order(order_id):
    connection = get_connection()
    cursor = connection.cursor()

    # Find the order
    cursor.execute("""
        SELECT status
        FROM orders
        WHERE id = ?
    """, (order_id,))

    order = cursor.fetchone()

    if order is None:
        print("Order not found.")
        connection.close()
        return

    if order[0] == "CANCELLED":
        print("Order is already cancelled.")
        connection.close()
        return

    # Get product and quantity
    cursor.execute("""
        SELECT product_id, quantity
        FROM order_items
        WHERE order_id = ?
    """, (order_id,))

    items = cursor.fetchall()

    try:
        # Restore inventory
        for product_id, quantity in items:

            cursor.execute("""
                UPDATE products
                SET quantity = quantity + ?
                WHERE id = ?
            """, (quantity, product_id))

        # Update order status
        cursor.execute("""
            UPDATE orders
            SET status = 'CANCELLED'
            WHERE id = ?
        """, (order_id,))

        connection.commit()

        print("Order cancelled successfully.")
        print("Inventory has been restored.")

    except Exception as e:
        connection.rollback()
        print("Cancellation failed.")
        print("Error:", e)

    finally:
        connection.close()
