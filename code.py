from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.02

colors = [
    (255, 0, 0),    # Red
    (255, 165, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 128, 0),    # Green
    (0, 0, 255),    # Blue
    (75, 0, 130),   # Indigo
    (238, 130, 238),# Violet
    (255, 192, 203),# Pink
    (255, 255, 255),# White
    (255, 192, 203),# Pink
]

direction = 1  # 1 for forward, -1 for backward
i = 0  # Start from the first LED

while True:
    cp.pixels.fill((0, 0, 0))  # Turn off all LEDs
    cp.pixels[i] = colors[i]  # Turn on the current LED
    time.sleep(0.1)  # Wait for quarter second
    if cp.button_a:  # If button A is pressed
        direction *= -1  # Change direction
    i += direction  # Move to the next or previous LED
    if i >= 10:  # If the end is reached
        i = 0  # Start from the beginning
    elif i < 0:  # If the beginning is reached
        i = 9  # Start from the end