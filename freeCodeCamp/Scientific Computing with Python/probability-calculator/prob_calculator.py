import copy
import random

class Hat:
    def __init__(self, **args):
        self.balls = args
        self.contents = [i for s in [[b] * args[b] for b in args] for i in s]
        self.nc = len(self.contents)
    def draw(self, k):
        if k >= self.nc:
            drawn_balls = copy.deepcopy(self.contents)
            self.nc = 0
            self.contents = []
            return drawn_balls
        else:
            drawn_balls = []
            for i in range(k):
                drawn_balls.append(self.contents.pop(random.randrange(self.nc)))
                self.nc -= 1
            return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    c = 0
    for _ in range(num_experiments):
        th = copy.deepcopy(hat)
        drawn_balls = th.draw(num_balls_drawn)
        for b in expected_balls:
            if drawn_balls.count(b) < expected_balls[b]:
                break
        else:
            c += 1
    return c / num_experiments
