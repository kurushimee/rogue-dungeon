import esper

from data.components.characters import Enemy
from data.components.interaction import Interactable
from data.components.world import ExitPortal
from data.scripts.actions.world import PortalAction


class PortalProcessor(esper.Processor):
    def process(self):
        for ent, portal in self.world.get_component(ExitPortal):
            # Activates the exit level portal if there is no enemies left
            enemies = sum(1 for _, _ in self.world.get_component(Enemy))
            if enemies == 0:
                portal.activated = True
                self.world.add_component(Interactable(PortalAction()))
