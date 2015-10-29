import click
from PIL import Image
import csv
import time
import os
import imghdr

def onerror(*args):
    click.echo(click.style("ERROR: " + args[0] + ". Type resize --help for help.", bg="red", fg="white"))
    if len(args) == 2: print("ERROR DETAILS: ", args[1])

def onwarning(war):
    click.echo(click.style("WARNING: " + war + ".", bg="yellow", fg="black"))

def oninfo(inf): click.echo(click.style("INFO: " + inf, fg="white"))

def onsuccess(inf): click.echo(click.style("SUCCESS: " + inf, fg="white", bg="green"))

@click.command()
@click.argument("file", type=str)
@click.option("--method", "-m", type=click.Choice(["nearest", "bilinear", "bicubic", "antialias"]), help="The method that should be used to resize the image.", default="nearest")
@click.option("--width", "-w", type=int, help="The width that the generated image should be.")
@click.option("--height", "-h", type=int, help="The height that the generated image should be.")
@click.option("--list", "-l", type=str, help="A CSV list of file sizes to resize the image into.")
def resize(file, method, width, height, list):
    start = time.time()

    if file is None: return onerror("--file was not specified")
    if width is None and height is None and list is None: return onerror("A size wasn't specified. Specify a size using either --width and --height, or by using --list")
    if (width is None and height is not None) or(height is None and width is not None): return onerror("If you specify --width, you must also specify --height, or vice versa")
    if width is not None and height is not None and list is not None: return onerror("You cannot use all of --list, --width and --height. Use either just --list, or just --width and --height")

    sizes = []

    if list is None:
        sizes.append((width, height))
    else:
        try:
            with open(list) as csvf:
                reader = csv.reader(csvf)
                for i, row in enumerate(reader):
                    if len(row) is not 2:
                        return onerror("There are " + ("too many" if len(row) > 2 else "too few") + " elements on line " + str(i + 1) + " in " + list)
                    try:
                        sizes.append([int(x) for x in row])
                    except:
                        return onerror("Line " + str(i + 1) + " of " + list + " contains a non-integer value")

        except FileNotFoundError:
            return onerror("The file " + list + " doesn't exist")
        except Exception as e:
            return onerror("An error occured while opening " + list, e)

    if not any(sizes):
        onwarning("There weren't any sizes in " + list + ", so the image won't be resized")
    else:
        img = None
        try:
            img = Image.open(file)
        except:
            return onerror("The image " + file + " could not be opened - make sure it exists")
        for size in sizes:
            resizedimg = img.resize(tuple(size))
            finalfilename = os.path.splitext(file)[0] + "-" + str(size[0]) + "x" + str(size[1]) + "." + imghdr.what(file)
            if os.path.isfile(finalfilename):
                if click.confirm("A file already exists at " + finalfilename + ". Do you want to overwrite it?"):
                    resizedimg.save(finalfilename)
                    oninfo("Saved " + finalfilename)
                else:
                    oninfo("Have not saved " + finalfilename + " based on user preference.")
            else:
                resizedimg.save(finalfilename)
                oninfo("Saved " + finalfilename)



    end = time.time()
    onsuccess("Request completed successfully in " + str(round(end - start, 3)) + " seconds.")

if __name__ == "__main__":
    resize()