import esper

from data.scripts.actions import Action
from data.scripts.world import level


class StartAction(Action):
    def stop(self, world: esper.World) -> None:
        level.generate(world)
