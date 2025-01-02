Overview

This project uses Python and PyAutoGUI to automate the following steps in Microsoft Paint:

- Launch Paint and maximize the window.
- Detect the canvas area with a reference image.
- Randomly draw a certain number of squares on the canvas.
- Count how many squares are detected (using another reference image).
- “Mess up” the canvas by drawing random lines and shapes.
- Recount squares until none are found, then close Paint.

Requirements:

- Python 3.x
- PyAutoGUI
- Microsoft Paint (tested on Windows)
- Matching reference images for canvas_full.png (empty Paint canvas) and square_image.png (model of the drawn square)

Usage:

- Place the images (canvas_full.png, square_image.png) in the same directory as the scripts or adjust paths accordingly.
- Run python main.py.
- Make sure to not interfere with mouse or keyboard while the script is running.

Notes:

- The script relies on screen captures to match the reference images. Any changes in Windows scaling, theme, or Paint UI may affect detection.
- Adjust sleep durations in the script if your system is slower or faster.