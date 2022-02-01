from __future__ import print_function
import sys
import fitz

# ------------------------------------------------------------------------------
# Example program
# License: GNU AGPL V3
# Extracts an embedded file from an existing PDF
# Command line:
# python embedded-export.py input.pdf name export.file
# ------------------------------------------------------------------------------
pdffn = sys.argv[1]  # PDF file name
name = sys.argv[2]  # embedded file identifier
expfn = sys.argv[3]  # filename of exported file

doc = fitz.open(pdffn)  # open PDF
with open(expfn, "wb") as outfile:
    # extract file content. Will get exception on any error.
    content = doc.embfile_get(name)

    outfile.write(content)