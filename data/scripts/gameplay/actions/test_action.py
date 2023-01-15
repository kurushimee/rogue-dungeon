import esper

from data.scripts.gameplay.actions import Action


class TestAction(Action):
    def act(self, world: esper.World):
        print("Button pressed")

    def stop(self, world: esper.World, ply: int):
        print("Button unpressed")
        super().stop(world, ply)
