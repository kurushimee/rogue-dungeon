import esper

from data.scripts.actions import Action


class ExitAction(Action):
    def __init__(self) -> None:
        # Stores the running variable in order to
        # be able to stop the game from a button
        self.running = True

    def stop(self, world: esper.World, ent: int) -> None:
        self.running = False
