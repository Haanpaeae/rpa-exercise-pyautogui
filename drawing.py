import pyautogui
import random
from utils import get_random_position, is_overlapping


def draw_squares(canvas_x, canvas_y, canvas_width, canvas_height):

    num_squares = random.randint(2, 5)
    positions = []

    for _ in range(num_squares):
        while True:
            pos = get_random_position(
                canvas_x, canvas_y, canvas_width, canvas_height)
            if not any(is_overlapping(pos, p) for p in positions):
                positions.append(pos)
                break

        # Ensuring that the squares are drawn inside the canvas
        pos_x, pos_y = pos
        if pos_x + 50 > canvas_x + canvas_width:
            pos_x = canvas_x + canvas_width - 50
        if pos_y + 50 > canvas_y + canvas_height:
            pos_y = canvas_y + canvas_height - 50

        pyautogui.moveTo(pos_x, pos_y)
        pyautogui.dragRel(50, 0, duration=0.2)
        pyautogui.dragRel(0, 50, duration=0.2)
        pyautogui.dragRel(-50, 0, duration=0.2)
        pyautogui.dragRel(0, -50, duration=0.2)

    print(f"Squares drawn: {num_squares}")

    pyautogui.moveTo(canvas_x + canvas_width + 50,
                     canvas_y + canvas_height + 50)
    return num_squares


def mess_up_canvas(canvas_x, canvas_y, canvas_width, canvas_height):

    print("Start messing up canvas.")

    pyautogui.click(canvas_x + 10, canvas_y + 10)
    pyautogui.click(canvas_x + 30, canvas_y + 10)

    margin = 20

    for _ in range(50):
        start_x = random.randint(
            canvas_x + margin, canvas_x + canvas_width - margin)
        start_y = random.randint(
            canvas_y + margin, canvas_y + canvas_height - margin)
        pyautogui.moveTo(start_x, start_y)

        for _ in range(random.randint(5, 15)):
            end_x = random.randint(-50, 50)
            end_y = random.randint(-50, 50)

            if (canvas_x + margin <= start_x + end_x <= canvas_x + canvas_width - margin and
                    canvas_y + margin <= start_y + end_y <= canvas_y + canvas_height - margin):
                pyautogui.dragRel(end_x, end_y, duration=0.1)
                start_x += end_x
                start_y += end_y

    print("Messing up canvas done.")

    pyautogui.sleep(2)

    canvas_after_path = 'canvas_after_mess.png'
    canvas_after_image = pyautogui.screenshot(
        region=(canvas_x, canvas_y, canvas_width, canvas_height))
    canvas_after_image.save(canvas_after_path)

    print(f"Screenshot after messing up canvas saved as {canvas_after_path}")
