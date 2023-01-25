import esper

from data.scripts.entities.buttons import exit
from data.scripts.entities.buttons import settings
from data.scripts.entities.buttons import start
from data.scripts.entities.characters import player


# Creates the main menu
def menu(world: esper.World, screen_width: int, screen_height: int) -> tuple:
    exit_ent = exit.create(world)
    settings.create(world)
    start.create(world)
    ply_ent = player.create(screen_width, screen_height, world)

    return exit_ent, ply_ent
