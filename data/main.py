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


def create_player(world: esper.World) -> int:
    ply_img = pg.image.load("resources/graphics/player.png")
    ply_img = pg.transform.scale(ply_img, (48, 48))
    ply_x = WIDTH // 2 - ply_img.get_width() // 2
    ply_y = HEIGHT // 2 - ply_img.get_height() // 2
    return world.create_entity(
        Player(), Position(0, 0), Sprite(ply_img, ply_x, ply_y), Velocity(0, 0)
    )


def create_enemy(world: esper.World) -> int:
    enemy_img = pg.image.load("resources/graphics/enemy.png")
    enemy_img = pg.transform.scale(enemy_img, (48, 48))
    return world.create_entity(Position(-150, -150), Sprite(enemy_img))


def main() -> None:
    pg.init()
    pg.display.set_caption("Rogue Dungeon")
    size = WIDTH, HEIGHT
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()

    world = build_world(screen)
    player = create_player(world)
    create_enemy(world)

    running = True
    while running:
        for event in pg.event.get():
            if event.type in (pg.QUIT, pg.KEYDOWN):
                running = False
            elif event.type == pg.KEYDOWN:
                set_velocity(event, player, 3, world)
            elif event.type == pg.KEYUP:
                reset_velocity(event, player, world)
        world.process()
        clock.tick(FPS)


def set_velocity(event: pg.event.Event, player: int, speed: int, world: esper.World) -> None:
    if event.key == pg.K_LEFT:
        world.component_for_entity(player, Velocity).x = -speed
    elif event.key == pg.K_RIGHT:
        world.component_for_entity(player, Velocity).x = speed
    elif event.key == pg.K_UP:
        world.component_for_entity(player, Velocity).y = -speed
    elif event.key == pg.K_DOWN:
        world.component_for_entity(player, Velocity).y = speed


def reset_velocity(event: pg.event.Event, player: int, world: esper.World) -> None:
    if event.key in (pg.K_LEFT, pg.K_RIGHT):
        world.component_for_entity(player, Velocity).x = 0
    if event.key in (pg.K_UP, pg.K_DOWN):
        world.component_for_entity(player, Velocity).y = 0
