import bpy
from math import pi

"""
TODOS: Implement object dragging with mobile acelerometers?
...

"""

class controller():
    def __init__(self, *args, **kwargs):
        pass
    



    def receivedMotionData(self,motionData):
        obj = bpy.data.objects["body"]
        obj.rotation_mode = 'XYZ'

        obj.rotation_euler.y = float(float(motionData['z'])*pi/180.0)

        obj.rotation_euler.x =  float(float(motionData['y'])*pi/180.0)
        obj.rotation_euler.z = float(float(motionData['x'])*pi/180.0)

        log="Recieved: " + "z:" + str(motionData['x']) + " y: " + str(motionData['y']) + " x :" + str(motionData['z'])
        print(log)
        pass