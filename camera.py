from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.annotate_text = "NovoAidar"
sleep(100)
camera.stop_preview()
