# PythonResize

PythonResize is a simple command line tool that lets you resize an image to a size or a collection of sizes.

## Usage
`resize <filename> <options>`

## Examples
```
resize image.png -w 1024 -h 728
resize image.png -l sizes.csv
```

## Options

| Command Line Switch | Description         |
| ------------------- | ------------------- |
| `--width` or `-w`:  | Change the output width of the image, in pixels. |
| `--height` or `-h`: | Change the output height of the image, in pixels. |
| `--list` or `-l`:   | Specify a CSV list of sizes to be used to resize the image into. |

## Using `--list`
You can make a CSV list of widths and heights to resize an image into many different sizes. For example, we could make a file called `icons.csv` with this inside:
```
512,512
192,192
144,144
92,92
72,72
48,48
36,36
```
If you then ran this:
```
resize icon.png --list icons.csv
```
It would generate 7 new image files, one of which is 512x512, one of which is 192x192, etc. This is very useful if you need to make an icon or image lots of different sizes for different screen densities.

## Building from source
**NOTE:** This might work on lower versions of Python than 3.4, but that hasn't been tested, so 3.4 is recommended. Also, this hasn't been tested on OSes other than Windows.

First, you'll need to install [Click](http://click.pocoo.org/5/) (`pip install click`) and [Pillow](https://python-pillow.github.io/) (`pip install Pillow`).

After that, you can simply just type `py resize.py` from your command line to use this tool, but if you're on Windows you can use `dist/resize.exe` instead. If you have `cxfreeze` installed and in your PATH (use `pip install cx_Freeze`), you can run `build.bat` to rebuild that executable file. 

## Warranty
THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
