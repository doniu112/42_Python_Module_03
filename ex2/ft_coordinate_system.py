import math


def distance(
    coordinates_1: tuple[float, float, float],
    coordinates_2: tuple[float, float, float],
) -> float:
    dist = math.sqrt(
        (coordinates_2[0] - coordinates_1[0]) ** 2
        + (coordinates_2[1] - coordinates_1[1]) ** 2
        + (coordinates_2[2] - coordinates_1[2]) ** 2
    )
    return dist


def get_player_pos() -> tuple[float, float, float] | None:
    while True:
        try:
            user_input = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            )
        except EOFError:
            print("\nInput ended.")
            return None

        list_of_coordinates = user_input.split(",")

        if len(list_of_coordinates) != 3:
            print("Invalid syntax. Use format: x,y,z")
            continue

        converted_coordinates: list[float] = []

        try:
            for pos in list_of_coordinates:
                converted_coordinates.append(float(pos))

        except ValueError:
            print(
                f"Error on parameter '{pos}': "
                f"could not convert string to float: '{pos}'")
            continue

        return (
            converted_coordinates[0],
            converted_coordinates[1],
            converted_coordinates[2]
            )


def main() -> None:
    coordinates_center: tuple[float, float, float] = (0.0, 0.0, 0.0)

    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    first_coordinates = get_player_pos()
    if first_coordinates is None:
        return

    print(f"Got a first tuple: {first_coordinates}")
    print(
        f"It includes: X={first_coordinates[0]}, "
        f"Y={first_coordinates[1]}, "
        f"Z={first_coordinates[2]}"
    )
    print(
        "Distance to center: "
        f"{round(distance(coordinates_center, first_coordinates), 4)}"
    )

    print("\nGet a second set of coordinates")
    second_coordinates = get_player_pos()
    if second_coordinates is None:
        return

    print(f"Got a second tuple: {second_coordinates}")

    distance_between = distance(
        first_coordinates,
        second_coordinates,
    )
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(distance_between, 4)}"
    )


if __name__ == "__main__":
    main()
