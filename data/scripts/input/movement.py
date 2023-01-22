from functools import partial
import pygame as pg

from data.components.engine.physics import Velocity


# Sets normalized velocity for specified axis
def set_velocity(vel: Velocity, x: float = None, y: float = None) -> None:
    if x is not None:
        vel.x = x
    if y is not None:
        vel.y = y
    vel.normalize()


def move(key: int, vel: Velocity) -> None:
    set_vel = partial(set_velocity, vel)
    if key == pg.K_LEFT:
        set_vel(x=-1)
    elif key == pg.K_RIGHT:
        set_vel(x=1)
    elif key == pg.K_UP:
        set_vel(y=-1)
    elif key == pg.K_DOWN:
        set_vel(y=1)


def stop_moving(key: int, vel: Velocity) -> None:
    set_vel = partial(set_velocity, vel)
    if key in (pg.K_LEFT, pg.K_RIGHT):
        set_vel(x=0)
    if key in (pg.K_UP, pg.K_DOWN):
        set_vel(y=0)
