import esper

from data.components.characters import ChasePlayer, Player
from data.components.engine.physics import Position, Velocity


class ChasePlayerProcessor(esper.Processor):
    def process(self) -> None:
        for ent, (ply, ply_pos) in self.world.get_components(Player, Position):
            for ent, (chase, pos, vel) in self.world.get_components(
                ChasePlayer, Position, Velocity
            ):
                # Sets velocity vector in the direction of the player
                new_vel = (ply_pos - pos).normalized()
                vel.set(new_vel)
