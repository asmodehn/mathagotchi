import pyxel

from .music import play_music
from .update import update
from .draw import draw


play_music(True, True, True)

pyxel.run(update, draw)
