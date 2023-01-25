import esper
import pygame as pg

from data.components.engine.physics import Collider
from data.components.engine.physics import Position
from data.components.engine import Sprite
from data.scripts.engine import utils


# Creates wall entity
def create(world: esper.World, x: int, y: int) -> int:
    img = utils.load_sprite("world/wall.png")

    width = img.get_width()
    # Needs to be halved because wall sprite is double in height
    height = img.get_height() // 2
    collider_rect = pg.Rect(0, 0, width, height)
    return world.create_entity(
        # Offset is needed to shift the top of the collider
        # down after halving it's height
        Collider(collider_rect, offset_y=height),
        Position(x, y),
        Sprite(img),
    )
