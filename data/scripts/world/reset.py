import esper
from functools import partial

from data.components.characters import Player
from data.components.engine import Sprite


# Removes every entity in the world except for the player
def clear_world(world: esper.World) -> None:
    for ent, _ in world.get_component(Sprite):
        has_component = partial(world.has_component, ent)
        if not has_component(Player):
            world.delete_entity(ent)
