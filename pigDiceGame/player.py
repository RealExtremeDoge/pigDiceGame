from ursina import *

class Player():
    def __init__(self):
        self.score = 0
        self.turn = False
        self.highscore = 0

    def changeScore(self, num):
        if num == 1:
            self.score = 0
            self.turn = False
        else:
            self.score += num
            if self.highscore < self.score:
                self.highscore = self.score
        