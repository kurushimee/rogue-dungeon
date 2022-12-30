import esper

from data.components import Position, Velocity

FPS = 60


class MovementProcessor(esper.Processor):
    def process(self) -> None:
        for ent, (pos, vel) in self.world.get_components(Position, Velocity):
            pos.x += vel.x
            pos.y += vel.y
