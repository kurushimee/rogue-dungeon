import esper
import random

from data.scripts.entities.characters.enemies import zombie


def create(world: esper.World, x: int, y: int):
    enemies = (zombie,)
    enemy_weights = [x.weight for x in enemies]

    if random.random() < 0.1:
        print(random.choices(enemies, enemy_weights, k=1))#.create(world, x, y)
