import esper

from data.components.engine import Cooldown

FPS = 60


class CooldownProcessor(esper.Processor):
    def process(self):
        for ent, cooldown in self.world.get_component(Cooldown):
            if cooldown.value < cooldown.limit:
                # Increase cooldown by time spent between frames
                cooldown.value += 1 / FPS
            else:
                self.world.remove_component(ent, Cooldown)
