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
    # Needed to shift the top of the collider
    # down after halving it's height
    offset_y = y + height
    collider_rect = pg.Rect(x, offset_y, width, height)
    return world.create_entity(
        Collider(collider_rect),
        Position(x, y),
        Sprite(img),
    )
