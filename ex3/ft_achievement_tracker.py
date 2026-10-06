import random


def gen_player_achievements(
    player_achievements: set[str],
    available_achievements: list[str],
) -> set[str]:
    number_of_achievements = random.randint(
        0,
        len(available_achievements),
    )

    selected_achievements = random.sample(
        available_achievements,
        k=number_of_achievements,
    )

    player_achievements.update(selected_achievements)

    return player_achievements


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

    players: dict[str, set[str]] = {
        "Anna": set(),
        "Dominik": set(),
        "Weronika": set(),
        "Antoni": set(),
    }

    print("=== Achievement Tracker System ===")

    add_achievements(players, achievements)

    for player_name, player_achievements in players.items():
        print(
            f"\nPlayer {player_name}: "
            f"{player_achievements}"
        )

    distinct = distinct_achievements(players)
    print(f"\nAll distinct achievements: {distinct}")

    common = common_achievements(players)
    print(f"\nCommon achievements: {common}")

    print()

    for player_name in players:
        unique = unique_achievements(
            player_name,
            players,
        )
        print(f"Only {player_name} has: {unique}")

    print()

    for player_name in players:
        missing = missing_achievements(
            player_name,
            players,
            achievements,
        )
        print(f"{player_name} is missing: {missing}")

if __name__ == "__main__":
    main()
