import pystache
import os
import sys
from pathlib import Path
import shutil
import yaml

def processFile(path,file,source,dest,contents):
    #print("\tfile: '%s'"%(file))
    # Does it end in .stsh?
    filename,filext = os.path.splitext(file)

    file_from = os.path.join(path,file)
    file_to   = os.path.join(dest,os.path.relpath(path,start=source),file)
    #print("\t\tfrom: '%s'\t to: '%s'"%(file_from,file_to))

    #Do we need to create a new directory?
    directory = os.path.split(file_to)[0]
    #print(directory)
    Path(directory).mkdir(parents=True, exist_ok=True)
    # Copy the file
    if filext=='.stsh':
        print("processing template '%s'"%(file_from) )
        file_to   = os.path.join(dest,os.path.relpath(path,start=source),filename)
        content_file = open(file_from, 'r')
        template_content = content_file.read()
        template_content_processed = pystache.render(template_content, contents)
        f = open(file_to, "w")
        f.write(template_content_processed)
        f.close()
    else:
        shutil.copyfile(file_from,file_to)

def loadContent(content_path):
    # Is this a directory or a file?
    data={}
    if os.path.isfile(content_path):
        # just load it
        filename,filext = os.path.splitext(file)
        if filext=='.yml':
            data = yaml.load(open(content_path), Loader=yaml.Loader)
    else:
        #Walk through all nested directories and load any yml files.
        for subdir, dirs, files in os.walk(content_path):
            for file in files:
                file_from = os.path.join(subdir,file)
                filename,filext = os.path.splitext(file)
                if filext==".yml":
                    print("Loading content file '%s'"%(file))
                    data_part = yaml.load(open(file_from), Loader=yaml.Loader)
                    data.update(data_part)
            # merge, replace same-key-values unless its an array in wich case, append

    return data

if len(sys.argv)<4:
    print("Not enough args!")
    exit(-1)
yaml_file = sys.argv[1]
data = loadContent(yaml_file)
source_dir = sys.argv[2]
dest_dir = sys.argv[3]


for subdir, dirs, files in os.walk(source_dir):
    #print("in: '%s'"%(Path(subdir)))
    for file in files:
        processFile(subdir,file,source_dir,dest_dir,data)
