# PixiPi 
<a href="https://python.org"><img src="https://img.shields.io/badge/Code-Python-informational?style=plastic&logo=python&logoColor=white&color=2bbc8a"></a>
<a href="https://git-scm.com"><img src="https://img.shields.io/badge/Code-Git-informational?style=plastic&logo=git&logoColor=white&color=2bbc8a"></a>
<a href="https://github.com"><img src="https://img.shields.io/badge/Code-Github-informational?style=plastic&logo=github&logoColor=white&color=2bbc8a"></a>
<a href="https://github.com/aravinds-arv/PixiPi/archive/refs/heads/main.zip"><img src="https://img.shields.io/badge/Source-Download-informational?style=flat&logo=download&logoColor=white&color=2bbc8a"></a>
<a href="#"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Faravinds-arv%2FPixiPi%2F&count_bg=%232BBC8A&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Hits&edge_flat=false"/></a>

> _The swiss army knife for working with images ⚒️_

Tired of searching for online tools for tweaking your image as you please? If yes then **PixiPi** might just be the right tool for you 🪄

#### What is it? 💡
PixiPi is a simple command line toolkit for images. It was designed to have a minimal interface while offering a seamless user experience. With PixiPi, you can change the format of your image, resize it - enlarge or shrink an image and much more. The application is still in an early stage and a lot more features are being planned to be integrated in the not so distant future. But until then why wait.. give it a try and share your thoughts on it or maybe even open a pull request 😉

## Team Members
1. [Sreelakshmi AR](https://github.com/Sree-R5727)<br>
2. [Aravind S](https://github.com/aravinds-arv)

## Team ID
> _Python/619_

## Link to product walkthrough
...

## How it works?
- The command line interface is powered by [Typer](https://typer.tiangolo.com) library in python
- Typer application uses custom decorators to convert python fuctions to CLI commands
- The image manipulation functions of the program is handled by [Pillow](https://python-pillow.org) library

## Libraries used

|Library|Version|
|-|-|
|click|8.0.4|
|colorama|0.4.4|
|Pillow|9.0.1|
|shellingham|1.4.0|
|typer|0.4.0|

## How to configure
**Step 1:** Clone the repository
```bash
$ git clone https://github.com/aravinds-arv/PixiPi.git
```

**Step 2:** Change directory
```bash
$ cd PixiPi
```

**Step 3:** Create a virtual environment (_optional_)
```bash
$ python -m venv venv
```

**Step 4:** Activate the virtual environment
```bash
$ source venv/bin/activate
```

**Step 5:** Install all requirements
```bash
$ pip install -r requirements.txt
```

**Step 6:** Finally run PixiPi 🎉
```bash
$ python main.py
```

## How to Run
### Interactive menu driven 📃
> _Just run the program without any arguements and follow the prompts and options_
```bash
$ python main.py
```

### CLI command driven 💻
1. To Convert any image file to specified filetype
```bash
$ python main.py converto [TYPE]:[jpg|png|ico|bmp] [FILEPATH]
```

2. To reduce/shrink the size of the image by a specified factor
```bash
$ python main.py reduceby [FACTOR] [FILEPATH]
```

3. To reduce/shrink the size of the image by a specified factor
```bash
$ python main.py enlarge [FACTOR] [FILEPATH]
```

4. To display help
```bash
$ python main.py help
```
