import esper

from data.components.interaction.interact import Interact


class Action:
    def act(self, world: esper.World) -> None:
        pass

    def stop(self, world: esper.World, ply: int) -> None:
        if world.has_component(ply, Interact):
            world.remove_component(ply, Interact)
