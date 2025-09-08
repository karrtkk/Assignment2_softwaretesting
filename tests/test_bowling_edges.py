import pytest
from bowling_game import BowlingGame

def roll_many(g, pins):
    for p in pins:
        g.roll(p)

def test_spare_then_strike_scoring():
    g = BowlingGame()
    roll_many(g, [5,5, 10, 3,4] + [0]*14)
    assert g.score() == 44

def test_strike_then_spare_scoring():
    g = BowlingGame()
    roll_many(g, [10, 5,5, 3,0] + [0]*14)
    assert g.score() == 36

def test_invalid_frame_overflow_raises():
    g = BowlingGame()
    g.roll(6)
    with pytest.raises(ValueError):
        g.roll(7)  # 6+7 > 10 in a normal frame

def test_nine_strikes_then_9_spare_X_scores_279():
    g = BowlingGame()
    roll_many(g, [10]*9 + [9,1,10])  # X X X X X X X X X  9/ X
    assert g.score() == 279

def test_game_disallows_extra_rolls_without_bonus():
    g = BowlingGame()
    roll_many(g, [1,1]*10)  # 20 open rolls
    with pytest.raises(ValueError):
        g.roll(0)  # 21st roll not allowed
