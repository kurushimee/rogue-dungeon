import esper
import pygame as pg

from data.components.characters.attack import Attack
from data.components.characters import Player
from data.components.engine.physics import Collider, Position, Velocity
from data.components.engine import Sprite
from data.components import Health, Speed
from data.scripts.engine import utils, Vector


# Creates player entity
def create(screen_width: int, screen_height: int, world: esper.World) -> int:
    img = utils.load_sprite("characters/player.png")

    # Position player sprite in the middle of the screen
    left = screen_width // 2 - img.get_width() // 2
    top = screen_height // 2 - img.get_height() // 2

    x, y = 0, 0
    width = img.get_width() - 8
    # Halve the height due to it being a humanoid sprite
    height = img.get_height() // 2
    # Horizontal offset is halved to position collider in the middle
    offset_x = x + (img.get_width() - width) // 2
    # While vertical collider sticks to bottom
    offset_y = y + height
    collider_rect = pg.Rect(offset_x, offset_y, width, height)
    return world.create_entity(
        Attack(30, utils.SPRITE_SIZE * 2, 1.5),
        Player(),
        Collider(collider_rect, offset=Vector(offset_x, offset_y)),
        Position(x, y),
        Velocity(),
        Sprite(img, left, top),
        Health(100),
        Speed(3),
    )
