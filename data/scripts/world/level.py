import os
import random
import esper

from data.components.characters import Player
from data.components.engine.physics import Position
from data.components.engine.sprite import Sprite
from data.scripts.entities.world import portal, wall
from data.scripts.world import fill
from data.scripts.engine import utils


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
            x = j * utils.SPRITE_SIZE
            y = i * utils.SPRITE_SIZE
            if level[i][j] == "#":
                # Subtracting SPRITE_SIZE from the Y coordinate is done because
                # the wall sprite is double the size in height
                wall.create(world, x, y - utils.SPRITE_SIZE)
            elif level[i][j] == "@":
                for ent, (ply, pos) in world.get_components(Player, Position):
                    # Teleports player to the specified cell
                    pos.x = x
                    pos.y = y
            elif level[i][j] == "$":
                # Creates exit portal
                portal.create(world, x, y, exit=True)
            elif level[i][j] == ".":
                if level[i + 1][j] == "@":
                    # Creates the enter portal if player is right below
                    portal.create(world, x, y)
                else:
                    # Tries to populate with enemies or loot
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
