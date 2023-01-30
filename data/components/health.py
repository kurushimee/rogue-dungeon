class Health:
    def __init__(self, max_health: int, curr_health: int = None):
        self.max = max_health
        self.current = curr_health or max_health
