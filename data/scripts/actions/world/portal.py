import esper

from data.scripts.actions import Action
from data.scripts.world import level


class PortalAction(Action):
    def stop(self, world: esper.World) -> None:
        level.init(world)
