# raspberry-pi-facial-recognition

This was a project my brother, Emmett (estorts), and I worked on for a day.  We wanted to build a person/facial recognition machine on a Raspberry Pi to use at his desk at work.

The program is somewhat simple.  To start there is a stop light signal at begins showing yellow.  A while loop begins and starts taking pictures.  The pictures are sent to the OpenCV detect_common_objects model.  With the resulting labels we determine if there is a person in the picture.  Based on the resulting labels we update the signal lights.


Thanks for reading and please don't be afraid to reach out with suggestions or ideas!
