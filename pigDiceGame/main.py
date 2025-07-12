from ursina import *
from ursina.shaders import lit_with_shadows_shader
from diceClass import *


app = Ursina()
app.setBackgroundColor(53/255, 101/255, 77/255)
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
rollButton = Button(
    scale=(.5, .25), 
    text='Roll', 
    text_size=3, 
    highlight_color=color.rgb(53/255, 82/255, 77/255), 
    color = color.rgb(53/255, 82/255, 77/255),
    origin=(0,1))
def update():
    if held_keys['right mouse']:
        pivot.rotation_y += mouse.velocity[0] * camRotationSpeed
        pivot.rotation_x += -mouse.velocity[1] * camRotationSpeed
        pivot.rotation_x = clamp(pivot.rotation_x, -90, 90)
    dice1.rotate()

    if rollButton.hovered and mouse.left and not dice1.rollAnimation and not dice1.cooldownActive:
        dice1.currentFace = random.randint(1,6)
        dice1.rollAnimation = True
        dice1.stopOnNum()
    
  


def input(key):
    if key == 'space':
        dice1.roll()
    if key in ['1', '2', '3', '4', '5', '6']:
        dice1.stopOnNum(int(key))

app.run()