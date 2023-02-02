import pygame as pg

FPS = 60
SPRITE_SIZE = 48


# Returns a sprite image at the specified path
def load_sprite(path: str) -> pg.Surface:
    img = pg.image.load(f"resources/graphics/{path}")
    # Transforms sprites to be twice as big
    # so that they aren't too small in-game
    x = img.get_width() * 2
    y = img.get_height() * 2
    return pg.transform.scale(img, (x, y))


# Returns big text
def get_heading_text(text: str, size: int = 50) -> pg.Surface:
    font = pg.font.Font(None, size)
    return font.render(text, False, (250, 60, 60))


# Returns normal text
def get_text(text: str, size: int = 40) -> pg.Surface:
    font = pg.font.Font(None, size)
    return font.render(text, False, (250, 250, 250))
