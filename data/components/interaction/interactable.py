from dataclasses import dataclass as component

from data.scripts.actions import Action


@component
class Interactable:
    action: Action
