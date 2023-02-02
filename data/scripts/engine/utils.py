import pygame as pg

FPS = 60
SPRITE_SIZE = 48


def load_sprite(path: str) -> pg.Surface:
    img = pg.image.load(f"resources/graphics/{path}")
    # Transforms sprites to be twice as big
    # so that they aren't too small in-game
    x = img.get_width() * 2
    y = img.get_height() * 2
    return pg.transform.scale(img, (x, y))
