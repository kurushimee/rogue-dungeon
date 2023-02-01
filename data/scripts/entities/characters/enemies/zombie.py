import esper
import pygame as pg

from data.components.characters.attack import Attack
from data.components.characters import ChasePlayer, Enemy
from data.components.engine.physics import Collider, Position, Velocity
from data.components.engine import Sprite
from data.components import Health, Speed
from data.scripts.engine import utils

weight = 0.1


# Creates zombie entity
def create(world: esper.World, x: int, y: int) -> int:
    img = utils.load_sprite("characters/enemies/zombie.png")

    collider_rect = pg.Rect(x, y, img.get_width(), img.get_height())
    return world.create_entity(
        Attack(15, utils.SPRITE_SIZE * 1.5, 2),
        ChasePlayer(),
        Enemy(),
        Collider(collider_rect),
        Position(x, y),
        Velocity(),
        Sprite(img),
        Health(50),
        Speed(1),
    )
