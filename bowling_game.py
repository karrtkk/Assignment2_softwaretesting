"""Ten-pin bowling scorer."""
from __future__ import annotations
from typing import List

class BowlingGame:
    """Single 10-pin bowling game."""
    def __init__(self) -> None:
        self.rolls: List[int] = []

    def roll(self, pins: int) -> None:
        """Record one roll (0–10)."""
        if not isinstance(pins, int):
            raise ValueError("pins must be an int")
        if pins < 0 or pins > 10:
            raise ValueError("pins must be between 0 and 10 inclusive")
        self.rolls.append(pins)

    def _is_strike(self, i: int) -> bool:
        return i < len(self.rolls) and self.rolls[i] == 10

    def _is_spare(self, i: int) -> bool:
        return (i + 1) < len(self.rolls) and (self.rolls[i] + self.rolls[i + 1] == 10)

    def _strike_bonus(self, i: int) -> int:
        return self.rolls[i + 1] + self.rolls[i + 2]

    def _spare_bonus(self, i: int) -> int:
        return self.rolls[i + 2]

    def score(self) -> int:
        """Compute total for 10 frames."""
        score = 0
        i = 0
        for _ in range(10):
            if self._is_strike(i):
                score += 10 + self._strike_bonus(i)
                i += 1
            elif self._is_spare(i):
                score += 10 + self._spare_bonus(i)
                i += 2
            else:
                score += self.rolls[i] + self.rolls[i + 1]
                i += 2
        return score
