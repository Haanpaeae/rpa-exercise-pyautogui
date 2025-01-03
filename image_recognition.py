import pyautogui


def count_squares(image_path='square_image.png', canvas_region=None):
    try:
        if canvas_region:
            print(f"Using canvas region: {canvas_region}")
            squares = list(pyautogui.locateAllOnScreen(
                image_path, confidence=0.9, region=canvas_region))
        else:
            squares = list(pyautogui.locateAllOnScreen(
                image_path, confidence=0.9))
    except pyautogui.ImageNotFoundException:
        print("No squares found. ImageNotFoundException caught.")
        return 0

    if not squares:
        print("No squares found.")
        return 0
    return len(squares)
