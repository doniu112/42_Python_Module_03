import sys

class ItemError(Exception):
    pass

def create_invetrory_system(inventory: dict[str, int]) -> dict[str, int]:
    print("=== Inventory System Creation ===")

    for argument in sys.argv[1:]:
        try:
            key, value = argument.split(":")
            if key in inventory:
                raise ItemError(f"Redundant item '{key}' - discarding")
            if not value.isdigit():
                raise ItemError(f"Quantity error for '{key}': invalid literal for int() with base 10: '{value}' - discarding")
            if int(value) < 0:
                raise ItemError(f"Quantity error for '{key}': value must be non-negative - discarding")
            inventory.update({key: int(value)})
        except ValueError:
            print(f"Error - invalid parameter '{argument}' - discarding")
        except ItemError as e:
            print(e)

    return inventory


def add_item(inventory: dict[str, int], item: str, quantity: int) -> None:
    try:
        if item in inventory:
            raise ItemError(f"Redundant item '{item}' - discarding")
        if quantity < 0:
            raise ItemError(f"Quantity error for '{item}': value must be non-negative - discarding")
        inventory.update({item: quantity})
    except ItemError as e:
        print(e)

def main() -> None:
    print("=== Inventory System Analysis ===")
    
    inventory = {}

    create_invetrory_system(inventory=inventory)

    print(f"Got inventory: {inventory}")

    print(f"Item list: {list(inventory.keys())}")

    print(f"Total quantity of the {len(inventory)} items: {sum(inventory.values())}")

    for item, quantity in inventory.items():
        print(f"Item '{item}' represents {quantity / sum(inventory.values()) * 100:.1f}%")

    add_item(inventory=inventory, item="magic_item", quantity=-1)

    print(f"Updated inventory: {inventory}")


if __name__ == '__main__':
    main()
