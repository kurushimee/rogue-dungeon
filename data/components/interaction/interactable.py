from dataclasses import dataclass as component

from data.scripts.gameplay.actions import Action


@component
class Interactable:
    action: Action
