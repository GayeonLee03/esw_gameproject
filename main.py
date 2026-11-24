from PIL import Image
import time
from Joystick import Joystick
from player import Player
from monster import Monster
from equipped_monster import EquippedMonster
from monster_ball import MonsterBall


def main():
    joystick = Joystick()

    start_image = Image.open("images/start.png").convert("RGB")
    background = Image.open("images/background.png").convert("RGB")

    player = Player(Image.open("images/player.png").convert("RGBA"))
    monster = Monster("Momo", Image.open("images/monster.png").convert("RGBA"), 156, 65)
    equipped = EquippedMonster("Pipi", Image.open("images/equipped_monster.png").convert("RGBA"))
    ball = MonsterBall(Image.open("images/monster_ball.png").convert("RGBA"))

    game_started = False
    joystick.disp.image(start_image)

    while True:
        if game_started == False:
            if not joystick.button_A.value:
                game_started = True
                my_image = background.copy()
                player.draw(my_image)
                monster.draw(my_image)
                joystick.disp.image(my_image)

        else:
            command = {'move': False, 'up_pressed': False, 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}

            if not joystick.button_U.value:
                command['up_pressed'] = True
                command['move'] = True

            if not joystick.button_D.value:
                command['down_pressed'] = True
                command['move'] = True

            if not joystick.button_L.value:
                command['left_pressed'] = True
                command['move'] = True

            if not joystick.button_R.value:
                command['right_pressed'] = True
                command['move'] = True

            player.move(command)

            my_image = background.copy()
            player.draw(my_image)
            monster.draw(my_image)

            joystick.disp.image(my_image)  

        time.sleep(0.05)


if __name__ == '__main__':
    main()
