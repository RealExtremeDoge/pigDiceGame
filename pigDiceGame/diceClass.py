from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.curve import out_expo
import random

class Dice(Entity):
    def __init__(self):
        super().__init__(model='dice.obj', shader=lit_with_shadows_shader, scale=0.5)
        self.rotationSpeedX = 0
        self.rotationSpeedY = 0
        self.rotationSpeedZ = 0
        self.spinning = False
        self.diceFaces = {
            1: Vec3(0, 0, 0),
            2: Vec3(270, -90, 0),
            3: Vec3(270, -270, 0),
            4: Vec3(270, 0, 0),
            5: Vec3(90, 0, 0),
            6: Vec3(180, 0, 0),
        }
    def rotate(self):
        if self.spinning == True:
            self.rotation_x += self.rotationSpeedX * time.dt
            self.rotation_y += self.rotationSpeedY * time.dt
            self.rotation_z += self.rotationSpeedZ * time.dt

    def roll(self):
        self.spinning = True
        self.rotationSpeedX = random.randint(360, 720)
        self.rotationSpeedY = random.randint(360, 720)
        self.rotationSpeedZ = random.randint(360, 720)

    def stopOnNum(self, num):
        self.spinning = False
        self.animate_rotation(self.diceFaces[num], duration=2, curve=out_expo)