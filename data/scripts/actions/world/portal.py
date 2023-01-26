import esper

from data.scripts.actions import Action


class PortalAction(Action):
    def stop(self, world: esper.World) -> None:
        from data.scripts.world import level

        level.init(world)
