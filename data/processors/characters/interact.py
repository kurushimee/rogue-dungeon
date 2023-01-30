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
                    if interact.stopping:
                        # Call action.stop() on key release
                        interactable.action.stop(self.world, ply_ent)
                        # Remove Interact component in order to stop interacting
                        if self.world.has_component(ply_ent, Interact):
                            self.world.remove_component(ply_ent, Interact)
                    else:
                        # Call action.start() on key press
                        interactable.action.start(self.world, ply_ent)
