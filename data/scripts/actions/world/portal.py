import esper
from data.components.engine.game_manager import GameManager

from data.scripts.actions import Action


class PortalAction(Action):
    def stop(self, world: esper.World, ent: int) -> None:
        from data.scripts.world import level

        # Inits high score variable if it's not initialised yet
        for ent, manager in world.get_component(GameManager):
            if manager.score is None:
                manager.score = 0
            else:
                manager.score += 1

        level.init(world)
