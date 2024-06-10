from drawing import draw_squares, mess_up_canvas
from image_recognition import count_squares
import pyautogui

def main():
    # Open Paint
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('mspaint')
    pyautogui.press('enter')

    # Wait until Paint opens
    pyautogui.sleep(3)

    # Draw squares
    num_squares = draw_squares()

    # Count squares
    if count_squares() == num_squares:
        print("Neliöiden lukumäärä täsmää")

    # Mess up canvas
    mess_up_canvas()

    # Close Paint
    pyautogui.hotkey('alt', 'f4')

if __name__ == "__main__":
    main()

