import copy

roll_number = 24110011615%100

def create_inventory():
    return [
        {
            "item": "Laptop",
            "details": {"price": 50000, "stock": 10, "supplier": {"rating": 4.5}}
        },
        {
            "item": "Phone",
            "details": {"price": 20000, "stock": 25, "supplier": {"rating": 4.2}}
        }
    ]

def apply_discount(data):
    index_to_modify = roll_number % len(data)
    
    for i in range(len(data)):
        if i == index_to_modify:
            data[i]["details"]["price"] *= 0.9
            data[i]["details"]["stock"] -= 5
    return data

def compare_data(original, modified):
    changed = 0
    unchanged = 0

    for i in range(len(original)):
        if original[i] != modified[i]:
            changed += 1
        else:
            unchanged += 1

    return (changed, unchanged)

inventory = create_inventory()

original_backup = copy.deepcopy(inventory)

shallow_copy = inventory.copy()
deep_copy = copy.deepcopy(inventory)

apply_discount(shallow_copy)
apply_discount(deep_copy)

print("Original Inventory:")
print(inventory)

print("\nShallow Copy Result:")
print(shallow_copy)

print("\nDeep Copy Result:")
print(deep_copy)

print("\nDifferences Observed:")

original_vs_backup = compare_data(original_backup, inventory)
print("Tuple Summary (Original vs Backup):", original_vs_backup)

deep_vs_backup = compare_data(original_backup, deep_copy)
print("Tuple Summary (Deep Copy vs Backup):", deep_vs_backup)