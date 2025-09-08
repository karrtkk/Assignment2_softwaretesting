"""Run sample bowling scenarios."""
from bowling_game import BowlingGame


def show(name, rolls, expected, actual):
    tick = "✓" if expected == actual else "✗"
    print(f"\n{name}:\nRolls: {rolls}\nExpected score: {expected}\nActual score: {actual}\nCorrect implementation: {tick}")


def perfect_game():
    g = BowlingGame(); rolls = [10] * 12
    for r in rolls: g.roll(r)
    return rolls, 300, g.score()


def all_spares():
    g = BowlingGame(); rolls = [5] * 21
    for r in rolls: g.roll(r)
    return rolls, 150, g.score()


def gutter_game():
    g = BowlingGame(); rolls = [0] * 20
    for r in rolls: g.roll(r)
    return rolls, 0, g.score()


def example_190():
    rolls = [10, 3, 6, 5, 5, 8, 1, 10, 10, 10, 9, 0, 7, 3, 10, 10, 8]
    g = BowlingGame()
    for r in rolls: g.roll(r)
    return rolls, 190, g.score()


def regular_game():
    rolls = [3, 4, 2, 5, 1, 6, 4, 2, 8, 1, 7, 1, 5, 3, 2, 3, 4, 3, 2, 6]
    g = BowlingGame()
    for r in rolls: g.roll(r)
    return rolls, sum(rolls), g.score()


def main():
    print("BOWLING GAME – RUN SCENARIOS\n===============================")
    for name, fn in [
        ("Perfect Game", perfect_game),
        ("All Spares", all_spares),
        ("Gutter Game", gutter_game),
        ("Example 190", example_190),
        ("Regular (no marks)", regular_game),
    ]:
        rolls, expected, actual = fn()
        show(name, rolls, expected, actual)


if __name__ == "__main__":
    main()
