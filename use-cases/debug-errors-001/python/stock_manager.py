# stock_manager.py
def print_inventory_report(items):
    print("===== INVENTORY REPORT =====")
    # Number of items starting from 1 for user friendly display

    for i, item in enumerate(items, start=1): 
        print(f"Item {i}: {item['name']} - Quantity: {item['quantity']}")
    print("============================")

def main():
    items = [
        {"name": "Laptop", "quantity": 15},
        {"name": "Mouse", "quantity": 30},
        {"name": "Keyboard", "quantity": 25}
    ]
    print_inventory_report(items)

if __name__ == "__main__":
    main()
