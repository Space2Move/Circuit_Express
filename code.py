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
    (0, 0, 0)       # Black
]

while True:
    for i in range(10):
        cp.pixels.fill((0, 0, 0))  # Turn off all LEDs
        cp.pixels[i] = colors[i]  # Turn on the current LED
        time.sleep(0.1)  # Wait for half a second