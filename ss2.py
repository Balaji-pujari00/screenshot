import pyscreenshot
import pyautogui
image=pyscreenshot.grab(bbox=(180,169,990,1018))
image.show()
image.save("screenshot")
