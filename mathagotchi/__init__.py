import pyxel

pyxel.init(200, 150)

# TODO : in case we want a modular game, usable inside another game

pyxel.image(0).set(
    0,
    0,
    [
        "00011000",
        "00010100",
        "00010010",
        "00010010",
        "00010100",
        "00010000",
        "01110000",
        "01100000",
    ],
)

pyxel.sound(0).set(
    "e2e2c2g1 g1g1c2e2 d2d2d2g2 g2g2rr" "c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr",
    "p",
    "6",
    "vffn fnff vffs vfnn",
    25,
)

pyxel.sound(1).set(
    "r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2" "f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ",
    "s",
    "6",
    "nnff vfff vvvv vfff svff vfff vvvv svnn",
    25,
)

pyxel.sound(2).set(
    "c1g1c1g1 c1g1c1g1 b0g1b0g1 b0g1b0g1" "a0e1a0e1 a0e1a0e1 g0d1g0d1 g0d1g0d1",
    "t",
    "7",
    "n",
    25,
)

pyxel.sound(3).set(
    "f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1" "f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1",
    "t",
    "7",
    "n",
    25,
)

pyxel.sound(4).set("f0ra4r f0ra4r f0ra4r f0f0a4r", "n", "6622 6622 6622 6422", "f", 25)
