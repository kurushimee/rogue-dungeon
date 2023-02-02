import esper

from data.components.characters.attack import Attack, Attacking
from data.components.characters import Player
from data.components.engine import Cooldown
from data.components import Health
from data.components.engine.game_manager import GameManager


class AttackProcessor(esper.Processor):
    def process(self):
        for ent, (attack, attacking) in self.world.get_components(Attack, Attacking):
            if self.world.entity_exists(attacking.ent):
                health = self.world.component_for_entity(attacking.ent, Health)
                health.current -= attack.damage

                # Kills the entity if it's health depleted and it's not a player
                # otherwise, calls game over
                if health.current <= 0:
                    if self.world.has_component(attacking.ent, Player):
                        for _, manager in self.world.get_component(GameManager):
                            manager.game_over = True
                    else:
                        self.world.delete_entity(attacking.ent)

                self.world.add_component(ent, Cooldown(attack.cooldown))
                self.world.remove_component(ent, Attacking)
