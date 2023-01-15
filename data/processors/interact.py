import esper

from data.components import Player, Position
from data.components.interaction import Interact, Interactable
from data.scripts.engine import Vector


class InteractProcessor(esper.Processor):
    def process(self) -> None:
        for ply_ent, (ply, ply_pos, interact) in self.world.get_components(
            Player, Position, Interact
        ):
            for ent, (interactable, pos) in self.world.get_components(Interactable, Position):
                if Vector.distance(pos, ply_pos) <= interact.range:
                    interactable.action.act(self.world)
                    interactable.action.stop(self.world, ply_ent)
