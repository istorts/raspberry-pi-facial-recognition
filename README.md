# raspberry-pi-facial-recognition

This was a project my brother, estorts, and I worked on for a day.  We wanted to build a person/facial recognition machine on a Raspberry Pi to use at his desk at work.

The program is somewhat simple.  To start there is a stop light signal at begins showing yellow.  Every 10 seconds or so the Pi takes a picutre and saves it to and AWS S3 bucket.  From there the image is submitted to AWS Rekognition with only one response allowed.  The program takes the response and extracts the label.  If the model detects a "Person" or "Face" the stop light signal is updated to green, if it is anything else the stop light turns to red.  

We plan to make future updates to the program.  Maybe adding fimilar faces and update the lights according to those people.  Any other ideas are welcome.

Thanks for reading and please don't be afraid to reach out with suggestions or ideas!
