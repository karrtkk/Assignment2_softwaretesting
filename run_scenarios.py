"""Run sample bowling scenarios."""
from bowling_game import BowlingGame

def show(name, rolls, expected, actual):
    tick = "✓" if expected == actual else "✗"
    print(f"\n{name}:\nRolls: {rolls}\nExpected score: {expected}\nActual score: {actual}\nCorrect implementation: {tick}")

def example_game():
    g = BowlingGame(); rolls = []
    g.roll(10); rolls.append(10)
    g.roll(3); g.roll(6); rolls += [3, 6]
    g.roll(5); g.roll(5); rolls += [5, 5]
    g.roll(8); g.roll(1); rolls += [8, 1]
    g.roll(10); rolls.append(10)
    g.roll(10); rolls.append(10)
    g.roll(10); rolls.append(10)
    g.roll(9); g.roll(0); rolls += [9, 0]
    g.roll(7); g.roll(3); rolls += [7, 3]
    g.roll(10); g.roll(10); g.roll(8); rolls += [10, 10, 8]
    return rolls, 190, g.score()

def perfect_game():
    g = BowlingGame(); rolls = []
    for _ in range(12):
        g.roll(10); rolls.append(10)
    return rolls, 300, g.score()

def all_spares():
    g = BowlingGame(); rolls = []
    for _ in range(21):
        g.roll(5); rolls.append(5)
    return rolls, 150, g.score()

def gutter_game():
    g = BowlingGame(); rolls = []
    for _ in range(20):
        g.roll(0); rolls.append(0)
    return rolls, 0, g.score()

def regular_game():
    g = BowlingGame()
    rolls = [3,4,2,5,1,6,4,2,8,1,7,1,5,3,2,3,4,3,2,6]
    for p in rolls:
        g.roll(p)
    return rolls, 72, g.score()

def main():
    print("BOWLING GAME – RUN SCENARIOS\n===============================")
    for name, fn in [
        ("Perfect Game", perfect_game),
        ("All Spares", all_spares),
        ("Gutter Game", gutter_game),
        ("Regular Game", regular_game),
        ("Example Game", example_game),
    ]:
        rolls, expected, actual = fn()
        show(name, rolls, expected, actual)

if __name__ == "__main__":
    main()
