import pyxel
from .music import play_music


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    if pyxel.btnp(pyxel.KEY_1):
        play_music(True, True, True)

    if pyxel.btnp(pyxel.KEY_2):
        play_music(True, False, False)

    if pyxel.btnp(pyxel.KEY_3):
        play_music(False, True, False)

    if pyxel.btnp(pyxel.KEY_4):
        play_music(False, False, True)

    if pyxel.btnp(pyxel.KEY_5):
        play_music(False, False, False)
