import esper

from data.components.characters import Player
from data.components.engine.physics import Position
from data.components.interaction import Interact, Interactable
from data.scripts.engine import Vector


class InteractProcessor(esper.Processor):
    def process(self) -> None:
        for ply_ent, (ply, ply_pos, interact) in self.world.get_components(
            Player, Position, Interact
        ):
            for ent, (interactable, pos) in self.world.get_components(Interactable, Position):
                if Vector.distance(pos, ply_pos) <= interact.range:
                    # Call action.stop() when unpressing the button, otherwise call action.act()
                    # Remove Interact component after calling action.stop()
                    # in order to stop interacting
                    if interact.stopping:
                        interactable.action.stop(self.world)
                        self.world.remove_component(ply_ent, Interact)
                    else:
                        interactable.action.act(self.world)
