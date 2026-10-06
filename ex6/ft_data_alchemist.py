import random


def main() -> None:
    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]

    print("=== Game Data Alchemist ===\n")

    new_players = [player.capitalize() for player in players]

    print(f"Initial list of players:{players}")
    print(f"New list with all names capitalized: {new_players}\n")

    capitalized_only_players = [
        player for player in players if player[0].isupper()
    ]

    print(f"New list of capitalized names only: {capitalized_only_players}\n")

    scores = {player: random.randint(0, 1000) for player in new_players}
    print(f"Score dict: {scores}\n")

    total_score = sum(scores.values())
    average_score = round(total_score / len(scores), 2)
    print(f"Score average is: {average_score}\n")

    above_average_players = {
        player: score for player, score in scores.items()
        if score > average_score
    }
    print(f"Players with above average score: {above_average_players}")


if __name__ == "__main__":
    main()
