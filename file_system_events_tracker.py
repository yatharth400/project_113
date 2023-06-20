import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "c:/Users/yatharth999/Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):     
    def on_created(self, event):
        print(" Hey,{event.src_path} has been created!")
    def on_deleted(self, event):
        print("Oops! somemone deleted{event.src_path}!")
    def on_modified(self, event):
        print("Hey There!,{event.src_path} has been modified")   
    def on_moved(self, event):
        print("Someone Moved {event.src_path} to{event.dest_path}")

    #2_on_deleted

    #3_on_modified

    #4_on_moved

        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt
try:
    while True:
     time.sleep(2)
     print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
    







