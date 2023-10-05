import random

class Game:
    def __init__(self):
        self.frames = []
        self.next_frame = 0

    def roll(self, pins):
        self.frames[self.next_frame].add_roll(pins)
        self.next_frame = (self.next_frame + 1) % 10

    def score(self):
        score = 0
        for frame in self.frames:
            score += frame.score()
        return score

class Frame:
    def __init__(self, pins):
        self.rolls = []
        self.pins = pins

    def add_roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        if len(self.rolls) == 2:
            if self.rolls[0] + self.rolls[1] == 10:
                return 10 + self.rolls[2] if len(self.rolls) > 2 else 10
            else:
                return self.rolls[0] + self.rolls[1]
        else:
            return sum(self.rolls)

class NormalFrame(Frame):
    def __init__(self, pins):
        super().__init__(pins)

class TenthFrame(Frame):
    def __init__(self, pins):
        super().__init__(pins)


