## This program will accept a picture file 
# upload it to an AWS S3 bucket and then submit that picture to 
# AWS rekgonition.
# Then it will process the JSON response and return a response

# written by Emmett Storts
# email: emmett.storts14@gmail.com
# Date: 1/3/2020

import boto3


def upload_to_s3(file_location, file_name):
	'''
	Upload file, given by the file_name, to the program s3 bucket
	'''
   
	#boto3 S3 client
	s3 = boto3.client('s3')

	try:
	    #upload file to s3
		s3.upload_file(file_location, bucket, file_name)
		return print('File was uploaded to S3.')
	except:
		return print('Error File did not upload to S3.')


def send_to_rek(file_name):
	'''
	this function sends the picture uploaded in the S3 bucket to 
	AWS rekognition
	'''

	#boto3 rekognition client
	rk = boto3.client('rekognition')

	#json request
	request = {
	        "S3Object": {
	            "Bucket": bucket,
	            "Name": file_name
	        }
	    }

	#send json request to rekognition
	full_response = rk.detect_labels(Image = request,
								MaxLabels = 1,
								MinConfidence = 60.0)

	#unpack the response for the 200 confirm code
	response_code = full_response['ResponseMetadata']['HTTPStatusCode']

	if response_code == 200:
		print('Response was successful')
		return full_response['Labels'][0]['Name']
	else:
		return print("ERROR: image did not return a response")
