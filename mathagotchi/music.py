import pyxel


def play_music(ch0, ch1, ch2):
    if ch0:
        pyxel.play(0, [0, 1], loop=True)
    else:
        pyxel.stop(0)

    if ch1:
        pyxel.play(1, [2, 3], loop=True)
    else:
        pyxel.stop(1)

    if ch2:
        pyxel.play(2, 4, loop=True)
    else:
        pyxel.stop(2)
