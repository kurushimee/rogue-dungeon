import esper
from data.components.engine.game_manager import GameManager

from data.scripts.actions import Action


class ExitAction(Action):
    # Stops the game on interaction
    def stop(self, world: esper.World, ent: int) -> None:
        for ent, manager in world.get_component(GameManager):
            manager.running = False
