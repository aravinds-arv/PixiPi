import os
import typer
from enum import Enum
from pathlib import Path
from typing import Optional
from PIL import Image

# initialize the typer application
app = typer.Typer()

# enum inherited custom class specifying supported file types
class SupportedFileTypes(str, Enum):
    jpg = "jpg"
    png = "png"
    ico = "ico"
    bmp = "bmp"

# helper function to check for supported file types
def check_support(type_prmt):
    global type_choice
    try:
        type_choice = SupportedFileTypes(type_choice.lower())
    except:
        typer.secho("Welp! we don't support that file type yet, please try again", fg=typer.colors.BRIGHT_RED)
        type_choice = typer.prompt(type_prmt)
        check_support(type_prmt)

# helper function to check for path validity
def check_path(path_prmt):
    global path_choice
    if not path_choice.exists():
        typer.secho("Hmm.. that's an invlid location! Please try again", fg=typer.colors.BRIGHT_RED)
        path_choice = Path(typer.prompt(path_prmt))
        check_path(path_prmt)

# helper function to check if prompt input is a valid integer
def check_int(scale_prmt):
    global scale_choice
    try:
        scale_choice = int(scale_choice)
    except Exception as e:
        typer.secho("Scaling factor cannot be a non-integer value -_-", fg=typer.colors.BRIGHT_RED)
        scale_choice = typer.prompt(scale_prmt)
        check_int(scale_prmt)

# helper function to display interactive menu and subsequent prompts
def options():
    print()
    prmt = typer.style('''        Choose an option:
                            1 - CHANGE FORMAT
                            2 - ENLARGE IMAGE
                            3 - REDUCE IMAGE
                            4 - PIXIPI HELP
                            5 - EXIT PIXIPI
       ➤ Choice''', fg=typer.colors.BRIGHT_BLUE)
    
    choice = typer.prompt(prmt)
    print()
    global type_choice
    global path_choice
    global scale_choice

    if choice == '1':
        typer.secho("You have selected 1", fg=typer.colors.BRIGHT_GREEN)
        type_prmt = typer.style("Type in the file type you need to convert to (JPG/PNG/BMP/ICO)", fg=typer.colors.BRIGHT_YELLOW)
        path_prmt = typer.style("Type in the location of your image (RELATIVE/ABSOLUTE PATH)", fg=typer.colors.BRIGHT_YELLOW)
        type_choice = typer.prompt(type_prmt)
        check_support(type_prmt)
        path_choice = Path(typer.prompt(path_prmt))
        check_path(path_prmt)
        converto(type=type_choice, path=path_choice)
    
    elif choice == '2':
        typer.secho("You have selected 2", fg=typer.colors.BRIGHT_GREEN)
        scale_prmt = typer.style("Type in the scaling factor to enlarge your image (INTEGER)", fg=typer.colors.BRIGHT_YELLOW)
        path_prmt = typer.style("Type in the location of your image (RELATIVE/ABSOLUTE PATH)", fg=typer.colors.BRIGHT_YELLOW)
        scale_choice = typer.prompt(scale_prmt)
        check_int(scale_prmt)
        path_choice = Path(typer.prompt(path_prmt))
        check_path(path_prmt)
        enlargeby(factor=scale_choice, path=path_choice)
    
    elif choice == '3':
        typer.secho("You have selected 3", fg=typer.colors.BRIGHT_GREEN)
        scale_prmt = typer.style("Type in the scaling factor to reduce your image (INTEGER)", fg=typer.colors.BRIGHT_YELLOW)
        path_prmt = typer.style("Type in the location of your image (RELATIVE/ABSOLUTE PATH)", fg=typer.colors.BRIGHT_YELLOW)
        scale_choice = typer.prompt(scale_prmt)
        check_int(scale_prmt)
        path_choice = Path(typer.prompt(path_prmt))
        check_path(path_prmt)
        reduceby(factor=scale_choice, path=path_choice)

    elif choice == '4':
        typer.secho("You have selected 4", fg=typer.colors.BRIGHT_GREEN)
        help()

    elif choice == '5':
        typer.secho("You have selected 4", fg=typer.colors.BRIGHT_GREEN)
        typer.secho("Exited.. until next time :D", fg=typer.colors.MAGENTA)
        raise typer.Exit()

    else:
        typer.secho("   That's an invalid option.. please try again", fg=typer.colors.BRIGHT_RED)
        options()

# file format converter command
@app.command()
def converto(type: Optional[SupportedFileTypes]= typer.Argument(None, case_sensitive=False), path: Optional[Path] = typer.Argument(None)):
    if type is None:
        typer.secho("Image type is missing.. please try again", fg=typer.colors.BRIGHT_RED)
        raise typer.Exit(code=1)
    elif path is None:
        typer.secho("Image path is missing.. please try again", fg=typer.colors.BRIGHT_RED)
        raise typer.Exit(code=2)
    elif not path.exists():
        typer.secho("That's an invalid path.. please try again", fg=typer.colors.BRIGHT_RED)
        raise typer.Exit(code=3)
    elif not str(path).lower().endswith(('.jpg', '.jpeg', 'png', '.ico', '.bmp')):
        typer.secho("Unsupported file format.. please use image files of JPG, JPEG, PNG, ICO, or BMP file types", fg=typer.colors.BRIGHT_YELLOW)
    else:
        typer.secho(f"Convering image to {type}...", fg=typer.colors.GREEN)
        image = Image.open(str(path))
        file_name = os.path.splitext(str(path))[0]
        rgb_im = image.convert('RGB')
        rgb_im.save(f"{file_name}.{type}")
        typer.secho(f"Image converted to {type} format and saved !!",  fg=typer.colors.BRIGHT_GREEN)

# image reduction command
@app.command()
def reduceby(factor: Optional[int]= typer.Argument(None, case_sensitive=False), path: Optional[Path] = typer.Argument(None)):
    if factor is None:
        typer.secho("The reduction factor is missing.. please try again", fg=typer.colors.BRIGHT_RED)
        raise typer.Exit(code=1)
    elif path is None:
        typer.secho("Image path is missing.. please try again", fg=typer.colors.BRIGHT_RED)
        raise typer.Exit(code=2)
    elif not path.exists():
        typer.secho("That's an invalid path.. please try again", fg=typer.colors.BRIGHT_RED)
        raise typer.Exit(code=3)
    elif not str(path).lower().endswith(('.jpg', '.jpeg', 'png', '.ico', '.bmp')):
        typer.secho("Unsupported file format.. please use image files of JPG, JPEG, PNG, ICO, or BMP file types", fg=typer.colors.BRIGHT_YELLOW)
    else:
        typer.secho(f"Reducing image by a factor of {factor}...", fg=typer.colors.GREEN)
        image = Image.open(str(path))
        file_name, ext = os.path.splitext(str(path))
        resized_img = image.resize((round(image.size[0]/factor), round(image.size[1]/factor)))
        resized_img.save(f"{file_name}_reduced_{factor}{ext}")
        typer.secho(f"Image reduced by a factor of {factor} and saved !!",  fg=typer.colors.BRIGHT_GREEN)

# image enlargement command
@app.command()
def enlargeby(factor: Optional[int]= typer.Argument(None, case_sensitive=False), path: Optional[Path] = typer.Argument(None)):
    if factor is None:
        typer.secho("The enlargement factor is missing.. please try again", fg=typer.colors.BRIGHT_RED)
        raise typer.Exit(code=1)
    elif path is None:
        typer.secho("Image path is missing.. please try again", fg=typer.colors.BRIGHT_RED)
        raise typer.Exit(code=2)
    elif not path.exists():
        typer.secho("That's an invalid path.. please try again", fg=typer.colors.BRIGHT_RED)
        raise typer.Exit(code=3)
    elif not str(path).lower().endswith(('.jpg', '.jpeg', 'png', '.ico', '.bmp')):
        typer.secho("Unsupported file format.. please use image files of JPG, JPEG, PNG, ICO, or BMP file types", fg=typer.colors.BRIGHT_YELLOW)
    else:
        typer.secho(f"Enlarging image by a factor of {factor}...", fg=typer.colors.GREEN)
        image = Image.open(str(path))
        file_name, ext = os.path.splitext(str(path))
        resized_img = image.resize((round(image.size[0]*factor), round(image.size[1]*factor)))
        resized_img.save(f"{file_name}_enlarged_{factor}{ext}")
        typer.secho(f"Image enlarged by a factor of {factor} and saved !!",  fg=typer.colors.BRIGHT_GREEN)

# PixiPi help command
@app.command()
def help():
    print()
    pixipi = typer.style("  𝔓𝔦𝔵𝔦𝔓𝔦: ", fg=typer.colors.WHITE, bold=True)
    swiss = typer.style('''𝔗𝔥𝔢 𝔰𝔴𝔦𝔰𝔰 𝔞𝔯𝔪𝔶 𝔨𝔫𝔦𝔣𝔢 𝔣𝔬𝔯 𝔴𝔬𝔯𝔨𝔦𝔫𝔤 𝔴𝔦𝔱𝔥 𝔦𝔪𝔞𝔤𝔢𝔰  ''', fg=typer.colors.BRIGHT_YELLOW)
    typer.secho(pixipi + swiss)
    print()
    typer.secho("  Here are the list of available commands to tweak your image..", fg=typer.colors.GREEN)
    typer.secho('''$ python main.py - To open the interactive menu (for lazy people ¯\_(ツ)_/¯)
$ python main.py converto [TYPE]:[jpg|png|ico|bmp] [FILEPATH] - To Convert any image file to specified filetype
$ python main.py reduceby [FACTOR] [FILEPATH] - To reduce/shrink the size of the image by the specified factor
$ python main.py enlarge [FACTOR] [FILEPATH] - To enlarge/increase the size of the image by the specified factor
$ python main.py help - Yep you guessed it right.. to open this help section :3''',
    fg=typer.colors.BRIGHT_BLUE)

# callback fuction invoked only when no other subcommand is invoked
# used to display the application banner, author and version details
@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        banner = typer.style('''
                    ██████╗ ██╗██╗  ██╗██╗██████╗ ██╗
                    ██╔══██╗██║╚██╗██╔╝██║██╔══██╗██║
                    ██████╔╝██║ ╚███╔╝ ██║██████╔╝██║
                    ██╔═══╝ ██║ ██╔██╗ ██║██╔═══╝ ██║
                    ██║     ██║██╔╝ ██╗██║██║     ██║
                    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝

    ▀▄▀▄▀▄  𝙰𝚞𝚝𝚑𝚘𝚛𝚜: 𝔄𝔯𝔞𝔳𝔦𝔫𝔡 𝔖 & 𝔖𝔯𝔢𝔢𝔩𝔞𝔨𝔰𝔥𝔪𝔦 𝔄ℜ 𝚅𝚎𝚛𝚜𝚒𝚘𝚗: 𝟢.𝟣.𝟢     ▀▄▀▄▀
    ''',  fg=typer.colors.WHITE)
        typer.echo(banner)
        typer.secho('''   《《Welcome to PixiPi.. The swiss army knife for working with images 》》''', fg=typer.colors.BRIGHT_YELLOW,  bold=True)
        options()

# run the app
if __name__ == '__main__':
    app()