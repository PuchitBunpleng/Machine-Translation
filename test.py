from glob import glob
import os

files = []
for folder in glob('src/models/*'):
    for file in glob(os.path.join(folder,'*')):
        files.append((file, file))
print(files)