import esper


class Action:
    # Performs logic on interacting with the entity
    def act(self, world: esper.World) -> None:
        pass

    # Performs logic on stopping interacting with the entity
    def stop(self, world: esper.World) -> None:
        pass
