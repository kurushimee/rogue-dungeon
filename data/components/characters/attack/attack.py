from dataclasses import dataclass as component


@component
class Attack:
    damage: int
    range: int
    cooldown: float
