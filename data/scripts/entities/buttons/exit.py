import esper

from data.components.engine.physics import Position
from data.components.engine import Sprite
from data.components.interaction import Interactable
from data.scripts.actions.buttons import ExitAction
from data.scripts.engine import utils


# Creates exit button entity
def create(world: esper.World) -> int:
    img = utils.load_sprite("buttons/exit.png")
    return world.create_entity(
        Position(100, -100),
        Sprite(img),
        Interactable(ExitAction()),
    )
