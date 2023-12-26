'''
http://doc.aldebaran.com/2-8/naoqi/vision/alphotocapture-tuto.html
'''

# This test demonstrates how to use the ALPhotoCapture module.
# Note that you might not have this module depending on your distribution
import os
import sys
import time
from naoqi import ALProxy

# Replace this with your robot's IP address
IP = "172.9.0.86"
PORT = 9559

# Create a proxy to ALPhotoCapture
try:
  photoCaptureProxy = ALProxy("ALPhotoCapture", IP, PORT)
except Exception, e:
  print "Error when creating ALPhotoCapture proxy:"
  print str(e)
  exit(1)

# Take 3 pictures in VGA and store them in /home/nao/recordings/cameras/

photoCaptureProxy.setResolution(2)
photoCaptureProxy.setPictureFormat("jpg")
photoCaptureProxy.takePictures(3, "Users/adsonalves/Desktop/NAO-NPL/NAO/img", "image")
print "ok"