#!/usr/bin/python
# -*- coding: utf-8 -*-
import fitz
from PIL import Image
import sys

print(fitz.__doc__)
"""
Create a Pixmap from any PIL / Pillow supported filetype
Changes in v1.10.0
-------------------
- omit alpha to save image memory
"""
pic_fn = sys.argv[1] if len(sys.argv) == 2 else None
if pic_fn:
    print("Reading %s" % pic_fn)
    with open(pic_fn, "rb") as pic_f:
        img = Image.open(pic_f).convert("RGB")
        samples = img.tobytes()
        pix = fitz.Pixmap(fitz.csRGB, img.size[0], img.size[1], samples, 0)
        outputFileName = pic_fn + "-from-PIL.png"
        print("Writing %s" % outputFileName)
        pix.save(outputFileName)
