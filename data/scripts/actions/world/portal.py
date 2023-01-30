import esper

from data.scripts.actions import Action


class PortalAction(Action):
    def stop(self, world: esper.World, ent: int) -> None:
        from data.scripts.world import level

        level.init(world)
