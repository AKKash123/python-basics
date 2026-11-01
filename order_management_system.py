"""
=====================================================================
 ORDER MANAGEMENT SYSTEM (OMS)
=====================================================================
A command-line Order Management System built in Python that uses
JSON file handling for persistent storage.

Features
--------
1.  Add new orders
2.  View all orders (formatted table)
3.  Search orders by Order ID / Customer Name / Product
4.  Update an existing order
5.  Delete an order
6.  Filter orders by status (Pending / Shipped / Delivered / Cancelled)
7.  View sales statistics (total orders, total revenue, avg order value)
8.  Backup orders to a timestamped file
9.  Auto-generates unique Order IDs
10. Input validation and graceful error handling

Data is stored in: orders.json  (same folder as this script)
=====================================================================
"""

import json
import os
import sys
from datetime import datetime

# ---------------------------------------------------------------------
# Configuration- global variable
# ---------------------------------------------------------------------
DATA_FILE = "orders.json"
BACKUP_DIR = "backups"
VALID_STATUSES = ["Pending", "Shipped", "Delivered", "Cancelled"]

# Separator line used in menus / tables
LINE = "=" * 78
THIN_LINE = "-" * 78


# ---------------------------------------------------------------------
# File Handling Layer
# ---------------------------------------------------------------------
def load_orders():
    """Load all orders from the JSON file.
    Returns an empty list if the file does not exist or is corrupt.
    """
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []
            data = json.loads(content)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, IOError) as e:
        print(f"[WARNING] Could not read data file: {e}")
        print("[WARNING] Starting with an empty order list.")
        return []


def save_orders(orders):
    """Save the orders list to the JSON file (pretty-printed)."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(orders, f, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"[ERROR] Could not save data: {e}")
        return False


def generate_order_id(orders):
    """Generate the next sequential Order ID like ORD001, ORD002 ..."""
    if not orders:
        return "ORD001"
    # Extract numeric portion from existing IDs and find the max
    max_num = 0
    for order in orders:
        oid = order.get("order_id", "")
        if oid.startswith("ORD"):
            try:
                num = int(oid[3:])
                if num > max_num:
                    max_num = num
            except ValueError:
                continue
    return f"ORD{max_num + 1:03d}"


# ---------------------------------------------------------------------
# Input Helpers (with validation)
# ---------------------------------------------------------------------
def read_string(prompt, allow_empty=False):
    """Read a non-empty string from the user."""
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print("  -> Input cannot be empty. Please try again.")


def read_float(prompt, min_val=0.0):
    """Read a positive float from the user."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value >= min_val:
                return value
            print(f"  -> Value must be >= {min_val}.")
        except ValueError:
            print("  -> Please enter a valid number.")


def read_int(prompt, min_val=1):
    """Read a positive integer from the user."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value >= min_val:
                return value
            print(f"  -> Value must be >= {min_val}.")
        except ValueError:
            print("  -> Please enter a valid integer.")


def read_status(prompt="Status (Pending/Shipped/Delivered/Cancelled): "):
    """Read a valid order status."""
    while True:
        value = input(prompt).strip().title()
        if value in VALID_STATUSES:
            return value
        print(f"  -> Invalid status. Choose from: {', '.join(VALID_STATUSES)}")


# ---------------------------------------------------------------------
# Core CRUD Operations
# ---------------------------------------------------------------------
def add_order(orders):
    """Create a new order and append it to the list."""
    print("\n" + LINE)
    print(" ADD NEW ORDER".center(78))
    print(LINE)

    order_id = generate_order_id(orders)
    print(f"Generated Order ID : {order_id}")

    customer = read_string("Customer Name      : ")
    product = read_string("Product Name       : ")
    quantity = read_int("Quantity           : ")
    price = read_float("Unit Price (Rs)    : ")
    status = read_status()
    order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    total = quantity * price

    order = {
        "order_id": order_id,
        "customer_name": customer,
        "product": product,
        "quantity": quantity,
        "unit_price": price,
        "total_amount": total,
        "status": status,
        "order_date": order_date,
    }

    orders.append(order)
    if save_orders(orders):
        print(f"\n[SUCCESS] Order {order_id} added successfully!")
        print(f"          Total amount: Rs {total:,.2f}")
    else:
        print("\n[ERROR] Order could not be saved.")


def view_all_orders(orders):
    """Display all orders in a formatted table."""
    print("\n" + LINE)
    print(" ALL ORDERS".center(78))
    print(LINE)

    if not orders:
        print("No orders found. Add an order first.\n")
        return

    print_orders_table(orders)
    print(f"\nTotal orders: {len(orders)}")


def _truncate(text, max_len):
    """Truncate text to max_len, adding '..' if cut."""
    text = str(text)
    if len(text) > max_len:
        return text[: max_len - 2] + ".."
    return text


def print_orders_table(orders):
    """Print a list of orders as a table with clear column separation."""
    header = (f"{'Order ID':<10} {'Customer':<15} {'Product':<15} "
              f"{'Qty':>4} {'Price':>10} {'Total':>11} {'Status':<11}")
    print(THIN_LINE)
    print(header)
    print(THIN_LINE)
    for o in orders:
        customer = _truncate(o.get("customer_name", ""), 15)
        product = _truncate(o.get("product", ""), 15)
        print(f"{o.get('order_id', ''):<10} "
              f"{customer:<15} "
              f"{product:<15} "
              f"{o.get('quantity', 0):>4} "
              f"{o.get('unit_price', 0):>10.2f} "
              f"{o.get('total_amount', 0):>11.2f} "
              f"{o.get('status', ''):<11}")
    print(THIN_LINE)


def search_orders(orders):
    """Search orders by Order ID, Customer Name, or Product."""
    print("\n" + LINE)
    print(" SEARCH ORDERS".center(78))
    print(LINE)
    print("Search by:")
    print("  1. Order ID")
    print("  2. Customer Name")
    print("  3. Product Name")
    choice = read_string("\nEnter choice (1-3): ")

    if choice not in ("1", "2", "3"):
        print("[ERROR] Invalid choice.")
        return

    keyword = read_string("Enter search keyword: ").lower()
    results = []

    for o in orders:
        if choice == "1" and keyword in o.get("order_id", "").lower():
            results.append(o)
        elif choice == "2" and keyword in o.get("customer_name", "").lower():
            results.append(o)
        elif choice == "3" and keyword in o.get("product", "").lower():
            results.append(o)

    if results:
        print(f"\nFound {len(results)} matching order(s):")
        print_orders_table(results)
    else:
        print("\nNo matching orders found.")


def update_order(orders):
    """Update fields of an existing order."""
    print("\n" + LINE)
    print(" UPDATE ORDER".center(78))
    print(LINE)

    if not orders:
        print("No orders to update.\n")
        return

    order_id = read_string("Enter Order ID to update: ").upper()
    order = next((o for o in orders if o.get("order_id", "").upper() == order_id), None)

    if not order:
        print(f"[ERROR] Order {order_id} not found.")
        return

    print("\nCurrent order details:")
    print_orders_table([order])
    print("\nLeave a field blank to keep its current value.\n")

    customer = read_string(f"Customer Name [{order['customer_name']}]: ", allow_empty=True)
    if customer:
        order["customer_name"] = customer

    product = read_string(f"Product Name [{order['product']}]: ", allow_empty=True)
    if product:
        order["product"] = product

    qty_raw = input(f"Quantity [{order['quantity']}]: ").strip()
    if qty_raw:
        try:
            q = int(qty_raw)
            if q >= 1:
                order["quantity"] = q
        except ValueError:
            print("  -> Invalid quantity, keeping old value.")

    price_raw = input(f"Unit Price [{order['unit_price']}]: ").strip()
    if price_raw:
        try:
            p = float(price_raw)
            if p >= 0:
                order["unit_price"] = p
        except ValueError:
            print("  -> Invalid price, keeping old value.")

    status_raw = input(f"Status [{order['status']}] (Pending/Shipped/Delivered/Cancelled): ").strip().title()
    if status_raw in VALID_STATUSES:
        order["status"] = status_raw

    # Recalculate total
    order["total_amount"] = order["quantity"] * order["unit_price"]

    if save_orders(orders):
        print(f"\n[SUCCESS] Order {order_id} updated!")
        print_orders_table([order])


def delete_order(orders):
    """Delete an order by Order ID."""
    print("\n" + LINE)
    print(" DELETE ORDER".center(78))
    print(LINE)

    if not orders:
        print("No orders to delete.\n")
        return

    order_id = read_string("Enter Order ID to delete: ").upper()
    index = next((i for i, o in enumerate(orders) if o.get("order_id", "").upper() == order_id), None)

    if index is None:
        print(f"[ERROR] Order {order_id} not found.")
        return

    print("\nOrder to be deleted:")
    print_orders_table([orders[index]])
    confirm = read_string("\nAre you sure? (yes/no): ").lower()
    if confirm in ("yes", "y"):
        deleted = orders.pop(index)
        if save_orders(orders):
            print(f"\n[SUCCESS] Order {deleted['order_id']} deleted.")
    else:
        print("\nDeletion cancelled.")


def filter_by_status(orders):
    """Filter and display orders by status."""
    print("\n" + LINE)
    print(" FILTER ORDERS BY STATUS".center(78))
    print(LINE)

    if not orders:
        print("No orders available.\n")
        return

    status = read_status()
    results = [o for o in orders if o.get("status", "").title() == status]

    if results:
        print(f"\nOrders with status '{status}':")
        print_orders_table(results)
        print(f"Count: {len(results)}")
    else:
        print(f"\nNo orders found with status '{status}'.")


def view_statistics(orders):
    """Display summary statistics of all orders."""
    print("\n" + LINE)
    print(" SALES STATISTICS".center(78))
    print(LINE)

    if not orders:
        print("No orders to analyze.\n")
        return

    total_orders = len(orders)
    total_revenue = sum(o.get("total_amount", 0) for o in orders)
    avg_order_value = total_revenue / total_orders if total_orders else 0

    # Revenue only from delivered orders
    delivered_revenue = sum(
        o.get("total_amount", 0) for o in orders if o.get("status", "") == "Delivered"
    )

    # Status counts
    status_counts = {s: 0 for s in VALID_STATUSES}
    for o in orders:
        s = o.get("status", "")
        if s in status_counts:
            status_counts[s] += 1

    print(f"Total Orders            : {total_orders}")
    print(f"Total Revenue (all)     : Rs {total_revenue:,.2f}")
    print(f"Delivered Revenue       : Rs {delivered_revenue:,.2f}")
    print(f"Average Order Value     : Rs {avg_order_value:,.2f}")
    print(THIN_LINE)
    print("Status Breakdown:")
    for s in VALID_STATUSES:
        count = status_counts[s]
        pct = (count / total_orders * 100) if total_orders else 0
        print(f"  {s:<12}: {count:>4}  ({pct:5.1f}%)")


def backup_orders(orders):
    """Create a timestamped backup of the current orders file."""
    print("\n" + LINE)
    print(" BACKUP ORDERS".center(78))
    print(LINE)

    if not orders:
        print("No orders to back up.\n")
        return

    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"orders_backup_{timestamp}.json")

    try:
        with open(backup_file, "w", encoding="utf-8") as f:
            json.dump(orders, f, indent=4, ensure_ascii=False)
        print(f"[SUCCESS] Backup created: {backup_file}")
        print(f"          Orders backed up: {len(orders)}")
    except IOError as e:
        print(f"[ERROR] Backup failed: {e}")


# ---------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------
def display_menu():
    """Print the main menu."""
    print("\n" + LINE)
    print(" ORDER MANAGEMENT SYSTEM".center(78))
    print(LINE)
    print("  1. Add New Order")
    print("  2. View All Orders")
    print("  3. Search Orders")
    print("  4. Update Order")
    print("  5. Delete Order")
    print("  6. Filter Orders by Status")
    print("  7. View Sales Statistics")
    print("  8. Backup Orders")
    print("  9. Exit")
    print(LINE)


def main():
    """Main program loop."""
    orders = load_orders()

    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_order(orders)
        elif choice == "2":
            view_all_orders(orders)
        elif choice == "3":
            search_orders(orders)
        elif choice == "4":
            update_order(orders)
        elif choice == "5":
            delete_order(orders)
        elif choice == "6":
            filter_by_status(orders)
        elif choice == "7":
            view_statistics(orders)
        elif choice == "8":
            backup_orders(orders)
        elif choice == "9":
            print("\nThank you for using the Order Management System. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please select 1-9.")

        # Reload from disk so multiple sessions stay in sync
        orders = load_orders()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting gracefully.")
        sys.exit(0)
