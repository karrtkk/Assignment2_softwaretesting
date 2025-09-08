"""Ten-pin bowling scorer with validation."""
from __future__ import annotations
from typing import List

MAX_PINS = 10

class BowlingGame:
    """Single 10-pin bowling game with basic validation."""

    def __init__(self) -> None:
        self.rolls: List[int] = []

    # ---------- Public API ----------
    def roll(self, pins: int) -> None:
        """
        Record one roll.

        Args:
            pins: integer pins knocked down (0..10)
        Raises:
            ValueError: if pins out of range or adding this roll would
                        violate frame rules or game length.
        """
        if not isinstance(pins, int):
            raise ValueError("pins must be an int")
        if pins < 0 or pins > MAX_PINS:
            raise ValueError("pins must be between 0 and 10 inclusive")

        prospective = self.rolls + [pins]
        if not self._sequence_is_valid(prospective):
            raise ValueError("Invalid roll sequence")
        self.rolls.append(pins)

    def score(self) -> int:
        """Compute total for a complete 10-frame game."""
        score = 0
        i = 0
        # frames 1..9
        for _ in range(9):
            if self._is_strike(i):
                score += 10 + self._strike_bonus(i)
                i += 1
            elif self._is_spare(i):
                score += 10 + self._spare_bonus(i)
                i += 2
            else:
                score += self.rolls[i] + self.rolls[i + 1]
                i += 2
        # frame 10
        r = self.rolls[i:]
        if r[0] == 10:
            score += 10 + r[1] + r[2]
        elif r[0] + r[1] == 10:
            score += 10 + r[2]
        else:
            score += r[0] + r[1]
        return score

    # ---------- Helpers ----------
    def _is_strike(self, i: int) -> bool:
        return self.rolls[i] == 10

    def _is_spare(self, i: int) -> bool:
        return self.rolls[i] + self.rolls[i + 1] == 10

    def _strike_bonus(self, i: int) -> int:
        return self.rolls[i + 1] + self.rolls[i + 2]

    def _spare_bonus(self, i: int) -> int:
        return self.rolls[i + 2]

    def _sequence_is_valid(self, s: List[int]) -> bool:
        """Frames 1..9 must be ≤10 pins; 10th follows bonus rules; no extra rolls."""
        i = 0
        # frames 1..9
        for _ in range(9):
            if i >= len(s):
                return True
            a = s[i]
            if a == 10:
                i += 1
            else:
                if i + 1 >= len(s):
                    return True  # incomplete while rolling
                b = s[i + 1]
                if a + b > MAX_PINS:
                    return False
                i += 2
        # frame 10
        r = s[i:]
        if not r:
            return True
        if len(r) == 1:
            return 0 <= r[0] <= MAX_PINS
        if len(r) == 2:
            a, b = r
            return (b <= MAX_PINS) if a == 10 else (a + b <= MAX_PINS)
        if len(r) == 3:
            a, b, c = r[:3]
            if a == 10:
                return (b == 10 and 0 <= c <= MAX_PINS) or (b < 10 and b + c <= MAX_PINS)
            if a + b == 10:
                return 0 <= c <= MAX_PINS
            return False  # third roll without spare/strike
        return False      # >3 rolls in 10th never valid
