import os
import random
import esper

from data.components.characters import Player
from data.components.engine.physics import Position
from data.scripts.entities.world import wall

SPRITE_SIZE = 48


# Loads level from a .txt file
def load(filename: str) -> list:
    filename = f"resources/levels/{filename}"

    # Reads level while stripping the newline from each line
    with open(filename, "r") as mapFile:
        return [line.strip() for line in mapFile]


# Builds level in the world from level data
def build(world: esper.World, level: list) -> None:
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == "#":
                x = j * SPRITE_SIZE
                # Subtracting SPRITE_SIZE from the Y coordinate is done because
                # the wall sprite is double the size in height
                y = i * SPRITE_SIZE - SPRITE_SIZE
                wall.create(world, x, y)
            elif level[i][j] == "@":
                x = j * SPRITE_SIZE
                y = i * SPRITE_SIZE
                for ent, (ply, pos) in world.get_components(Player, Position):
                    # Teleports player to the specified cell
                    pos.x = x
                    pos.y = y


# Sets up the world for a new level
def generate(world: esper.World):
    levels = os.listdir("resources/levels")
    level = load(random.choice(levels))

    build(world, level)
