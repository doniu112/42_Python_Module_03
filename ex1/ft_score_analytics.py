import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores: list[int] = []

    for argument in sys.argv[1:]:
        try:
            score = int(argument)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{argument}'")

    if len(scores) == 0:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        total = sum(scores)
        maximum = max(scores)
        minimum = min(scores)

        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {total}")
        print(f"Average score: {total / len(scores)}")
        print(f"High score: {maximum}")
        print(f"Low score: {minimum}")
        print(f"Score range: {maximum - minimum}")


if __name__ == "__main__":
    main()
