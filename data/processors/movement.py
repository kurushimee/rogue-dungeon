import esper
import pygame as pg
from functools import partial
from typing import Callable

from data.components.engine.physics import Collider, Position, Velocity
from data.components import Speed


class MovementProcessor(esper.Processor):
    def process(self) -> None:
        for ent, (pos, vel) in self.world.get_components(Position, Velocity):
            if not (speed := self.world.try_component(ent, Speed).value):
                speed = 1.0
            coll = self.world.try_component(ent, Collider)
            # Move in the direction of velocity
            # and correct if colliding
            pos.x += vel.x * speed
            if coll:
                coll.rect.x = pos.x + coll.offset.x
                check = partial(self.check_x, pos, vel, coll)
                self.check_collision(ent, coll, check)
            pos.y += vel.y * speed
            if coll:
                coll.rect.y = pos.y + coll.offset.y
                check = partial(self.check_y, pos, vel, coll)
                self.check_collision(ent, coll, check)

    def check_collision(self, ent: int, coll: Collider, check: Callable):
        for other_ent, other_coll in self.world.get_component(Collider):
            if other_ent != ent and coll.rect.colliderect(other_coll.rect):
                check(other_coll.rect)

    def check_x(
        self, pos: Position, vel: Velocity, coll: Collider, other_coll: pg.Rect
    ) -> None:
        if vel.x < 0:
            pos.x = other_coll.right
        if vel.x > 0:
            pos.x = other_coll.left - coll.rect.width
        pos.x -= coll.offset.x
        coll.rect.x = pos.x + coll.offset.x

    def check_y(
        self, pos: Position, vel: Velocity, coll: Collider, other_coll: pg.Rect
    ) -> None:
        if vel.y > 0:
            pos.y = other_coll.top - coll.rect.height
        if vel.y < 0:
            pos.y = other_coll.bottom
        pos.y -= coll.offset.y
        coll.rect.y = pos.y + coll.offset.y
