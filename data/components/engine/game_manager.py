import json
import os.path

SAVE_DATA = {
    "high_score": 0,
}


# Holds data for the game for changing it's state
class GameManager:
    def __init__(self) -> None:
        self.running = True
        self.game_over = False
        self.score = None

        if not os.path.isfile("save.json"):
            with open("save.json", "w") as save_file:
                json.dump(SAVE_DATA, save_file)
        with open("save.json") as save_file:
            self.save = json.load(save_file)

    # Sets a new value for a property
    def set(self, key: str, value) -> None:
        with open("save.json", "w") as save_file:
            self.save[key] = value
            json.dump(self.save, save_file)
