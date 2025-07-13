from ursina import *

class Player():
    def __init__(self):
        self.score = 0
        self.turnScore = 0
        self.highscore = 0
        self.rollsPerTurn = 0
        self.turn = False
        

    def changeScore(self, num):
        if num == 1:
            self.turnScore = 0
            self.rollsPerTurn = 0
            self.turn = False
        else:
            self.rollsPerTurn += 1
            self.turnScore += num
            if self.highscore < self.score:
                self.highscore = self.score
        