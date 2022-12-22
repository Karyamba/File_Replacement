from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            file = folder_track + "/" + filename
            new_path = folder_dest + "/" + filename
            os.rename(file,new_path)
            
newpath = r'D:\source_new'
if not os.path.exists(newpath):
    os.makedirs(newpath)

newpath1 = r'D:\dest_new'
if not os.path.exists(newpath1):
    os.makedirs(newpath1)

folder_track = 'D:/source_new'
folder_dest = 'D:/dest_new'

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()