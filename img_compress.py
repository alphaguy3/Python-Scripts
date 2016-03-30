#Script Name:	img_compress.py
#Author:	URJIT PATEL
#version:	1.0

from PIL import Image
import os

for f in os.listdir('.'):
    if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg'):
        i = Image.open(f)
        fn,fext = os.path.splitext(f)
        i.save('./{}{}'.format(fn,fext),optimize=True,quality=30)
