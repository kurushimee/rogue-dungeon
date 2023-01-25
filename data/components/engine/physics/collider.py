from dataclasses import dataclass as component
import pygame as pg


@component
class Collider:
    rect: pg.Rect
    offset_x: int = 0
    offset_y: int = 0
