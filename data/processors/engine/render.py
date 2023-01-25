import esper
import pygame as pg

from data.components.characters import Player
from data.components.engine.physics import Collider, Position
from data.components.engine import Sprite


class RenderProcessor(esper.Processor):
    def __init__(self, screen: pg.Surface, clear_color=(0, 0, 0)) -> None:
        super().__init__()
        self.screen = screen
        self.clear_color = clear_color

    def process(self) -> None:
        # Clear the window
        self.screen.fill(self.clear_color)

        # Transform each sprite according to player position (except player itself)
        for ent, (ply_sprite, ply_pos, ply) in self.world.get_components(Sprite, Position, Player):
            for ent, (sprite, pos) in self.world.get_components(Sprite, Position):
                if not self.world.has_component(ent, Player):
                    sprite.x = ply_sprite.x + pos.x - ply_pos.x
                    sprite.y = ply_sprite.y + pos.y - ply_pos.y

        # Render each sprite
        for ent, sprite in self.world.get_component(Sprite):
            # Updates entity's collider position if there is any
            if coll := self.world.try_component(ent, Collider):
                coll.rect.x = sprite.x + coll.offset_x
                coll.rect.y = sprite.y + coll.offset_y

            self.screen.blit(sprite.image, (sprite.x, sprite.y))

        pg.display.flip()
