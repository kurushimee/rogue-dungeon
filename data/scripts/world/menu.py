import esper

from data.scripts.entities.buttons import exit
from data.scripts.entities.buttons import settings
from data.scripts.entities.characters import player
from data.scripts.entities.world import portal


# Creates the main menu
def init(world: esper.World, screen_width: int, screen_height: int) -> tuple:
    exit_ent = exit.create(world)
    settings.create(world)
    portal.create(world, -100, -100, activated=True)
    ply_ent = player.create(screen_width, screen_height, world)

    return exit_ent, ply_ent
