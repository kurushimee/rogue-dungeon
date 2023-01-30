import esper

from data.scripts.actions import Action
from data.scripts.world import level


class StartAction(Action):
    def stop(self, world: esper.World, ent: int) -> None:
        level.init(world)
