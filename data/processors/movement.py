import esper
from functools import partial

from data.components.engine.physics import Collider, Position, Velocity
from data.components import Speed

SPRITE_WIDTH = 48


class MovementProcessor(esper.Processor):
    def process(self) -> None:
        # Cache method call for performance
        get_components = self.world.get_components
        get_component = self.world.get_component
        try_component = self.world.try_component
        fix_colliding = partial(self.fix_colliding, get_component)
        for ent, (pos, vel) in get_components(Position, Velocity):
            # Skip entity if it's not trying to move
            if vel.x != 0 or vel.y != 0:
                # Initialise speed if there isn't any
                if not (speed := try_component(ent, Speed).value):
                    speed = 1.0

                # Moves in the direction of velocity
                pos.x += vel.x * speed
                if coll := try_component(ent, Collider):
                    # Updates collider position
                    coll.rect.x = pos.x + coll.offset.x
                    # Tries to adjust our position out of an object
                    # if we got inside of it after moving
                    fix_colliding(ent, pos, vel, coll, x=True)

                pos.y += vel.y * speed
                if coll:
                    coll.rect.y = pos.y + coll.offset.y
                    fix_colliding(ent, pos, vel, coll, y=True)

    # Fixes movement if it caused us to collide
    def fix_colliding(
        self,
        get_component: esper.World.get_component,
        ent: int,
        pos: Position,
        vel: Velocity,
        coll: Collider,
        x: bool = False,
        y: bool = False,
    ) -> None:
        for other_ent, other_coll in get_component(Collider):
            if other_ent != ent and coll.rect.colliderect(other_coll.rect):
                if x:
                    # Move back outside of the collider
                    if vel.x > 0:
                        pos.x = other_coll.rect.left - coll.rect.width
                    else:
                        pos.x = other_coll.rect.right
                    # Move to accomodate for collider offset if there's any
                    pos.x -= coll.offset.x
                    # Update collider position
                    coll.rect.x = pos.x + coll.offset.x
                elif y:
                    # Move back outside of the collider
                    if vel.y > 0:
                        pos.y = other_coll.rect.top - coll.rect.height
                    else:
                        pos.y = other_coll.rect.bottom
                    # Move to accomodate for collider offset if there's any
                    pos.y -= coll.offset.y
                    # Update collider position
                    coll.rect.y = pos.y + coll.offset.y
