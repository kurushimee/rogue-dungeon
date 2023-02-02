import esper
import pygame as pg

from data.processors.characters import AttackProcessor, ChasePlayerProcessor, InteractProcessor
from data.processors.engine import CooldownProcessor, RenderProcessor
from data.processors.world import PortalProcessor
from data.processors import MovementProcessor
from data.scripts.world import menu
from data import runtime

WIDTH = 960
HEIGHT = 768


# Adds all game processors to the world
def add_processors(world: esper.World, screen: pg.Surface) -> None:
    processors = (
        AttackProcessor(),
        ChasePlayerProcessor(),
        InteractProcessor(),
        CooldownProcessor(),
        RenderProcessor(screen, (11, 7, 28)),
        PortalProcessor(),
        MovementProcessor(),
    )
    for processor in processors:
        world.add_processor(processor)


# Builds world and populates it with logic
def build_world(screen: pg.Surface) -> esper.World:
    world = esper.World()
    add_processors(world, screen)
    return world


# Sets up and runs the game
def main() -> None:
    # Initialises pygame
    pg.init()
    pg.display.set_caption("Rogue Dungeon")
    size = WIDTH, HEIGHT
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()

    # Initialises and starts the game
    world = build_world(screen)
    manager_ent, player_ent = menu.main_init(world, WIDTH, HEIGHT)
    runtime.start_game_loop(screen, clock, world, manager_ent, player_ent)
