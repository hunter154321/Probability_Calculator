import prob_calculator
from unittest import main

prob_calculator.random.seed(40)
hat = prob_calculator.Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 3,
                    "yellow":2,
                    "test": 1
                            },
    num_balls_drawn=40,
    num_experiments=100)
print("Probability:", probability)

# Run unit tests automatically
main(module='test_module', exit=False)
