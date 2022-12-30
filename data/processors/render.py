import esper
import pygame as pg

from data.components import Player, Position, Sprite


class RenderProcessor(esper.Processor):
    def __init__(self, screen: pg.Surface, clear_color=(0, 0, 0)) -> None:
        super().__init__()
        self.screen = screen
        self.clear_color = clear_color

    def process(self) -> None:
        # Clear the window
        self.screen.fill(self.clear_color)

        # Transform each sprite according to player position
        for ent, (ply_sprite, ply_pos, ply) in self.world.get_components(Sprite, Position, Player):
            for ent, (sprite, pos) in self.world.get_components(Sprite, Position):
                if not self.world.has_component(ent, Player):
                    sprite.x = ply_sprite.x + pos.x - ply_pos.x
                    sprite.y = ply_sprite.y + pos.y - ply_pos.y

        # Render each sprite
        for ent, sprite in self.world.get_component(Sprite):
            self.screen.blit(sprite.image, (sprite.x, sprite.y))

        # Update display
        pg.display.flip()
