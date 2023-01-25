import esper
import pygame as pg
from data.components.interaction import Interactable

from data.processors.characters import ChasePlayerProcessor, InteractProcessor
from data.processors.engine import RenderProcessor
from data.processors import MovementProcessor
from data.scripts.world import init
from data.scripts.input import player_input

FPS = 60
WIDTH = 960
HEIGHT = 540


def add_processors(world: esper.World, screen: pg.Surface) -> None:
    processors = (
        ChasePlayerProcessor(),
        InteractProcessor(),
        MovementProcessor(),
        RenderProcessor(screen, (11, 7, 28)),
    )
    for processor in processors:
        world.add_processor(processor)


def build_world(screen: pg.Surface) -> esper.World:
    world = esper.World()
    add_processors(world, screen)
    return world


def main() -> None:
    # Initialise PyGame
    pg.init()
    pg.display.set_caption("Rogue Dungeon")
    size = WIDTH, HEIGHT
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()

    # Initialise and setup the world
    world = build_world(screen)
    exit_ent, ply_ent = init.menu(world, WIDTH, HEIGHT)

    # Get exit button's data for the running variable
    # so that we can change it within the button
    exit_int = world.component_for_entity(exit_ent, Interactable)
    exit = exit_int.action
    # Main game cycle
    while exit.running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit.running = False
            else:
                player_input.process(world, ply_ent, event)
        world.process()
        clock.tick(FPS)
