import esper
import pygame as pg
from functools import partial

from data.components.engine import GameManager
from data.scripts.engine.utils import FPS
from data.scripts.input import player_input
from data.scripts.world import menu, reset


# Sets new high score if we can and shows game over screen
def set_high_score(screen: pg.Surface, manager: GameManager) -> None:
    if manager.score > manager.save["high_score"]:
        manager.set("high_score", manager.score)
    else:
        manager.score = manager.save["high_score"]

    menu.game_over_init(screen, manager.score)


# Shows the game over screen and waits for player input
def handle_game_over(
    screen: pg.Surface, clock: pg.time.Clock, world: esper.World, manager_ent: int, player_ent: int
) -> None:
    manager = world.component_for_entity(manager_ent, GameManager)
    set_high_score(screen, manager)
    while manager.running:
        # We wait for player to press spacebar in order to continue the game
        for event in pg.event.get():
            if event.type == pg.QUIT:
                manager.running = False
            elif event.type == pg.KEYUP:
                # Resumes the game if space pressed
                if event.key == pg.K_SPACE:
                    # Resets manager data for new game
                    manager.game_over = False
                    manager.score = None
                    reset.clear_world(world)
                    world.delete_entity(player_ent)
                    manager_ent, player_ent = menu.main_init(
                        world, screen.get_width(), screen.get_height()
                    )
                    start_game_loop(screen, clock, world, manager_ent, player_ent)


# Starts the main game loop
def start_game_loop(
    screen: pg.Surface, clock: pg.time.Clock, world: esper.World, manager_ent: int, player_ent: int
) -> None:
    manager = world.component_for_entity(manager_ent, GameManager)
    process_player_input = partial(player_input.process, world, player_ent)
    while manager.running:
        if manager.game_over:
            handle_game_over(screen, clock, world, manager_ent, player_ent)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                manager.running = False
            else:
                process_player_input(event)

        world.process()
        pg.display.flip()
        clock.tick(FPS)
