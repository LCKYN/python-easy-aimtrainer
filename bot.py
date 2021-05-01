import pyautogui
import keyboard
from statistics import mean
import time

try:
    while 1:
        while keyboard.is_pressed('w'):
            x, y = pyautogui.position()

            pic = pyautogui.screenshot(region=(850*2, 234*2, 810*2, 482*2))
            # pic.save('my_screenshot.png')

            w, h = pic.size

            for x in range(0, w, 2):
                for y in range(0, h, 5):
                    pixelColor = pic.getpixel((x, y))

                    if(mean(pixelColor) > 150):
                        pyautogui.click(850 + x//2, 234 + y//2)
                        # pyautogui.moveTo(850*2 + x, 234*2 + x)
                        # pyautogui.moveTo(850 + x//2, 234 + y//2)
                        time.sleep(0.05)
                        break
except KeyboardInterrupt:
    print("\nDone...")

    #  3840 2400
