import esper

from data.components.characters.attack import Attack, Attacking
from data.components.characters import ChasePlayer, Player
from data.components.engine.physics import Position, Velocity
from data.components.engine import Cooldown
from data.scripts.engine import Vector


class ChasePlayerProcessor(esper.Processor):
    def process(self) -> None:
        for ply_ent, (ply, ply_pos) in self.world.get_components(Player, Position):
            for ent, (chase, pos, vel) in self.world.get_components(
                ChasePlayer, Position, Velocity
            ):
                if not self.world.has_component(ent, Cooldown):
                    if attack := self.world.component_for_entity(ent, Attack):
                        if Vector.distance(ply_pos, pos) <= attack.range:
                            self.world.add_component(ent, Attacking(ply_ent))
                            return

                    # Sets velocity vector in the direction of the player
                    new_vel = (ply_pos - pos).normalized()
                    vel.set(new_vel)
                else:
                    # Stop the enemy if cooling down after attack
                    vel.x = vel.y = 0
