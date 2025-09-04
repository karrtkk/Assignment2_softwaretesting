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
    g.roll(5); g.roll(5)
    g.roll(3)
    roll_many(g, 17, 0)
    assert g.score() == 16

def test_one_strike_then_three_and_four():
    g = BowlingGame()
    g.roll(10)
    g.roll(3); g.roll(4)
    roll_many(g, 16, 0)
    assert g.score() == 24

def test_perfect_game():
    g = BowlingGame()
    roll_many(g, 12, 10)
    assert g.score() == 300

def test_all_spares():
    g = BowlingGame()
    for _ in range(21):
        g.roll(5)
    assert g.score() == 150

def test_example_game_matches_expected():
    g = BowlingGame()
    g.roll(10)
    g.roll(3); g.roll(6)
    g.roll(5); g.roll(5)
    g.roll(8); g.roll(1)
    g.roll(10)
    g.roll(10)
    g.roll(10)
    g.roll(9); g.roll(0)
    g.roll(7); g.roll(3)
    g.roll(10); g.roll(10); g.roll(8)
    assert g.score() == 190

def test_regular_no_marks():
    g = BowlingGame()
    rolls = [3,4,2,5,1,6,4,2,8,1,7,1,5,3,2,3,4,3,2,6]
    for p in rolls:
        g.roll(p)
    assert g.score() == 72

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
