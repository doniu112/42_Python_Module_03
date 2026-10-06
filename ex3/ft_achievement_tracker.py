import random


def gen_player_achievements(
    available_achievements: list[str],
) -> set[str]:
    number_of_achievements = random.randint(
        5,
        10,
    )

    selected_achievements = random.sample(
        available_achievements,
        k=number_of_achievements,
    )

    return set(selected_achievements)


def main() -> None:
    achievements = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Hidden Path Finder",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
    ]

    print("=== Achievement Tracker System ===")

    anna = gen_player_achievements(achievements)
    dominik = gen_player_achievements(achievements)
    weronika = gen_player_achievements(achievements)
    antoni = gen_player_achievements(achievements)

    print(f"\nPlayer Anna: {anna}")
    print(f"Player Dominik: {dominik}")
    print(f"Player Weronika: {weronika}")
    print(f"Player Antoni: {antoni}")

    all_distinct = anna.union(
        dominik,
        weronika,
        antoni,
    )

    print(f"\nAll distinct achievements: {all_distinct}")

    common = anna.intersection(
        dominik,
        weronika,
        antoni,
    )

    print(f"\nCommon achievements: {common}")

    only_anna = anna.difference(
        dominik.union(weronika, antoni)
    )
    only_dominik = dominik.difference(
        anna.union(weronika, antoni)
    )
    only_weronika = weronika.difference(
        anna.union(dominik, antoni)
    )
    only_antoni = antoni.difference(
        anna.union(dominik, weronika)
    )

    print()
    print(f"Only Anna has: {only_anna}")
    print(f"Only Dominik has: {only_dominik}")
    print(f"Only Weronika has: {only_weronika}")
    print(f"Only Antoni has: {only_antoni}")

    all_achievements = set(achievements)

    print()
    print(
        f"Anna is missing: "
        f"{all_achievements.difference(anna)}"
    )
    print(
        f"Dominik is missing: "
        f"{all_achievements.difference(dominik)}"
    )
    print(
        f"Weronika is missing: "
        f"{all_achievements.difference(weronika)}"
    )
    print(
        f"Antoni is missing: "
        f"{all_achievements.difference(antoni)}"
    )


if __name__ == "__main__":
    main()
