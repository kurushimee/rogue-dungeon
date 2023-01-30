import esper


class Action:
    def __init__(self) -> None:
        self.ent = None

    # Performs logic on interacting with the entity
    def start(self, world: esper.World, ent: int) -> None:
        pass

    # Performs logic on stopping interacting with the entity
    def stop(self, world: esper.World, ent: int) -> None:
        pass
