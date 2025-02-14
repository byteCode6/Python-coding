from playsound2 import playsound

import time
playsound("output.mp3")
time.sleep(1)
os.remove("output.mp3")
