import random
import math

class Hat():
    def __init__(self, **kwargs):
        contents = []
        for key in kwargs:
            for num in range(kwargs[key]):
                contents.append(str(key))
        self.contents = contents
        self.original_contents = contents.copy()
        
    def draw(self, num):
        if num > len(self.contents):
            self.contents = self.original_contents
            return()
        balls = []
        for i in range(num):
            ball = self.contents.pop(random.randrange(len(self.contents)))
            balls.append(ball)
        return(balls)
        
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_trials = 0.00
    for experiment in range(num_experiments):
        pass_or_fail = []
        balls_drawn = hat.draw(num_balls_drawn)
        balls_needed = []
        for key in expected_balls:
            for num in range(expected_balls[key]):
                balls_needed.append(str(key))
        for key in expected_balls:
            if balls_drawn.count(key) >= balls_needed.count(key):
                pass_or_fail.append(1)
            else:
                pass_or_fail.append(0)
        if 0 in pass_or_fail:
            pass
        else:
            successful_trials += 1
        hat.contents = hat.original_contents.copy()
    probability = successful_trials / float(num_experiments)
    return(probability)
