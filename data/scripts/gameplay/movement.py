import pygame as pg

from data.components import Speed, Velocity


def set_velocity(key: int, speed: Speed, vel: Velocity) -> None:
    if key == pg.K_LEFT:
        vel.x = -speed.value
    elif key == pg.K_RIGHT:
        vel.x = speed.value
    elif key == pg.K_UP:
        vel.y = -speed.value
    elif key == pg.K_DOWN:
        vel.y = speed.value


def reset_velocity(key: int, vel: Velocity) -> None:
    if key in (pg.K_LEFT, pg.K_RIGHT):
        vel.x = 0
    if key in (pg.K_UP, pg.K_DOWN):
        vel.y = 0
