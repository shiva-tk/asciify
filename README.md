# asciify - a python tool which generates ascii art for any image

## Installation
1. Clone the repository
2. Run setup.py:

```
sudo python setup.py install
```

3. To uninstall, run:

```
sudo pip uninstall asciify
```

## Usage

```
asciify -i /filepath/to/image.png -w 1234 -I False
```

*Where:*
- `/filepath/to/image.png` is replaced with the filepath to the image you want to asciify
- `1234` is replaced with the width of the output text in characters
- `False` is replaced with whether or not the output should be inverted - by default the output is for black text on a white background

Use `asciify -h` for more details.
