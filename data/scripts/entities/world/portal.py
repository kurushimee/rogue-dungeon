import esper

from data.components.engine.physics import Position
from data.components.engine import Sprite
from data.components.interaction import Interactable
from data.components.world import ExitPortal
from data.scripts.actions.world import PortalAction
from data.scripts.engine import utils


# Creates portal entity
def create(world: esper.World, x: int, y: int, activated: bool = False, exit: bool = False) -> int:
    name = "portal_lit" if activated else "portal_unlit"
    img = utils.load_sprite(f"world/{name}.png")

    components = [Position(x, y), Sprite(img)]
    if activated:
        # Makes portal interactable if it's active right now
        components.append(Interactable(PortalAction()))
    if exit:
        # Gives the entity ExitPortal component, which allows
        # the game to know which portal can be unlocked at the
        # end of the level
        components.append(ExitPortal())

    return world.create_entity(*components)
