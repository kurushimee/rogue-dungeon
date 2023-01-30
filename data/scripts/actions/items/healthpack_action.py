import esper

from data.components import Health
from data.scripts.actions import Action


class HealthpackAction(Action):
    # Restores player health and removes the healthpack
    def start(self, world: esper.World, ent: int) -> None:
        health = world.component_for_entity(ent, Health)
        if health.current != health.max:
            health.current = min(health.max, health.current + 10)
            world.delete_entity(self.ent)
