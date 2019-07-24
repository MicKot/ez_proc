import time
from datetime import datetime


def timer_decorator(func):
    def time_(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time elapsed:{:.5f}s".format(end - start))
        return result

    return time_


class Timer:
    def __init__(self):
        self.events = {}

    def register(self, event_name=None):
        self.timer_start = time.time()
        if event_name is not None:
            self.events[event_name] = self.timer_start
        else:
            self.events[str(datetime.now())] = self.timer_start

    def get_since(self, event_name=None):
        if not hasattr(self, "timer_start"):
            print("Error: timer not started, next time start it, bucko")
            return
        self.timer_end = time.time()
        if event_name is not None:
            print(
                "Time elapsed since event {}: {:.5f}s".format(
                    event_name, self.timer_end - self.events[event_name]
                )
            )
        else:
            print(
                "Time elapsed since last event: {:.5f}s".format(
                    self.timer_end - self.timer_start
                )
            )

    def get_between(self, first_event_name, second_event_name):
        started = self.events[first_event_name]
        ended = self.events[second_event_name]
        print(
            "Time elapsed between {} and {} {:.5f}s".format(
                first_event_name, second_event_name, ended - started
            )
        )

    def get_events(self):
        return [(x, y) for x, y in self.events.items()]

    def reset_timer(self):
        self.events = {}
