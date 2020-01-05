#raspberry pi
from picamera import PiCamera

#create pi camera object
camera = PiCamera()

def take_picture(file_location, file_name):
    '''
    this function takes a picture and
    returns the file name
    '''
    #after the sensor rests it will capture an image
    camera.capture(file_location + '/' + file_name)
    #function will return image file name
    return print('Picture was taken')
    
