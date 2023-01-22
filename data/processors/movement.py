import esper
import pygame as pg

from data.components.engine.physics import Collider, Position, Velocity
from data.components import Speed


class MovementProcessor(esper.Processor):
    def process(self) -> None:
        for ent, (pos, vel) in self.world.get_components(Position, Velocity):
            self.reset_collisions()
            # Check collision with every collidable entity if we have Collider component
            if coll := self.world.try_component(ent, Collider):
                for other_ent, other_coll in self.world.get_component(Collider):
                    if coll.rect.colliderect(other_coll.rect):
                        self.check_collision(coll.rect, other_coll.rect, vel)

            # Try to move in the direction of velocity
            if not (speed := self.world.try_component(ent, Speed).value):
                speed = 1.0
            if not self.coll_left and not self.coll_right:
                pos.x += vel.x * speed
            if not self.coll_top and not self.coll_bottom:
                pos.y += vel.y * speed

    def check_collision(self, rect: pg.Rect, other_rect: pg.Rect, vel: Velocity) -> None:
        collision_tolerance = 10
        # Check on which sides we're colliding with
        # Ignore collision if within acceptable collision_tolerance distance
        if abs(other_rect.top - rect.bottom) < collision_tolerance and vel.y > 0:
            self.coll_bottom = True
        if abs(other_rect.bottom - rect.top) < collision_tolerance and vel.y < 0:
            self.coll_top = True
        if abs(other_rect.right - rect.left) < collision_tolerance and vel.x < 0:
            self.coll_left = True
        if abs(other_rect.left - rect.right) < collision_tolerance and vel.x > 0:
            self.coll_right = True

    def reset_collisions(self):
        self.coll_top = False
        self.coll_bottom = False
        self.coll_left = False
        self.coll_right = False
