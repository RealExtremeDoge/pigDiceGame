from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.curve import out_expo
import random

class Dice(Entity):
    def __init__(self):
        super().__init__(model='diceRed.obj', shader=lit_with_shadows_shader, scale=0.5)
        self.rotationSpeedX = 0
        self.rotationSpeedY = 0
        self.rotationSpeedZ = 0
        self.currentFace = 1
        self.spinning = False
        self.rollAnimation = False
        self.cooldownActive = False
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
        self.rotationSpeedX = random.randint(100, 360)
        self.rotationSpeedY = random.randint(100, 360)
        self.rotationSpeedZ = random.randint(100, 360)

    def stopOnNum(self):
        self.spinning = False
        self.animate_rotation(self.diceFaces[self.currentFace], duration=1.5, curve=out_expo)
        invoke(self.finish_roll, delay=1)
        
    def finish_roll(self):
        self.rollAnimation = False
        self.cooldownActive = True
        invoke(self.end_cooldown, delay=1)  # ← cooldown duration

    def end_cooldown(self):
        self.cooldownActive = False


'''
to-do
make dice metallic so its fire
make turn based                          ||DONE||
start screen
'''