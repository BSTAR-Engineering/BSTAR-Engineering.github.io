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

if len(sys.argv)<4:
    print("Not enough args!")
    exit(-1)
yaml_file = sys.argv[1]
data = yaml.load(open(yaml_file), Loader=yaml.Loader)
source_dir = sys.argv[2]
dest_dir = sys.argv[3]


for subdir, dirs, files in os.walk(source_dir):
    #print("in: '%s'"%(Path(subdir)))
    for file in files:
        processFile(subdir,file,source_dir,dest_dir,data)
