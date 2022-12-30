import esper
import pygame as pg

from data.components import Player, Position, Sprite
from data.processors import RenderProcessor

FPS = 60
WIDTH = 960
HEIGHT = 540


def add_processors(world: esper.World, screen: pg.Surface) -> None:
    world.add_processor(RenderProcessor(screen, (11, 7, 28)))


def build_world(screen: pg.Surface) -> esper.World:
    world = esper.World()
    add_processors(world, screen)
    return world


def main() -> None:
    pg.init()
    pg.display.set_caption("Rogue Dungeon")
    size = WIDTH, HEIGHT
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()

    world = build_world(screen)

    ply_img = pg.image.load("resources/graphics/player.png")
    ply_img = pg.transform.scale(ply_img, (48, 48))
    ply_x = WIDTH // 2 - ply_img.get_width() // 2
    ply_y = HEIGHT // 2 - ply_img.get_height() // 2
    player_id = world.create_entity(Player(), Position(0, 0), Sprite(ply_img, ply_x, ply_y))
    print(player_id)

    enemy_img = pg.image.load("resources/graphics/enemy.png")
    enemy_img = pg.transform.scale(enemy_img, (48, 48))
    enemy_id = world.create_entity(Position(-150, -150), Sprite(enemy_img))
    print(enemy_id)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        world.process()
        clock.tick(FPS)
