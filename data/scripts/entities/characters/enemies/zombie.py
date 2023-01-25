import esper
import pygame as pg

from data.components.characters import ChasePlayer
from data.components.engine.physics import Collider
from data.components.engine.physics import Position
from data.components.engine.physics import Velocity
from data.components.engine import Sprite
from data.components import Speed
from data.scripts.engine import utils


# Creates zombie entity
def create(world: esper.World) -> int:
    img = utils.load_sprite("characters/enemies/enemy.png")

    collider_rect = pg.Rect(0, 0, img.get_width(), img.get_height())
    return world.create_entity(
        ChasePlayer(),
        Collider(collider_rect),
        Position(-200, -300),
        Velocity(),
        Sprite(img),
        Speed(1),
    )
