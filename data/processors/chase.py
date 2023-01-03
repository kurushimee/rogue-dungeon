import esper

from data.components import Chase, Player, Position, Speed, Velocity
from data.engine import Vector


class ChaseProcessor(esper.Processor):
    def process(self) -> None:
        for ent, (ply, ply_pos) in self.world.get_components(Player, Position):
            for ent, (chase, pos, speed, vel) in self.world.get_components(
                Chase, Position, Speed, Velocity
            ):
                new_vel = (ply_pos - pos).normalized()
                new_vel *= Vector(speed.value, speed.value)
                vel.set(new_vel.x, new_vel.y)
