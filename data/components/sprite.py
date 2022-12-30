from dataclasses import dataclass as component
import pygame as pg


@component
class Sprite:
    image: pg.Surface
    x: int = 0
    y: int = 0
