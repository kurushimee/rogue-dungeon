import esper

from data.components.characters.attack import Attack, Attacking
from data.components.characters import Enemy
from data.components.engine.physics import Position
from data.components.engine import Cooldown
from data.scripts.engine import Vector


# Adds Attacking component to player for handling attack
def set_attack(world: esper.World, ent: int):
    attack = world.component_for_entity(ent, Attack)
    pos = world.component_for_entity(ent, Position)

    if not world.has_component(ent, Cooldown):
        for mob_ent, (enemy, mob_pos) in world.get_components(Enemy, Position):
            # Attack if in range
            if Vector.distance(pos, mob_pos) <= attack.range:
                world.add_component(ent, Attacking(mob_ent))
                return
