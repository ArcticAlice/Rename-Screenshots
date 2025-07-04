import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:

            filename = os.path.basename(event.src_path)
            
            if filename.startswith("."):
                time.sleep(7)

            timestamp = time.strftime("%H-%M-%S")
            folder = os.path.dirname(event.src_path)
            dst_path = os.path.join(folder, f"{timestamp}.png")
            
            file = event.src_path.replace(".", "", 1)

            try:
                os.rename(file, dst_path)
                print(f"Renamed to {dst_path}")
            except Exception as e:
                print(f"Rename failed: {e}")

path_to_watch = "/Users/fakeName/Desktop"

observer = Observer()
observer.schedule(MyHandler(), path=path_to_watch, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
