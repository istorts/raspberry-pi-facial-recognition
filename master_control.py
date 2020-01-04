## this program is the master file of the whole program
## it controls the loop that constant is sending pictures
# and check the results


import picture_capture
import submit_picture
import signal_control
import os
from gpiozero import LED

#this is the location of where the image is to be saved
file_location = os.getcwd() 
#this will give the image a name to locate it later so it can be sent away
file_name = 'image.jpg' 
#s3 bucket name
bucket = 'raspberry-pi-facial-recognition'

#create light objects
red = LED(27)
yellow = LED(22)
green = LED(17)

#before loop starts show a yellow light for pending
yellow.on()

while True:
	try:
		#take picture
		picture_capture.take_picture(file_location, file_name)
	except:
		print('ERROR: Could not take picutre')
		break
	try:
		#send picture from Pi to s3
		submit_picture.upload_to_s3(file_location, file_name)
	except:
		print('ERROR: Could not upload image to s3')
		break
	try:
		#send picture from s3 to rekognition
		response = submit_picture.send_to_rek(file_name)
	except:
		print('ERROR: Could submit image to rekognition.')
		break
	try:
		#take the response update signal
		signal_control.signal(response)
	except:
		print('ERROR: Could not update signal.')
		break


red.on()
red.off()
yellow.on()
yellow.off()





