import esper

from data.components.engine.physics import Position
from data.components.engine import Sprite
from data.components.interaction import Interactable
from data.scripts.actions.buttons import SettingsAction
from data.scripts.engine import utils


# Creates settings button entity
def create(world: esper.World) -> int:
    img = utils.load_sprite("buttons/settings.png")
    return world.create_entity(
        Interactable(SettingsAction()),
        Position(0, -100),
        Sprite(img),
    )
