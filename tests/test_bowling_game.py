import pytest
from bowling_game import BowlingGame

def roll_many(g, n, pins):
    for _ in range(n):
        g.roll(pins)

def test_gutter_game():
    g = BowlingGame()
    roll_many(g, 20, 0)
    assert g.score() == 0

def test_all_ones():
    g = BowlingGame()
    roll_many(g, 20, 1)
    assert g.score() == 20

def test_one_spare_then_three():
    g = BowlingGame()
    g.roll(5); g.roll(5)     # spare
    g.roll(3)                # bonus
    roll_many(g, 17, 0)
    assert g.score() == 16   # 10 + 3 + 3

def test_one_strike_then_three_four():
    g = BowlingGame()
    g.roll(10)               # strike
    g.roll(3); g.roll(4)
    roll_many(g, 16, 0)
    assert g.score() == 24   # 10 + (3+4) + (3+4)

def test_perfect_game():
    g = BowlingGame()
    for _ in range(12):
        g.roll(10)
    assert g.score() == 300

def test_roll_negative_raises():
    g = BowlingGame()
    with pytest.raises(ValueError, match="between 0 and 10"):
        g.roll(-1)

def test_roll_above_ten_raises():
    g = BowlingGame()
    with pytest.raises(ValueError, match="between 0 and 10"):
        g.roll(11)

def test_roll_non_int_raises():
    g = BowlingGame()
    with pytest.raises(ValueError, match="must be an int"):
        g.roll(3.5)  # type: ignore[arg-type]
