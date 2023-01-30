import esper

from data.components.engine.physics import Position
from data.components.engine import Sprite
from data.components.interaction import Interactable
from data.scripts.actions.items import HealthpackAction
from data.scripts.engine import utils

weight = 0.1


# Creates healthpack entity
def create(world: esper.World, x: int, y: int) -> int:
    img = utils.load_sprite("items/healthpack.png")

    ent = world.create_entity(
        Position(x, x),
        Sprite(img),
        Interactable(HealthpackAction()),
    )

    # Let action know what entity it is part of for further deletion after interaction
    interactable = world.component_for_entity(ent, Interactable)
    interactable.action.ent = ent
