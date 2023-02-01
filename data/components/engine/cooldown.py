from dataclasses import dataclass as component


@component
class Cooldown:
    limit: float
    value: float = 0.0
