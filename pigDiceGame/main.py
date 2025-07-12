from ursina import *
from ursina.shaders import lit_with_shadows_shader
from diceClass import *
from player import *

app = Ursina()
app.setBackgroundColor(53/255, 101/255, 77/255)
DirectionalLight().look_at(Vec3(1, -1, -1))  # points from top-right toward center
# Optional: ambient light for soft shadows/fill
AmbientLight(color=color.rgba(100, 100, 100, 0.5))

dice1 = Dice()
player1 = Player()
player2 = Player()

pivot = Entity()
textP1 = Text(text=f'Player 1 Score: {player1.score}', origin=(-3,-8), default_resolution = 1080 * Text.size)
textP2 = Text(text=f'Player 2 Score: {player2.score}', origin=(-3,-6), default_resolution = 1080 * Text.size)

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
    origin=(0,1.3))

endTurnButton = Button(
    scale=(.25, .125), 
    text='End Turn', 
    text_size=1, 
    highlight_color=color.rgb(53/255, 82/255, 77/255), 
    color = color.rgb(53/255, 82/255, 77/255),
    origin=(-2,2.6)
)

player1.turn = True
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

        if player1.turn:
            player1.changeScore(dice1.currentFace)
            if dice1.currentFace == 1:
                player2.turn = True

        elif player2.turn:
            player2.changeScore(dice1.currentFace)
            if dice1.currentFace == 1:
                player1.turn = True


    if endTurnButton.hovered and mouse.left and not dice1.rollAnimation and not dice1.cooldownActive:
        if player1.turn:
            player1.turn = False
            player2.turn = True
        elif player2.turn:
            player2.turn = False
            player1.turn = True

    textP1.text = f'Player 1 Score: {player1.score}'
    textP2.text = f'Player 2 Score: {player2.score}'
  

'''
def input(key):
    if key == 'space':
        dice1.roll()
    if key in ['1', '2', '3', '4', '5', '6']:
        dice1.stopOnNum(int(key))
'''
app.run()