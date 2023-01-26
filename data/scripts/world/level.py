import os
import random
import esper

from data.components.characters import Player
from data.components.engine.physics import Position
from data.components.engine.sprite import Sprite
from data.scripts.entities.world import portal, wall
from data.scripts.world import fill

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
            x = j * SPRITE_SIZE
            y = i * SPRITE_SIZE
            if level[i][j] == "#":
                # Subtracting SPRITE_SIZE from the Y coordinate is done because
                # the wall sprite is double the size in height
                wall.create(world, x, y - SPRITE_SIZE)
            elif level[i][j] == "@":
                for ent, (ply, pos) in world.get_components(Player, Position):
                    # Teleports player to the specified cell
                    pos.x = x
                    pos.y = y
            elif level[i][j] == "$":
                portal.create(world, x, y, exit=True)
            elif level[i][j] == ".":
                if level[i + 1][j] == "@":
                    portal.create(world, x, y)
                elif (
                    level[i + 1][j] == "."
                    and level[i - 1][j] == "."
                    and level[i][j + 1] == "."
                    and level[i][j - 1] == "."
                ):
                    fill.create(world, x, y)


# Sets up the world for a new level
def init(world: esper.World):
    levels = os.listdir("resources/levels")
    level = load(random.choice(levels))

    # Save player and remove everything else
    for ent, _ in world.get_component(Sprite):
        if not world.has_component(ent, Player):
            world.delete_entity(ent)

    build(world, level)
