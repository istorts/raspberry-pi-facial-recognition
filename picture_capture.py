#raspberry pi
from picamera import PiCamera
from time import sleep
import os

camera = PiCamera()

#@camera.start_preview() this was for testing it shows what the camera sees
def take_picture():
    '''
    this function takes a picture every 10 seconds and
    returns the file name
    '''
    sleep(10)  #10 seconds so the sensor can sense light levels
    file_location = os.getcwd() #this is the location of where the image is to be saved
    file_name = 'image.jpg' #this will give the image a name to locate it later so it can be sent away
    camera.capture(file_location + '/' + file_name)#after the sensor rests it will capture an image
    #function will return image file name
    return file_name
    



#camera.stop_preview(_)  this ends a preview
    
#final step send signal to tell whether or not a person was recognized
#if result == Person signal green
    #else signal red 