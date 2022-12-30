import esper
import pygame as pg

from data.components import Player, Position, Sprite, Velocity
from data.processors import MovementProcessor, RenderProcessor

FPS = 60
WIDTH = 960
HEIGHT = 540


def add_processors(world: esper.World, screen: pg.Surface) -> None:
    world.add_processor(MovementProcessor())
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
    player = world.create_entity(
        Player(), Position(0, 0), Sprite(ply_img, ply_x, ply_y), Velocity(0, 0)
    )
    print(player)

    enemy_img = pg.image.load("resources/graphics/enemy.png")
    enemy_img = pg.transform.scale(enemy_img, (48, 48))
    enemy = world.create_entity(Position(-150, -150), Sprite(enemy_img))
    print(enemy)

    speed = 3
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    world.component_for_entity(player, Velocity).x = -speed
                elif event.key == pg.K_RIGHT:
                    world.component_for_entity(player, Velocity).x = speed
                elif event.key == pg.K_UP:
                    world.component_for_entity(player, Velocity).y = -speed
                elif event.key == pg.K_DOWN:
                    world.component_for_entity(player, Velocity).y = speed
                elif event.key == pg.K_ESCAPE:
                    running = False
            elif event.type == pg.KEYUP:
                if event.key in (pg.K_LEFT, pg.K_RIGHT):
                    world.component_for_entity(player, Velocity).x = 0
                if event.key in (pg.K_UP, pg.K_DOWN):
                    world.component_for_entity(player, Velocity).y = 0

        world.process()

        clock.tick(FPS)
