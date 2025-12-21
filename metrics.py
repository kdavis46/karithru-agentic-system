import time

class Metrics:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    @property
    def elapsed_seconds(self):
        if self.start_time is None or self.end_time is None:
            return None
        return self.end_time - self.start_time
