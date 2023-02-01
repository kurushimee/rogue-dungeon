import esper

from data.components.characters.attack import Attack, Attacking
from data.components.engine import Cooldown
from data.components import Health


class AttackProcessor(esper.Processor):
    def process(self):
        for ent, (attack, attacking) in self.world.get_components(Attack, Attacking):
            if self.world.entity_exists(attacking.ent):
                health = self.world.component_for_entity(attacking.ent, Health)
                health.current -= attack.damage
                print(f"{attacking.ent} took {attack.damage} damage, left with {health.current} HP")

                if health.current <= 0:
                    print(f"{attacking.ent} has {health.current} HP, deleting...")
                    self.world.delete_entity(attacking.ent)

                self.world.add_component(ent, Cooldown(attack.cooldown))
                self.world.remove_component(ent, Attacking)
