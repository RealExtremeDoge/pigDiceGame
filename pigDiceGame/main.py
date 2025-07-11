from ursina import *
from ursina.shaders import lit_with_shadows_shader
from diceClass import *


app = Ursina()
DirectionalLight().look_at(Vec3(1, -1, -1))  # points from top-right toward center
# Optional: ambient light for soft shadows/fill
AmbientLight(color=color.rgba(100, 100, 100, 0.5))

dice1 = Dice()

pivot = Entity()

camera.parent = pivot
camera.position = (0, 0, -10)  # Back the camera up
camera.look_at(pivot.position)

camRotationSpeed = 100

rotation_step = 20

def update():
    if held_keys['right mouse']:
        pivot.rotation_y += mouse.velocity[0] * camRotationSpeed
        pivot.rotation_x += -mouse.velocity[1] * camRotationSpeed
        pivot.rotation_x = clamp(pivot.rotation_x, -90, 90)
    
    dice1.rotate()
    

def input(key):
    if key == 'space':
        dice1.roll()
    if key in ['1', '2', '3', '4', '5', '6']:
        dice1.stopOnNum(int(key))

app.run()