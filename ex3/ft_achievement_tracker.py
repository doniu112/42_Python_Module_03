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


def add_achievements(
    players_achievements: dict[str, set[str]],
    available_achievements: list[str],
) -> None:
    for player_achievements in players_achievements.values():
        gen_player_achievements(
            player_achievements,
            available_achievements,)


def distinct_achievements(
    players_achievements: dict[str, set[str]],
) -> set[str]:
    distinct: set[str] = set()

    for player_achievements in players_achievements.values():
        distinct.update(player_achievements)

    return distinct


def common_achievements(
    players_achievements: dict[str, set[str]],
) -> set[str]:
    if not players_achievements:
        return set()

    achievements = list(players_achievements.values())
    common = achievements[0]

    for player_achievements in achievements[1:]:
        common = common.intersection(player_achievements)

    return common


def unique_achievements(
    player_name: str,
    players_achievements: dict[str, set[str]],
) -> set[str]:
    others: set[str] = set()

    for name, achievements in players_achievements.items():
        if name != player_name:
            others = others.union(achievements)

    return players_achievements[player_name].difference(others)


def missing_achievements(
    player_name: str,
    players_achievements: dict[str, set[str]],
    available_achievements: list[str],
) -> set[str]:
    all_achievements = set(available_achievements)

    return all_achievements.difference(
        players_achievements[player_name])


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
