from dataclasses import dataclass as component


@component
class Health:
    max: int
    current: int = max
