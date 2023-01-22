import esper
import pygame as pg

from data.scripts.engine import utils
from data.components.characters import ChasePlayer, Player
from data.components.engine.physics import Collider, Position, Velocity
from data.components.engine import Sprite
from data.components.interaction import Interactable
from data.components import Speed
from data.scripts.actions.buttons import ExitAction


def create_player(world: esper.World, width: int, height: int) -> int:
    img = utils.load_sprite("player.png")
    # Set coordinates for the player image in the middle of the screen
    # so that other sprites will be based off it
    x = width // 2 - img.get_width() // 2
    y = height // 2 - img.get_height() // 2
    collider_rect = pg.Rect(x, y, img.get_width(), img.get_height())
    return world.create_entity(
        Collider(collider_rect),
        Player(),
        Position(0, 0),
        Speed(3),
        Sprite(img, x, y),
        Velocity(0, 0),
    )


def create_enemy(world: esper.World) -> int:
    img = utils.load_sprite("enemy.png")
    collider_rect = pg.Rect(0, 0, img.get_width(), img.get_height())
    return world.create_entity(
        ChasePlayer(),
        Collider(collider_rect),
        Position(-200, -150),
        Speed(1),
        Sprite(img),
        Velocity(0, 0),
    )


def create_exit_button(world: esper.World) -> int:
    img = utils.load_sprite("exit.png")
    return world.create_entity(Interactable(ExitAction()), Position(-250, 50), Sprite(img))
