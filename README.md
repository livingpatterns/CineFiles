# CineFiles
Dealing with .cine files from the Phantom Camera. Convert to TIFF, extract metadata, etc.

## How to use it
1. Go to __main__ .
2. Change the path of your .cine file. This is also where the tiff and the metadata files are going to be written to.
3. If the file is too large, an error is going to be raised. IN that case, change bigtiff=False to True in the call to the imwrite function.
