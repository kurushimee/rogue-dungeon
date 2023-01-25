from dataclasses import dataclass as component
import pygame as pg


@component
class Collider:
    rect: pg.Rect
