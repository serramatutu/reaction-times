import json
import time
import math
import random
import statistics
import pygame

pygame.init()

size = 400, 400
screen = pygame.display.set_mode(size)

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

MIN_WAIT = 1
MAX_WAIT = 7

def wait_for_press(key):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == key:
                return

def wait_random_time():
    time.sleep(MIN_WAIT + (MAX_WAIT - MIN_WAIT) * random.random())

def measure_reaction_time():    
    screen.fill(WHITE)
    pygame.display.flip()

    screen.fill(BLUE)
    
    wait_random_time()
    pygame.display.flip()

    start_time = time.time_ns()
    wait_for_press(pygame.K_s)
    end_time = time.time_ns()

    return (end_time - start_time)/10**9
    


screen.fill(BLACK)
pygame.display.flip()
wait_for_press(pygame.K_s)

MEASURES = 2

reaction_times = [measure_reaction_time() for i in range(MEASURES)]
mean = statistics.mean(reaction_times)
std_deviation = statistics.stdev(reaction_times)
uncertainty = std_deviation/math.sqrt(MEASURES)

output = {
    "measures": reaction_times,

    "mean": mean,
    "std_deviation": std_deviation,
    "uncertainty": uncertainty
}

with open('reaction_times.json', 'w') as f:
    f.write(json.dumps(output))

with open('reaction_times_raw.csv', 'w') as f:
    lines = ["reaction_time\n"] + [str(reaction_time) + "\n" for reaction_time in reaction_times]
    f.writelines(lines)
