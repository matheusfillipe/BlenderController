import sys
import os


sys.path.insert(0, '/home/matheus/projects/MotionServer/')

from bpy.types import Operator  
from server import serverHandler



bl_info = {  
     "name": "Blender Controller",  
     "author": "Matheus Fillipe (matheusfillipeag@gmail.com",  
     "version": (1, 0),  
     "blender": (2, 7, 9),  
     "location": "Outliner > View > Blender Controller",  
     "description": "Allows controlling rotation of objects with an android phone",  
     "warning": "",  
     "wiki_url": "",  
     "tracker_url": "",  
     "category": "Object"
     }  
    
server= serverHandler()

class BlenderController(bpy.types.Operator):  
    
    bl_idname = "object.blendercontroller_operator"  
    bl_label = "Blender Controller"  
   
      
    def execute(self, context):  
        
        if(server.serverThread.running):
            server.stop()          
            print("STOPPING CONTROLLER")
                                    
        else:       
            print("STARTING CONTROLLER")
            server.start() 


        return {'FINISHED'}  
    

def add_object_button(self, context):  
    self.layout.operator(  
    BlenderController.bl_idname,  
    text=BlenderController.bl_label,  
    icon='PLUGIN')  

      
def register():  
    bpy.utils.register_class(BlenderController)  
    bpy.types.OUTLINER_MT_view.append(add_object_button)
    
def unregister():
    bpy.utils.unregister_class(BlenderController) 
    bpy.types.OUTLINER_MT_view.remove(add_object_button)
      
if __name__ == "__main__":  
    register()  