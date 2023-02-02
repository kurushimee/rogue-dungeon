import esper
import random

from data.scripts.entities.characters.enemies import zombie
from data.scripts.entities.items import healthpack


def create(world: esper.World, x: int, y: int):
    enemies = (zombie,)
    enemy_weights = [x.weight for x in enemies]

    loot = (healthpack,)
    loot_weights = [x.weight for x in loot]

    if random.random() <= 0.01:
        # Spawn a random enemy
        # random.choices(enemies, enemy_weights, k=1)[0].create(world, x, y)
        pass
    elif random.random() <= 0.01:
        # Spawn a random item
        random.choices(loot, loot_weights, k=1)[0].create(world, x, y)
