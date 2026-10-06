import sys


class ItemError(Exception):
    pass


def create_inventory_system(
    inventory: dict[str, int],
) -> dict[str, int]:
    print("=== Inventory System Creation ===")

    for argument in sys.argv[1:]:
        try:
            key, value = argument.split(":")

            if len(key) == 0:
                raise ItemError(
                    f"Error - invalid parameter '{argument}'"
                )

            if key in inventory:
                raise ItemError(
                    f"Redundant item '{key}' - discarding"
                )

            try:
                quantity = int(value)
            except ValueError:
                print(
                    f"Quantity error for '{key}': "
                    f"invalid literal for int() with base 10: "
                    f"'{value}'"
                )
                continue

            if quantity < 0:
                raise ItemError(
                    f"Quantity error for '{key}': "
                    "value must be non-negative"
                )

            inventory.update({key: quantity})

        except ValueError:
            print(
                f"Error - invalid parameter "
                f"'{argument}'"
            )

        except ItemError as error:
            print(error)

    return inventory


def add_item(inventory: dict[str, int], item: str, quantity: int) -> None:
    try:
        if item in inventory:
            raise ItemError(f"Redundant item '{item}' - discarding")
        if quantity < 0:
            raise ItemError(f"Quantity error for '{item}': "
                             "value must be non-negative - discarding")
        inventory.update({item: quantity})
    except ItemError as e:
        print(e)


def item_representation_in_inventory(inventory: dict[str, int]) -> None:
    total_quantity = sum(inventory.values())

    if total_quantity == 0:
        print("Total quantity is zero. Cannot calculate percentages.")
        return

    for item in inventory:
        quantity = inventory[item]
        percentage = round(quantity / total_quantity * 100, 1)
        print(f"Item {item} represents {percentage}%")


def most_and_least_abundant_items(inventory: dict[str, int]) -> None:
    most_item = ""
    most_quantity = -1

    least_item = ""
    least_quantity = -1

    for item in inventory:
        quantity = inventory[item]

        if most_quantity == -1 or quantity > most_quantity:
            most_item = item
            most_quantity = quantity

        if least_quantity == -1 or quantity < least_quantity:
            least_item = item
            least_quantity = quantity

    print(f"Item most abundant: {most_item} with quantity {most_quantity}")
    print(f"Item least abundant: {least_item} with quantity {least_quantity}")


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    create_inventory_system(inventory=inventory)

    print(f"Got inventory: {inventory}")

    print(f"Item list: {list(inventory.keys())}")

    print(f"Total quantity of the {len(inventory)} items: "
          f"{sum(inventory.values())}")

    item_representation_in_inventory(inventory=inventory)

    if len(inventory) > 0:
        most_and_least_abundant_items(inventory)

    add_item(inventory=inventory, item="magic_item", quantity=1)

    print(f"Updated inventory: {inventory}")


if __name__ == '__main__':
    main()
