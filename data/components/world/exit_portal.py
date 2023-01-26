from dataclasses import dataclass as component


@component
class ExitPortal:
    activated: bool = False
