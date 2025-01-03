from drawing import draw_squares, mess_up_canvas
from image_recognition import count_squares
import pyautogui


def main():
    # Open Paint
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('mspaint')
    pyautogui.press('enter')

    # Wait until Paint opens
    pyautogui.sleep(5)

    # Maximize window size
    pyautogui.hotkey('win', 'up')

    pyautogui.sleep(3)

    # Find borders of canvas
    canvas = pyautogui.locateOnScreen('canvas_full.png', confidence=0.9)
    if not canvas:
        raise Exception("Canvas not found.")
    else:
        print(f"Canvas found: {canvas}")

    canvas_x, canvas_y = int(canvas.left), int(canvas.top)
    canvas_width, canvas_height = int(canvas.width), int(canvas.height)
    canvas_region = (canvas_x, canvas_y, canvas_width, canvas_height)

    # Draw squares
    num_squares = draw_squares(canvas_x, canvas_y, canvas_width, canvas_height)

    pyautogui.sleep(2)

   # Screenshot of the canvas after drawing the squares
    canvas_image = pyautogui.screenshot(
        region=(canvas_x, canvas_y, canvas_width, canvas_height))
    canvas_image.save('canvas_before_mess.png')

    # Count squares
    squares_counted = count_squares(canvas_region=canvas_region)
    if squares_counted == num_squares:
        print("The number of squares matches!")
    else:
        print(
            f"Error: was expected {num_squares}, but was found {squares_counted}.")

    pyautogui.sleep(2)

    mess_up_canvas(canvas_x, canvas_y, canvas_width, canvas_height)

    # Screenshot after messing up and recounting the squares
    squares_counted_after = count_squares(canvas_region=canvas_region)
    print(f"Squares counted after mess up: {squares_counted_after}")

    # Check if there are any squares on the messed up canvas and mess up again if there are squares
    while squares_counted_after > 0:
        print("Squares still found, messing up the canvas again...")
        mess_up_canvas(canvas_x, canvas_y, canvas_width, canvas_height)
        squares_counted_after = count_squares(canvas_region=canvas_region)
        print(
            f"Squares counted after additional mess up: {squares_counted_after}")

    print("No more squares found. Closing Paint.")
    # Close Paint
    pyautogui.hotkey('alt', 'f4')


if __name__ == "__main__":
    main()
