import pygame as pg


def load_sprite(path: str, size: int = 48) -> pg.Surface:
    img = pg.image.load(f"resources/graphics/{path}")
    img = pg.transform.scale(img, (size, size))
    return img
