import esper
import pygame as pg

from data.components.engine import GameManager
from data.scripts.entities.buttons import exit, settings
from data.scripts.entities.characters import player
from data.scripts.entities.world import portal


# Creates the main menu
def main_init(world: esper.World, screen_width: int, screen_height: int) -> tuple:
    # Creates the game manager if there isn't any
    manager_ent = None
    for ent, manager in world.get_component(GameManager):
        manager_ent = ent
    manager_ent = manager_ent or world.create_entity(GameManager())

    exit.create(world)
    settings.create(world)
    portal.create(world, -100, -100, activated=True)

    player_ent = player.create(screen_width, screen_height, world)

    return manager_ent, player_ent


# Returns big text
def get_heading_text(text: str) -> pg.Surface:
    font = pg.font.Font(None, 50)
    return font.render(text, False, (250, 60, 60))


# Returns normal text
def get_text(text: str) -> pg.Surface:
    font = pg.font.Font(None, 40)
    return font.render(text, False, (250, 250, 250))


# Renders transparent background
def render_background(screen: pg.Surface) -> None:
    background = pg.Surface((screen.get_width(), screen.get_height()), pg.SRCALPHA)
    background.fill((0, 0, 0, 128))
    screen.blit(background, (0, 0))


# Draws the game over screen
def game_over_init(screen: pg.Surface, high_score: int) -> None:
    game_over = get_heading_text("GAME OVER")
    high_score = get_text(f"High score: {high_score}")
    prompt = get_text("Press [SPACE] to continue")

    screen_width = screen.get_width()
    screen_height = screen.get_height()
    # Positions game over text in the middle of the screen, high score and buttom prompt below
    game_over_x = screen_width // 2 - game_over.get_width() // 2
    game_over_y = screen_height // 2 - game_over.get_height() // 2
    high_score_x = screen_width // 2 - high_score.get_width() // 2
    high_score_y = game_over_y - high_score.get_height() * 1.25
    prompt_x = screen_width // 2 - prompt.get_width() // 2
    prompt_y = game_over_y + prompt.get_height() * 1.5

    render_background(screen)
    screen.blit(game_over, (game_over_x, game_over_y))
    screen.blit(high_score, (high_score_x, high_score_y))
    screen.blit(prompt, (prompt_x, prompt_y))
    pg.display.flip()
