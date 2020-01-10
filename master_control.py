## this program is the master file of the whole program
## it controls the loop that constant is sending pictures
# and check the results

import os
from gpiozero import LED
import cv2
import cvlib as cv



#this is the location of where the image is to be saved
file_location = os.getcwd()
#this will give the image a name to locate it later so it can be sent away
file_name = 'image.jpg' 
#start picture object
camera = PiCamera()

#create light objects
red = LED(27)
yellow = LED(22)
green = LED(17)

#before loop starts show a yellow light for pending
yellow.on()

while True:
	try:
		#take picture
		camera.capture(file_location + '/' + file_name)
	except:
		print('ERROR: picture could not be taken.')
	try:
		#import picture
		im = cv2.imread(file_location + '/' + file_name)
	except:
		print('ERROR: File could not be imported'.)
	try:
		#run image to model
		bbox, label, conf = cv.detect_common_objects(im)
	except:
		print('ERROR: Model could not be run.')
        
    print(label)
    try:
        ##test if the response is a person or face
        #turn on or off lights accordingly
        if label == 'person':
            red.off()
            yellow.off()
            green.on()
        else:
            green.off()
            yellow.off()
            red.on()
    except:
        print('ERROR: Could not update signal.')
        break


#if the while loop breaks flash the red and yellow lights
# trhen turn them off as a warning
red.on()
red.off()
yellow.on()
yellow.off()





