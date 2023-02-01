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
        # Render each sprite
        self.render()
        # Update the screen
        pg.display.flip()

    # Renders each sprite, correcting their relative on-screen position
    def render(self):
        for ply_ent, (ply_sprite, ply_pos, ply) in self.world.get_components(
            Sprite, Position, Player
        ):
            # Render player
            self.screen.blit(ply_sprite.image, (ply_sprite.x, ply_sprite.y))

            for ent, (pos, sprite) in self.world.get_component(Position, Sprite):
                if ent != ply_ent:
                    self.set_relative_position(ply_pos, pos, ply_sprite, sprite)
                    self.blit_sprite(sprite)

    # Edits sprites position based based on entity's position relative to player
    # and player sprite's position (in the middle of the screen)
    def set_relative_position(
        self, ply_pos: Position, pos: Position, ply_sprite: Sprite, sprite: Sprite
    ) -> None:
        sprite.x = ply_sprite.x + pos.x - ply_pos.x
        sprite.y = ply_sprite.y + pos.y - ply_pos.y

    # Blits the sprite to the screen if it's in bounds of it
    def blit_sprite(self, sprite: Sprite) -> None:
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
