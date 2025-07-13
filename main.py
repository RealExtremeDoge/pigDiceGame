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
textP1 = Text(text=f'Player 1 Score: {player1.score}', default_resolution = 1080 * Text.size, x=0.5, y=.40)
textP2 = Text(text=f'Player 2 Score: {player2.score}', default_resolution = 1080 * Text.size, x=0.5, y=.35)
turnIndicator = Text(text="Player 1's Turn", origin=(0, -4), scale=2)

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

def endTurn():
    if dice1.rollAnimation or dice1.cooldownActive:
        return
    if player1.turn and not player1.rollsPerTurn == 0:
        player1.turn = False
        player2.turn = True
        player1.rollsPerTurn = 0
        player1.score += player1.turnScore
        player1.turnScore = 0
    elif player2.turn and not player2.rollsPerTurn == 0:
        player2.turn = False
        player1.turn = True
        player2.rollsPerTurn = 0
        player2.score += player2.turnScore
        player2.turnScore = 0
    




player1.turn = True
def update():
    if held_keys['right mouse']:
        pivot.rotation_y += mouse.velocity[0] * camRotationSpeed
        pivot.rotation_x += -mouse.velocity[1] * camRotationSpeed
        pivot.rotation_x = clamp(pivot.rotation_x, -90, 90)
    dice1.rotate()

    #button to roll the die
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

    #button to end turn
    endTurnButton.on_click = endTurn

    textP1.text = f'Player 1 Score: {player1.score}' if player1.turnScore == 0 else f'Player 1 Score: {player1.score + player1.turnScore}'
    textP2.text = f'Player 2 Score: {player2.score}' if player2.turnScore == 0 else f'Player 2 Score: {player2.score + player2.turnScore}'
    turnIndicator.text = "Player 1's Turn" if player1.turn else "Player 2's Turn"

'''
def input(key):
    if key == 'space':
        dice1.roll()
    if key in ['1', '2', '3', '4', '5', '6']:
        dice1.stopOnNum(int(key))
'''
app.run()