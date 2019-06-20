from picamera import PiCamera
from time import sleep
from subprocess import call 

# Setup the camera
print("Start Recording.....")
with PiCamera() as camera:
    camera.start_recording("/home/ubuntu/Desktop/cookie/pythonvideo.h264")
    sleep(5)
    camera.stop_recording()
print("Recording Finished.")

# Start converting 
print("Start Converting.....")
command = "MP4Box -add {} {} ".format("/home/ubuntu/Desktop/cookie/pythonvideo.h264", "/home/ubuntu/Desktop/cookie/pythonvideo_converted.mp4")
call([command], shell=True)
print("Converting finished")
