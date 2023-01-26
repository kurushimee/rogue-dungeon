import esper
import pygame as pg

from data.components.engine.physics import Velocity
from data.scripts.input import interaction
from data.scripts.input import movement


def process(world: esper.World, player: int, event: pg.event.Event) -> None:
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_f:
            interaction.add_interact(world, player)
        else:
            vel = world.component_for_entity(player, Velocity)
            movement.move(event.key, vel)
    elif event.type == pg.KEYUP:
        if event.key == pg.K_f:
            interaction.remove_interact(world, player)
        else:
            vel = world.component_for_entity(player, Velocity)
            movement.stop_moving(event.key, vel)
