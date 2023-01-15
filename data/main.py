import esper
import pygame as pg

from data.scripts.engine import utils
from data.components import Chase, Player, Position, Speed, Sprite, Velocity
from data.components.interaction import Interactable
from data.processors import ChaseProcessor, InteractProcessor, MovementProcessor, RenderProcessor
from data.scripts.gameplay.actions import TestAction
from data.scripts.gameplay import interaction
from data.scripts.gameplay import movement

FPS = 60
WIDTH = 960
HEIGHT = 540


def add_processors(world: esper.World, screen: pg.Surface) -> None:
    world.add_processor(ChaseProcessor())
    world.add_processor(InteractProcessor())
    world.add_processor(MovementProcessor())
    world.add_processor(RenderProcessor(screen, (11, 7, 28)))


def build_world(screen: pg.Surface) -> esper.World:
    world = esper.World()
    add_processors(world, screen)
    return world


def create_player(world: esper.World) -> int:
    img = utils.load_sprite("player.png")
    x = WIDTH // 2 - img.get_width() // 2
    y = HEIGHT // 2 - img.get_height() // 2
    return world.create_entity(
        Player(), Position(0, 0), Speed(3), Sprite(img, x, y), Velocity(0, 0)
    )


def create_enemy(world: esper.World) -> int:
    img = utils.load_sprite("enemy.png")
    return world.create_entity(Chase(), Position(-200, -150), Speed(1), Sprite(img), Velocity(0, 0))


def create_exit_button(world: esper.World) -> int:
    img = utils.load_sprite("exit.png")
    return world.create_entity(Interactable(TestAction()), Position(-250, 50), Sprite(img))


def main() -> None:
    pg.init()
    pg.display.set_caption("Rogue Dungeon")
    size = WIDTH, HEIGHT
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()

    world = build_world(screen)
    player = create_player(world)
    create_enemy(world)
    create_exit_button(world)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            else:
                handle_input(world, player, event)
        world.process()
        clock.tick(FPS)


def handle_input(world: esper.World, player: int, event: pg.event.Event) -> None:
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_e:
            interaction.add_interact(world, player)
            print("Trying to interact")
        else:
            speed = world.component_for_entity(player, Speed)
            vel = world.component_for_entity(player, Velocity)
            movement.set_velocity(event.key, speed, vel)
    elif event.type == pg.KEYUP:
        if event.key == pg.K_e:
            interaction.remove_interact(world, player)
            print("Stop trying to interact")
        else:
            vel = world.component_for_entity(player, Velocity)
            movement.reset_velocity(event.key, vel)
