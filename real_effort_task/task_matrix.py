from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import random

WIDTH = 450
HEIGHT = 360
# TEXT_SIZE = 32
# TEXT_PADDING = TEXT_SIZE
# IGNORED_CHARS = "↓"
# COUNTED_CHAR = "→"

INPUT_TYPE = "number"
INPUT_HINT = f"Count how many zeros in the matrix"


def generate_puzzle_fields():
    """Create new puzzle for a player"""

    n_zeros = random.choice(range(70,111))
    zero_seq = [0]*n_zeros + [1]*(180-n_zeros)
    random.shuffle(zero_seq)
    zero_seq = list(map(str, zero_seq))
    text = ''.join(zero_seq)
    return dict(text=text, solution=str(n_zeros))


def is_correct(response, puzzle):
    return puzzle.solution == response


def render_image(puzzle):
    image = Image.new(mode="RGB", size=(WIDTH, HEIGHT),color="white")
    draw = ImageDraw.Draw(image)
    init_x = 10
    init_y = 10
    seq = list(puzzle.text)
    font_size = ImageFont.truetype(font='_static/global/arial.ttf', size=22)
    for i,z in zip(range(len(seq)),seq):
        pos = divmod(i,15)
        draw.text((init_x+pos[1]*30,init_y+pos[0]*30), z,fill ="black", anchor="mm", font=font_size)

    return image
