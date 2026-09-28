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
            available_achievements,
        )


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

    return set.intersection(*players_achievements.values())


if __name__ == "__main__":
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
        print(f"\nPlayer {player_name}: {player_achievements}")

    distinct = distinct_achievements(players)
    print(f"\nAll distinct achievements: {distinct}")

    common = common_achievements(players)
    print(f"\nCommon achievements: {common}")
