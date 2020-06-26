Mathagotchi
=============

Dependency setup
----------------

On Ubuntu::

    sudo apt install python3 python3-pip libsdl2-dev libsdl2-image-dev gifsicle
    pip3 install -U mathagotchi

Run
---

From command line::

    python mathagotchi

DESIGN
------

Still work in progress :

- a simple game inspired by tamagochi (https://arcadespot.com/game/tamagotchi/) + chocobo world (https://finalfantasy.fandom.com/wiki/Chocobo_World)
- some way to look for metamath proof just like one would "mine" crypto currency
- some interraction between the two...

As a result:

- a metamath database can be "the world to explore" or the "player ingame log"
- game should be able to run unsupervised (idle-mode) and still be useful (maybe an exploration as a learning experience)
- when player actively plays the game, it is a more gamified way to explore & build metamath proofs

Other Ideas ? write up an issue to start the conversation...

TODO
----

- resources using metamath symbols
- integrate mmverify in code somehow
- determine if we inteerface directly with metamath C code or if we build some missing pieces on top of mmverify...
