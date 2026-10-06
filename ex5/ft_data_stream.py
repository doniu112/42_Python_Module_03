import random
import typing


def gen_event() -> typing.Generator[
    tuple[str, str],
    None,
    None,
]:
    players = [
        "alice",
        "bob",
        "charlie",
        "dylan",
    ]

    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]

    while True:
        player = random.choice(players)
        action = random.choice(actions)

        yield (player, action)


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[
    tuple[str, str],
    None,
    None,
]:
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events.pop(index)

        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()

    for index in range(1000):
        event = next(event_generator)

        print(
            f"Event {index}: "
            f"Player {event[0]} "
            f"did action {event[1]}"
        )

    events: list[tuple[str, str]] = []

    event_generator = gen_event()

    for _ in range(10):
        events.append(next(event_generator))

    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()