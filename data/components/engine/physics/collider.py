from dataclasses import dataclass as component
import pygame as pg

from data.scripts.engine import Vector


@component
class Collider:
    rect: pg.Rect
    offset: Vector = Vector(0, 0)
