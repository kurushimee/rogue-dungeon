import esper
import pygame as pg

from data.components.characters import Player
from data.components.engine.physics import Collider
from data.components.engine.physics import Position
from data.components.engine.physics import Velocity
from data.components.engine import Sprite
from data.components import Speed
from data.scripts.engine import utils


# Creates player entity
def create(screen_width: int, screen_height: int, world: esper.World) -> int:
    img = utils.load_sprite("characters/player.png")

    # Position player sprite in the middle of the screen
    left = screen_width // 2 - img.get_width() // 2
    top = screen_height // 2 - img.get_height() // 2

    x, y = 0, 0
    width = img.get_width()
    height = img.get_height()
    collider_rect = pg.Rect(x, y, width, height)
    return world.create_entity(
        Player(),
        Collider(collider_rect),
        Position(x, y),
        Velocity(),
        Sprite(img, left, top),
        Speed(3),
    )
