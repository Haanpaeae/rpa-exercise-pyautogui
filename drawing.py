import pyautogui
import random
from utils import get_random_position

def draw_squares():
    num_squares = random.randint(2, 5)
    positions = []

    for _ in range(num_squares):