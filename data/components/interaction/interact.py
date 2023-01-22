from dataclasses import dataclass as component


@component
class Interact:
    range: float = 50
    stopping: bool = False
