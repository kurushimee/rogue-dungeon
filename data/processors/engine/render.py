import esper
import pygame as pg

from data.components.characters import Player
from data.components.engine.physics import Position
from data.components.engine import Sprite


class RenderProcessor(esper.Processor):
    def __init__(self, screen: pg.Surface, clear_color=(0, 0, 0)) -> None:
        super().__init__()
        self.screen = screen
        self.clear_color = clear_color

    def process(self) -> None:
        # Clear the window
        self.screen.fill(self.clear_color)

        for ply_ent, (ply_sprite, ply_pos, ply) in self.world.get_components(
            Sprite, Position, Player
        ):
            # Render player
            self.screen.blit(ply_sprite.image, (ply_sprite.x, ply_sprite.y))

            # Edit each sprite's position on screen
            for ent, sprite in self.world.get_component(Sprite):
                if ent != ply_ent and (pos := self.world.try_component(ent, Position)):
                    # Edit sprites position based based on it's position relative to player
                    # and player sprite's position (in the middle of the screen)
                    sprite.x = ply_sprite.x + pos.x - ply_pos.x
                    sprite.y = ply_sprite.y + pos.y - ply_pos.y

                    # Check if the sprite is in bounds of the screen
                    rect = sprite.image.get_rect()
                    if (
                        rect.left <= self.screen.get_width()
                        and rect.right >= 0
                        and rect.top >= 0
                        and rect.bottom <= self.screen.get_height()
                    ):
                        # Render the sprite
                        self.screen.blit(sprite.image, (sprite.x, sprite.y))

        pg.display.flip()
