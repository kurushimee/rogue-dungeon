import esper

from data.components.interaction import Interact


def add_interact(world: esper.World, player: int):
    if not world.has_component(player, Interact):
        world.add_component(player, Interact())


def remove_interact(world: esper.World, player: int):
    if world.has_component(player, Interact):
        world.remove_component(player, Interact)
