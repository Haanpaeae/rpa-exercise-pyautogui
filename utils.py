import random


def get_random_position(canvas_x, canvas_y, canvas_width, canvas_height, square_size=50, margin=25):
    max_x = canvas_x + canvas_width - square_size - margin
    max_y = canvas_y + canvas_height - square_size - margin
    min_x = canvas_x + margin
    min_y = canvas_y + margin
    x = random.randint(min_x, max_x)
    y = random.randint(min_y, max_y)
    return (x, y)


def is_overlapping(pos1, pos2, square_size=50):
    x1, y1 = pos1
    x2, y2 = pos2
    return not (x1 + square_size <= x2 or x1 >= x2 + square_size or y1 + square_size <= y2 or y1 >= y2 + square_size)
