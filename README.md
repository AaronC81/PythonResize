#PythonResize

PythonResize is a simple command line tool that lets you resize an image to a size or a collection of sizes.

##Usage
`resize <filename> <options>`

##Examples
```
resize image.png -w 1024 -h 728
resize image.png -l sizes.csv
```

##Options
| Command Line Switch | Description         |
| ------------------- | ------------------- |
| `--width` or `-w`:  | Change the output width of the image, in pixels. |
| `--height` or `-h`: | Change the output height of the image, in pixels. |
| `--list` or `-l`:   | Specify a CSV list of sizes to be used to resize the image into. |

##Using `--list`

##Building from source
**NOTE:** This might work on lower versions of Python than 3.4, but that hasn't been tested, so 3.4 is recommended. Also, this hasn't been tested on OSes other than Windows.

First, you'll need to install [Click](http://click.pocoo.org/5/) (`pip install click`) and [Pillow](https://python-pillow.github.io/) (`pip install Pillow`).

After that, you can simply just type `py resize.py` from your command line to use this tool, but if you're on Windows you can use `dist/resize.exe` instead. If you have `cxfreeze` installed and in your PATH (use `pip install cx_Freeze`), you can run `build.bat` to rebuild that executable file.

##Warranty
THE PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT WITHOUT ANY WARRANTY. IT IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW THE AUTHOR WILL BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.