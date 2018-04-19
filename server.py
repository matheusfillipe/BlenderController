import json
import threading
import traceback


import sys
import os

from SimpleWebSocketServer import  SimpleWebSocketServer, WebSocket
from controller import controller

rotationControl=controller()

class SimpleEcho(WebSocket):
    
   
    def handleMessage(self):

        #self.sendMessage(self.data)
        try:
            rotationControl.receivedMotionData(json.loads(self.data))
        except Exception as e:
            print(e)


    def handleConnected(self):
        print(self.address, 'connected')
        print("Websocket Opened")

    def handleClose(self):
        print(self.address, 'closed')
        print("Websocket closed")


class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.server=SimpleWebSocketServer('', 9845, SimpleEcho)
        self.running = False
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()
        self.running = False
        self.server.run = False


    def stopped(self):
        return self._stop_event.is_set()
     

    def run(self):
        self.running=True        
        try:            
            self.server.serve()

        except Exception as e:                  
            self.stop()
            print (e) 
            pass






class serverHandler():

    def __init__(self):
        self.serverThread = ServerThread()
    
                
    
    def start(self):
        try:
            if self.serverThread.running == False:       
                self.serverThread.daemon=True
                self.serverThread.start()
                print("Starting server")
            else:
                print("Server already running, using new motion handler.")
        except Exception as e:
       

            self.serverThread.start()
        print("Starting server")

    def stop(self):
        self.serverThread.running=False
        self.serverThread.stop()
        self.serverThread = ServerThread()

