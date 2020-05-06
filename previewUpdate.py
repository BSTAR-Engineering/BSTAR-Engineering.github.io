import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
import sys
from pathlib import Path




def on_modified(event):
    pyexec=os.path.split(Path(sys.executable))[1]
    os.system("%s generateWebsite.py website-source/content/content.yml website-source/template website"%(pyexec))

if __name__ == "__main__":
    pyexec=os.path.split(Path(sys.executable))[1]
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_modified
    my_event_handler.on_deleted = on_modified
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_modified
    path = "website-source"
    go_recursively = True
    os.system("%s generateWebsite.py website-source/content/content.yml website-source/template website"%(pyexec))
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    my_observer.start()
    os.system("cd website && %s -m http.server &"%(pyexec))
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
