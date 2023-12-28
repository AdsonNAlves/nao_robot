# -*- encoding: UTF-8 -*-

# This is just an example script that shows how images can be accessed
# through ALVideoDevice in python.
# Nothing interesting is done with the images in this example.
# http://doc.aldebaran.com/1-14/dev/python/examples/vision/get_image.html

# from naoqi import ALProxy
from pynaoqi_mate import Mate
import vision_definitions

# IP = "nao.local"  # Replace here with your NAOqi's IP address.
# PORT = 9559

m=Mate("172.9.0.86",9559)
####
# Create proxy on ALVideoDevice

# print "Creating ALVideoDevice proxy to ", IP

# camProxy = ALProxy("ALVideoDevice", IP, PORT)

####
# Register a Generic Video Module

resolution = vision_definitions.kQVGA
colorSpace = vision_definitions.kYUVColorSpace
fps = 30

# nameId = camProxy.subscribe("python_GVM", resolution, colorSpace, fps)
nameId = m.ALVideoDevice.subscribe("python_GVM", resolution, colorSpace, fps)

print nameId

print 'getting images in local'
for i in range(0, 20):
  m.ALVideoDevice.getImageLocal(nameId)
  m.ALVideoDevice.releaseImage(nameId)

resolution = vision_definitions.kQQVGA
m.ALVideoDevice.setResolution(nameId, resolution)

print 'getting images in remote'
for i in range(0, 20):
  m.ALVideoDevice.getImageRemote(nameId)

m.ALVideoDevice.unsubscribe(nameId)

print 'end of gvm_getImageLocal python script'